def fprocessor():
    with open("/proc/cpuinfo", "rt") as cpuinfo:
        for caracteristic in cpuinfo:
            if "model name" in caracteristic:
                CPU = caracteristic.split(":")[1][1:]
                return CPU

    return -1
