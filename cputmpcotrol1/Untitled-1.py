#! /usr/bin/python3
# miu
temp_center = 60
temp_upp    = 1
temp_downp  = 2
cpu_upclk   = 100
cpu_downclk = 200

sysfscpu = '/sys/devices/system/cpu'
sysfshwmon = '/sys/class/hwmon'
cpupower_cmd = 'cpupower'

intervalsec = 10

import commands
import process
import time
import glob

class cpupower {
    def __self__():
        pass

    def setclkhz(n):
        pass
    def setclkmhz(n)
        self.setclkhz(n*1000*1000)

    def getclkhz():
        pass
    def getclkmhz():
        n = set.getclkhz() * 1000*1000

class hwmon:
    def __self__():
        pass

    def getdegc()
        pass


def find_cpu_package_temp_path(
    # name == 'coretemp'
    # label == 'Package id 0'
    # tmp = ./imput
)



# control loop
while 1:
    # down clk control
    if getdecg > temp_center+temp_upp:
        pass
    
    #up clk control
    if getdecg < temp_center-temp_downp:
        pass
    time.sleep(intervalsec)
