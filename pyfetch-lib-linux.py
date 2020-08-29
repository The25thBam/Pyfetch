'''This module is dedicated to fetch system data from Linux systems'''
from subprocess import check_output

def fcpu():
    '''Parses /proc/cpuinfo to get the CPU name'''
    # Opens /proc/cpuinfo
    with open("/proc/cpuinfo", "rt") as cpuinfo:
        # Browses through the lines of /proc/cpuinfo
        for parameter in cpuinfo:
            # Checks if the current line has the "model name" parameter
            if "model name" in parameter:
                # Parses the CPUs name from the "model name" parameter
                cpu = parameter.split(":")[1][1:]
                return cpu
    return -1

def fdevice():
    '''Returns the device name of the system'''
    # Tries to open /sys/devices/virtual/dmi/id/product_name and returns the device name from it
    try:
        with open("/sys/devices/virtual/dmi/id/product_name", "rt") as device:
            return device.readline()
    # If the previous file is not found or is not readable it will try to do the same with:
    # /sys/firmware/devicetree/base/model/
    except (FileNotFoundError, OSError):
        with open("/sys/firmware/devicetree/base/model", "rt") as device:
            return device.readline()

def parse_distro(file):
    '''Returns the name of a distro from the inputed file as long as it is an os-release file'''
    # Opens the giveny file
    with open(file, "rt") as distribution:
        # Browse the file line by line
        for line in distribution:
            # If the line is the one that has the pretty name of the distro returns it
            if "PRETTY_NAME" in line:
                # Parses the distro name
                distro_name = line.split("=")[1].replace("\"", "")
                return distro_name
    return -1

def fdistro():
    '''returns the distro the system is using'''
    # Tries to check distro from /bedrock/etc/os-release
    try:
        distro = parse_distro("/bedrock/etc/os-release")
        return distro
    # If the previous file was not found or unreadable
    except (FileNotFoundError, OSError):
        # Tries to check distro from /etc/os-release
        try:
            distro = parse_distro("/etc/os-release")
            return distro
        # If the previous file was not found or unreadable
        except (FileNotFoundError, OSError):
            # Tries to check distro from /usr/lib/os-release
            try:
                distro = parse_distro("/usr/lib/os-release")
                return distro
            # If the previous file was not found or unreadable
            except (FileNotFoundError, OSError):
            # extracts generic build name from the system command "uname -sr"
                distro_name = check_output("uname -sr", shell=True).decode("utf-8")
                return distro_name

    return -1
