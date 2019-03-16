#!/bin/bash
tar --exclude='/opt/backup' --exclude='/dev' --exclude='/tmp' --exclude='/sys' --exclude='/proc' --exclude='/mnt' --exclude='/run' --exclude='/media' --exclude='/usr/src' --exclude='/usr/ports' --exclude='/var/cache' -cvpJf backup-`date -Idate`.txz /