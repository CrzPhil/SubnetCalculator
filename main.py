
BANNER = """ ▄▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄▄▄▄▄ ▄▄    ▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄   
█       █  █ █  █  ▄    █  █  █ █       █       █       █   ▄  █  
█  ▄▄▄▄▄█  █ █  █ █▄█   █   █▄█ █    ▄▄▄█▄     ▄█   ▄   █  █ █ █  
█ █▄▄▄▄▄█  █▄█  █       █       █   █▄▄▄  █   █ █  █ █  █   █▄▄█▄ 
█▄▄▄▄▄  █       █  ▄   ██  ▄    █    ▄▄▄█ █   █ █  █▄█  █    ▄▄  █
 ▄▄▄▄▄█ █       █ █▄█   █ █ █   █   █▄▄▄  █   █ █       █   █  █ █
█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄█  █▄▄█▄▄▄▄▄▄▄█ █▄▄▄█ █▄▄▄▄▄▄▄█▄▄▄█  █▄█
"""


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
    pass


def getSubnetByDecimals(decimals):
    pass


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
            getSubnetByShorthand()
        elif option == "2":
            getSubnetByDecimals()
        elif option == "3":
            getSubnetAll()
        elif option == "E" or option == "e":
            break
        else:
            print("[FOOL!] Please choose a valid option.")

    print("Goodbye.")


if __name__ == "__main__":
    main()

