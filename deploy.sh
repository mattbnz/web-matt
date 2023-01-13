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
    echo "Could not fetch latest version, got: $LATEST"
    exit 1
fi

CURRENT=$(cat current 2>/dev/null)
if [ "$CURRENT" == "$LATEST" ]; then
    echo "Site is up to date!"
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

OLD=$(find ./html/ -type f | wc -l)
CHANGED=$(diff -uwbr html/ "$SD/" | diffstat -s | awk '{print $1}')
let THOLD="$OLD / 10"
if [ "$CHANGED" -gt "$THOLD" -a "$FORCE" != "1" ]; then
    echo "Error: $CHANGED/$OLD files changed (> $THOLD). Cannot proceed"
    exit 1
fi

echo "$CHANGED/$OLD files are being updated"
rsync -aqvz --delete "$SD/" html/
if [ "$?" != "0" ]; then
    echo "Error: rsync failed, state may be inconsistent!"
    exit 1
fi
echo "$LATEST" > ./current
echo "Site is now serving from $LATEST"