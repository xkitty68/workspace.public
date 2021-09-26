bimport glob
import os.path
import subprocess

max_cpu_clk         = 1500000
min_cpu_clk         = 1000000
max_cpu_tmp         = 50
cpu_clk_down_step   = 200000
cpu_clk_up_step     = 100000

class cputemp:
    hwmon_rootpath = '/sys/class/hwmon/'

    curtemp = None
    sensorpath = None

    def find_coretemp_sensor(self):
        hwmonlist = glob.glob( self.hwmon_rootpath + '*')
        for hm in hwmonlist:
            fn = open(hm+'/name', 'r')
            name = fn.readline().strip()
            fn.close()
            if name == 'coretemp':
                return(hm)
        return(None)

    def __init__(self):
        self.ctpath = self.find_coretemp_sensor()

    def getSensorpath(self):
        pass

    def getTemp(self):
        if self.sensorpath == None:
            return(None)

class cpuclkctl:
    rootpath = '/sys/devices/system/cpu/cpufreq/policy0/'


    def __init__(self):
        pass

    def get_cpu_clk_param(self):
        pass

    def current_cpu_clk(self):
        pass

    def set_max_cpu_clk(self):
        pass

    def set_max_cpu_clk_down(self):
        pass

    def set_max_cpu_clk_up(self):
        pass


def main():
    if current_cpu_clk() > max_cpu_clk:
        set_max_cpu_clk()

    if current_cpu_clk >= min_cpu_clk:
        if current_cpu_tmp() > max_cpu_tmp:
            set_max_cpu_clk_down()
        elif current_cpu_tmp() < max_cpu_tmp:
            set_max_cpu_clk_up()

    