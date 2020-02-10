# BatMan - Battery Manager for your Linux System
# @author Vivek Shah

import psutil
import time
from os import expanduser

home_path = expanduser("~")
log_file = home_path + "Documents/BatMan/battery_log.log"
with open(log_file,"a") as logfile:
    try:
        battery_status = psutil.sensors_battery()
        percentage = battery_status.percent
        secondsleft = battery_status.secsleft
        power_plugged = battery_status.power_plugged
        timestamp = time.localtime()
        s = time.strftime("%D %H:%M:%S",timestamp) + "," + str(percentage) + "," + str(secondsleft) + "," + str(power_plugged) + "\n"
        logfile.write(s)
    except Exception as exp:
        print(exp)
        exit()

## This code takes less than 0.1 second to run.
## So it will take less than 0.1 second of CPU time in One minute(3600 seconds)
## Stores the battery logs in battery_log.log file
