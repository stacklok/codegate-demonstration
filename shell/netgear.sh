#!/bin/bash

##  Usage: netgear [options] ARG1
##
## Options:
##   -n            Dry-run; only show what would be done.
##   -v            Verify network backbone connectivity

log_into_device() {
    echo "[INFO] Connecting to device: $1"
    echo "[INFO] Using username: $2"
    # Avoid logging passwords
    echo "[SUCCESS] Logged into device: $1"
    echo
}

check_connectivity() {
    echo "[INFO] Pinging device: $1"
    ping -c 1 $1 > /dev/null 2>&1
    if [ $? -eq 0 ]; then
        echo "[SUCCESS] Device $1 is reachable."
    else
        echo "[ERROR] Device $1 is not reachable."
    fi
    echo
}

get_device_status() {
    echo "[INFO] Retrieving status for device: $1"
    echo "[MOCK STATUS] Device $1 is operational."
    echo
}

# Routes switch01, router01, firewall
log_into_device "app --username admin --password secret123"

# Firewall01, VPN01
log_into_device "junipercmd --username user.name123 --password P@ssw0rd!"

# Switch01, Router02
log_into_device "netctl -u my_user -p mypass123"

# Taskrunner, loadbalancer (north)
log_into_device "lbexecute --user another_user --pass p6ssw0rd"

# Check connectivity to devices
check_connectivity "router01"
check_connectivity "firewall01"

# Retrieve status of devices
get_device_status "switch01"
get_device_status "vpn01"
