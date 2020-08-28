def fdistro():
    try:
        with open("/bedrock/etc/os-release", "rt") as distro:
            for line in distro:
                if "PRETTY_NAME" in line:
                    distro_name=line.split("=")[1].replace("\"", "")
                    return distro_name
                    

    except (FileNotFoundError, OSError):

        try:
            with open("/etc/os-release", "rt") as distro:
                for line in distro:
                    if "PRETTY_NAME" in line:
                        distro_name=line.split("=")[1].replace("\"", "")
                        return distro_name

        except (FileNotFoundError, OSError):

            try:
                with open("/etc/os-release", "rt") as distro:
                    for line in distro:
                        if "PRETTY_NAME" in line:
                            distro_name=line.split("=")[1].replace("\"", "")
                            return distro_name

            except (FileNotFoundError, OSError):
                from subprocess import check_output
                distro_name=check_output("uname -sr", shell=True).decode("utf-8")
                return distro_name

print(fdistro())












