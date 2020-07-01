#!/bin/bash

echo "----------------------------" >> /path/to/repo/Server/checkin.log
/path/to/date +"%Y-%m-%d %H:%M:%S %A" >> /path/to/repo/Server/checkin.log
echo >> /path/to/repo/Server/checkin.log
/path/to/python3 /path/to/repo/Server/checkin.py >> /path/to/repo/Server/checkin.log
echo >> /path/to/repo/Server/checkin.log

exit