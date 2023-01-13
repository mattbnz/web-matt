#!/bin/sh
#
# Debian ifupdown hook script for madwifi-ng
#
# Author:   Matt Brown <matt@mattb.net.nz>
# Version:  1.0
#
# Copyright (C) 2005    Matt Brown
#
# This is free software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# This is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# crcnetd; if not, write to the Free Software Foundation, Inc., 59 Temple
# Place, Suite 330, Boston, MA 02111-1307 USA
#
WLANCONFIG=/usr/bin/wlanconfig

if [ ! -x $WLANCONFIG ]; then
  exit 0
fi

if [ -z "$IF_MADWIFI_BASE" ]; then
	exit 0
fi

# Check for interface
if ip link list $IFACE &>/dev/null; then
	# Destroy 
	$WLANCONFIG $IFACE destroy
fi

case "$IF_WIRELESS_MODE" in
Managed|managed|MANAGED)
	MODE="sta"
	;;
Ad-Hoc|ad-hoc|AD-HOC)
	MODE="adhoc"
	;;
Master|master|MASTER)
	MODE="ap"
	;;
Monitor|monitor|MONITOR)
	MODE="monitor"
	;;
*)
	MODE="sta"
	;;
esac

# Create or recreate interface
$WLANCONFIG $IFACE create wlandev $IF_MADWIFI_BASE wlanmode $MODE &>/dev/null
exit $?
