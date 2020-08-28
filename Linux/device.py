def fdevice():
    try:
        with open("/sys/devices/virtual/dmi/id/product_name", "rt") as device:
            return (device.readline())
    except FileNotFoundError:
         with open("/sys/firmware/devicetree/base/model", "rt") as device:
            return (device.readline())
