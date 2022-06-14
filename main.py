
BANNER = """ ▄▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄▄▄▄▄ ▄▄    ▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄   
█       █  █ █  █  ▄    █  █  █ █       █       █       █   ▄  █  
█  ▄▄▄▄▄█  █ █  █ █▄█   █   █▄█ █    ▄▄▄█▄     ▄█   ▄   █  █ █ █  
█ █▄▄▄▄▄█  █▄█  █       █       █   █▄▄▄  █   █ █  █ █  █   █▄▄█▄ 
█▄▄▄▄▄  █       █  ▄   ██  ▄    █    ▄▄▄█ █   █ █  █▄█  █    ▄▄  █
 ▄▄▄▄▄█ █       █ █▄█   █ █ █   █   █▄▄▄  █   █ █       █   █  █ █
█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄█  █▄▄█▄▄▄▄▄▄▄█ █▄▄▄█ █▄▄▄▄▄▄▄█▄▄▄█  █▄█
"""


def shToDec(sh: int):
    if 0 <= sh <= 32:
        if sh % 8 == 0:
            return 255

        out = 0
        j = 128

        for i in range(sh % 8):
            out += j
            j //= 2
        return out
    else:
        return -1


def getSubnetByShorthand():
    sh = "bob"
    while sh[0] != '/' and 0 < len(sh) < 4:
        sh = input("Shorthand (/xy): ")
        try:
            sh = int(sh[1:])
            break
        except ValueError:
            print("Invalid shorthand. Stick to the format '/22' '/15' '/5' '/17', etc.")
            return

    if sh <= 8:
        prefix = ""
        suffix = ".0.0.0"
    elif sh <= 16:
        prefix = "255."
        suffix = ".0.0"
    elif sh <= 24:
        prefix = "255.255."
        suffix = ".0"
    else:
        prefix = "255.255.255."
        suffix = ""

    return prefix + str(shToDec(sh)) + suffix


def getSubnetByDecimals():
    decimals = input("Subnet mask (xyz.xyz.xyz.xyz): ")
    aces = decimals.count("255")

    if aces == 4:
        return "/32"

    dec = int(decimals.split('.')[aces])

    if dec < 128:
        return -1

    tmp = 128
    out = 0

    while dec != 0:
        dec -= tmp
        out += 1
        tmp //= 2

    return f"/{out}"


def getSubnetAll(addressRange):
    pass


def main():
    print(BANNER)

    while True:
        print("Pick an option:")
        print("[1] Subnet Mask corresponding to /xy")
        print("[2] Shorthand corresponding to xyz.xyz.xyz.xyz")
        print("[3] Hosts, Network, Broadcast of xyz.xyz.xyz.xyz/xy")
        print("[E] Exit.")

        option = input("Option: ")

        if option == "1":
            print(getSubnetByShorthand())
        elif option == "2":
            print(getSubnetByDecimals())
        elif option == "3":
            getSubnetAll()
        elif option == "E" or option == "e":
            break
        else:
            print("[FOOL!] Please choose a valid option.")

    print("Goodbye.")


if __name__ == "__main__":
    main()

