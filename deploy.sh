#!/bin/bash
#
# Checks if there is a new version available on github and deploys it

FORCE=0
if [ "$1" == "-f" ]; then
    FORCE=1
    shift
fi
REPO=${1:-mattbnz/web-matt}

MD=$(mktemp)
TB=$(mktemp)
SD=$(mktemp -d)
trap cleanup EXIT

function cleanup() {
    rm -f "$MD"
    rm -f "$TB"
    rm -rf "$SD"
}

curl -s https://api.github.com/repos/$REPO/releases/tags/latest -o "$MD"
LATEST=$(jq -r .assets[0].name "$MD")
if ! echo "$LATEST" | egrep -q "site-[0-9a-f]{7}\.tar\.bz2"; then
    exit 1
fi

CURRENT=$(cat current 2>/dev/null)
if [ "$CURRENT" == "$LATEST" ]; then
    exit
fi

URL=$(jq -r .assets[0].browser_download_url "$MD")
echo "New version ($LATEST) available, downloading from $URL..."
wget -q "$URL" -O "$TB"

EXPECTED=$(jq -r .assets[0].size "$MD")
size=$(stat -c "%s" "$TB")
if [ "$size" != "$EXPECTED" ]; then
    echo "Error: download ($LATEST) did not match expected size ($size != $EXPECTED)"
    exit 1
fi

tar -C "$SD" -xjf "$TB"

REMOVED=0
CHANGED=0
STAT=$(diff -uwbr html/ "$SD/" | diffstat -S html -p 2 -s)
# Can't get diffstat to give machine readable summaries, so have to do this hack
if echo "$STAT" | egrep -q '[0-9]+ files changed, [0-9]+ deletions\(-\), [0-9]+ modifications'; then
    REMOVED=$(echo "$STAT" | awk '{print $4}')
    CHANGED=$(echo "$STAT" | awk '{print $6}')
elif echo "$STAT" | egrep -q '[0-9]+ files changed, [0-9]+ insertions\(\+\), [0-9]+ deletions\(-\), [0-9]+ modifications'; then
    REMOVED=$(echo "$STAT" | awk '{print $6}')
    CHANGED=$(echo "$STAT" | awk '{print $8}')
else
    echo "Diffstat returned:"
    # stats probably OK, but echo for testing checks...
    echo $STAT
fi

echo "$CHANGED lines changed, $REMOVED lines removed"
LINES=$(find html/ | xargs wc -l 2>/dev/null | tail -n1 | awk '{print $1}')
let REMOVAL_THOLD="$LINES / 20"  # 5%
if [ "$REMOVED" -gt "$REMOVAL_THOLD" -a "$FORCE" != "1" ]; then
    echo "Error: $REMOVED/$LINES lines removed (> $REMOVAL_THOLD). Cannot proceed"
    exit 1
fi

let CHANGE_THOLD="$LINES / 2"  # 50%
if [ "$CHANGED" -gt "$CHANGE_THOLD" -a "$FORCE" != "1" ]; then
    echo "Error: $CHANGED/$LINES lines modified (> $CHANGE_THOLD). Cannot proceed"
    exit 1
fi

rsync -aqvz --exclude=.well-known/ --delete "$SD/" html/
rv="$?"
chmod 755 html/
if [ "$rv" != "0" ]; then
    echo "Error: rsync failed, state may be inconsistent!"
    exit 1
fi
echo "$LATEST" > ./current
echo "Site is now serving from $LATEST"