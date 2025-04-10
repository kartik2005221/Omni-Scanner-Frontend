import subprocess

from utils.common_utils import documentation
from utils.menu_utils import traceroute_all_os, validate_ip, validate_ip_range, run_nmap_scan_big, run_command


def arp_scan_windows():
    return "Sorry, This option is not available in your operating system"


def arp_scan_nmap_windows(ip, interactive=False):
    return run_command(interactive, ["nmap", "-sn", "-T5", "--min-parallelism", "100",
                                     "--host-timeout", "2000ms", ip])


def flood_ping_windows(ip, interactive=False):
    return "Sorry, Flood ping not possible in your operating system"


def level_1():
    """Menu Based : All IP Scanner"""
    while True:
        print("\nSelect a Option:\n\t1. Scan All IPs in your Network (High Speed, Less Detailed) (Sudo Required) "
              "(linux/macos only)\n\t2. Scan specific IPs (High Speed, Less Detailed)"
              "\n\t3. Scan specific IPs (Slow speed, More Detailed)\n\tH. Help\n\t0. Previous Menu")
        input2 = input("::: ").lower() or '0'
        if input2 == 'h':
            print(documentation(1))
            input("Enter to go back to menu...")
        elif input2 == '0':
            return 0
        elif input2 == '1':
            print(arp_scan_windows())
        elif input2 in ['2', '3']:
            ip_addr = input("Enter range of IPs (eg. 192.168.1.1-255)\n::: ") or "127.0.0.1"
            if validate_ip_range(ip_addr):
                if input2 == '2':
                    arp_scan_nmap_windows(ip_addr, interactive=True)

                elif input2 == '3':
                    # try:
                    #     subprocess.run(["nmap", ip_addr])
                    #     input ("Press Enter to continue...")
                    # except KeyboardInterrupt:
                    #     print("\n(Ctrl-C) Exiting...\n\t[Try Fast Scan with option 1,
                    #     if user does not have enough time]")
                    run_nmap_scan_big(ip_addr)
            else:
                print("Invalid IP range entered, Please Try again")
        else:
            print("Unsupported Option selected, Please Try again")


def level_2():
    """Menu Based : Ping option's function"""
    while True:
        print("\nSelect a Option:\n\t1. Simple ping\n\t2. Large Ping\n\t3. Ping for slow network"
              "\n\t4. Flood Ping (requires sudo)(available only in linux/mac)\n\tH. Help\n\t0. Previous Menu")
        input2 = input("::: ").lower() or '0'
        if input2 == 'h':
            print(documentation(2))
            input("Enter to go back to menu...")
        elif input2 == '0':
            return 0
        elif input2 in ['1', '2', '3']:
            try:
                ip_addr = input("Enter IP to ping (eg 192.168.1.1)\n::: ") or "127.0.0.1"
                if validate_ip(ip_addr):
                    ping_type = input("Ping finitely or infinitely? (1/2)\n::: ") or '1'
                    if ping_type == '1':
                        no_of_packets = input("Enter number of packets to send\n::: ") or '5'
                        ping_count = f"-n {no_of_packets}"
                    else:
                        ping_count = "-t"

                    if input2 == '1':
                        subprocess.run(["ping", ping_count, ip_addr])

                    elif input2 == '2':
                        subprocess.run(
                            ["ping", ping_count, "-l", input("Enter size of packet to send (0-65500)"), ip_addr])

                    elif input2 == '3':
                        subprocess.run(
                            ["ping", ping_count, "-w", str(int(input("How much time (sec.) to wait?\n::: ")) * 1000),
                             ip_addr])

                else:
                    print("Invalid IP entered, Please Try again")
            except KeyboardInterrupt:
                print("[Ctrl-C] Stopping...")
                try:
                    if input("Press Enter to continue..."):
                        return 0
                except KeyboardInterrupt:
                    return 0
        elif input2 == '4':
            print(flood_ping_windows(2, interactive=True))
        else:
            print("Unsupported Option selected, Please Try again")


def level_4():
    """Menu based : All Nmap option's function"""
    while True:
        print("\nSelect Required option: (separated by spaces)"
              "\n\t1. Simple Nmap (Fast)(Dont use it with any other argument)\n\t2. Detect OS\n\t"
              "3. Detect running service & its version"
              " from open ports\n\t4. SYN Scan\n\t5. UDP Scan\n\t6. Specific Port scan \n\t"
              "7. All Port scan(6 or 7, not both)\n\t8. Aggressive Scan (Slower)"
              "\n\tP. Top 50  network ports used.\n\tH. Help\n\t0. Previous Menu")
        input2 = input("::: ").lower() or '0'
        input2 = input2.split()

        if 'h' in input2:
            print(documentation(4))
            input("Enter to go back to menu...")
        elif input2 == '0':
            return 0
        elif input2 == 'p':
            print(documentation('p'))
            input("Enter to go back to menu...")
        # elif input2 in ['1', '2', '3', '4', '5', '6', '7', '8']:
        elif all(x in ['1', '2', '3', '4', '5', '6', '7', '8'] for x in input2):
            ip_addr = input("Enter IP to scan(eg - 192.168.1.1)\n::: ") or "127.0.0.1"
            if validate_ip(ip_addr):
                if '1' in input2:
                    subprocess.run(["nmap", ip_addr])

                else:
                    new_input2 = input2.split("")
                    # print(new_input2)
                    list_of_commands = ['nmap']

                    if '2' in new_input2:
                        list_of_commands.append("-O")

                    if '3' in new_input2:
                        list_of_commands.append("-sV")

                    if '4' in new_input2:
                        list_of_commands.append("-sS")

                    if '5' in new_input2:
                        list_of_commands.append("-sU")

                    if '7' in new_input2:
                        list_of_commands.append("-p-")
                    elif '6' in new_input2:
                        list_of_ports = input("Enter port range (Eg. 1-65535) : ") or '1-65535'
                        list_of_commands.append("-p")
                        list_of_commands.append(list_of_ports)

                    if '8' in new_input2:
                        list_of_commands.append("-A")

                    list_of_commands.append(ip_addr)
                    print(list_of_commands)
                    subprocess.run(list_of_commands)

            else:
                print("Invalid IP entered, Please Try again")
        else:
            print("Unsupported Option selected, Please Try again")


def menu_windows():
    """Function for Initial Menu to show in front of the user"""
    # check_and_run_admin_windows()
    while True:
        print(r"""
(Windows Version)
Select a Option :
    1. Scanning full network, Finding Specific Target
    2. Pinging(Custom) a Specific IP
    3. TraceRouting
    4. Advance Scanning a Specific IP
    5. Get network information
    H. Help
    0. Exit""")
        input1 = input("::: ").lower() or '0'

        if input1 == 'h':
            print(documentation(0))
            input("Enter to go back to menu...")
        elif input1 == '0':
            return 0
        elif input1 == '1':
            level_1()
        elif input1 == '2':
            level_2()
        elif input1 == '3':
            traceroute_all_os()
        elif input1 == '4':
            level_4()
        elif input1 == '5':
            subprocess.run(["ipconfig"])

        else:
            print("Unsupported Option selected, Please Try again")


print("Wrong file selected for running\nPlease run 'main.py' file by using 'python main.py' command")
