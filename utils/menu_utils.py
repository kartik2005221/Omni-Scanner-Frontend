import subprocess
import ipaddress
from utils.common_utils import oper_system
import threading
import time
import sys


# def run_command(command):
#     """Running commands, with subprocess
#     :param command: Command to run"""
#     print("\nExecuting: ", end="")
#     for i in command:
#         print(i, end=" ")
#     print()
#     subprocess.run(command)
#     input("Press Enter to continue...")

def run_command(interactive, command):
    """Running commands, with subprocess
    :param interactive: If True, run in interactive mode
    :param command: Command to run
    :returns: Output of the command if not interactive, else None"""
    if interactive:
        print(f"\nExecuting: {' '.join(command)}")
        return subprocess.run(command)
    else:
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout


def traceroute_all_os():
    """Just a Simple Traceroute Function
    :returns : 0"""
    if oper_system() == "Windows":
        subprocess.run(["tracert", input("Enter IP for traceroute : ")])
        input("Press Enter to continue...")
    else:
        subprocess.run(["traceroute", input("Enter IP for traceroute : ")])
    return 0


def validate_ip(ip):
    """To validate the IP address.
    Return True if valid, else False
    :param ip: IP address to validate
    :returns: True if valid, else False"""
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False


def validate_ip_range(ip_range):
    """To validate IP address range. Return True if valid, else False
    :param ip_range: IP address range to validate
    :returns: True if valid, else False"""
    try:
        if "-" in ip_range:
            # noinspection PyTupleAssignmentBalance
            base_ip, start, end = ip_range.rsplit(".", 1)[0], *ip_range.split("-")
            return validate_ip(start) and validate_ip(base_ip + "." + end) and (int(start.split(".")[-1]) <= int(end))
        else:
            return validate_ip(ip_range)
    except ValueError:
        return False


def spinning_cursor():
    """Generator for spinning cursor"""
    while True:
        for cursor in '|/-\\':
            yield cursor


def spinner_task(spinner_user):
    """Displays a spinner while the process is running"""
    spinner = spinning_cursor()
    while spinner_user.poll() is None:  # Keep running while a process is active
        sys.stdout.write(f"\rScanning network... {next(spinner)} ")
        sys.stdout.flush()
        time.sleep(0.2)  # Adjust the speed of the spinner
    # sys.stdout.write("\rScanning complete!     \n")


process = 0


def run_nmap_scan_big(ip_range):
    """Runs Nmap scan with progress indicator and graceful exit"""
    global process
    try:
        process = subprocess.Popen(["nmap", ip_range], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        # Start the spinner in a separate thread
        spinner_thread = threading.Thread(target=spinner_task, args=(process,), daemon=True)
        spinner_thread.start()
        # Wait for the Nmap process to complete
        stdout, stderr = process.communicate()
        # Print Nmap results
        print("\n \n", stdout)
        if stderr:
            print("\nErrors:\n", stderr)

        input("Press Enter to continue...")

    except KeyboardInterrupt:
        process.terminate()  # Kill Nmap process if the user presses Ctrl+C
        print("\n[Ctrl - C] Stopping...")


def run_nmap_scan_big_web(ip):
    command = ["nmap", ip]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

# def get_ip():
#     """Get the IP address of the current system"""
#     if oper_system() == "Windows":
#         subprocess.run(["ipconfig"])
#     else:
#         subprocess.run(["ip", "addr"])


# sample codes for reference
# result = subprocess.run(["arp-scan", "-l"], capture_output=True, text=True)
# print("Output:", result.stdout)
# print("Error:", result.stderr)
# print("Return Code:", result.returncode)
print("Wrong file selected for running\nPlease run 'main.py' file by using 'python main.py' command")
