import os
import platform
import utils.documentation_utils as doc_utils

Oper_system = platform.system()
oper_system = Oper_system.lower()


def splash_screen():
    """To print the splash screen"""
    print(r'''                                  
   ____                     _   _____                                       
  / __ \                   (_) / ____|                                      
 | |  | | _ __ ___   _ __   _ | (___    ___  __ _  _ __   _ __    ___  _ __ 
 | |  | || '_ ` _ \ | '_ \ | | \___ \  / __|/ _` || '_ \ | '_ \  / _ \| '__|
 | |__| || | | | | || | | || | ____) || (__| (_| || | | || | | ||  __/| |   
  \____/ |_| |_| |_||_| |_||_||_____/  \___|\__,_||_| |_||_| |_| \___||_|   

''')
    # print(f"## Welcome to Kartik's OmniScanner ({Oper_system} Version)")


def clear_screen():
    """Clearing the screen before running"""
    os.system('cls' if os.name == 'nt' else 'clear')


def documentation(i):
    """To print documentation from documentation_utils.
    :param : 0 for the main menu, 1 for level 1, 2 for level 2, 4 for level 4, p for ports
    :returns : Documentation as string"""

    if i == 0:
        return doc_utils.help0
    elif i == 1:
        return doc_utils.help1
    elif i == 2:
        return doc_utils.help2
    elif i == 4:
        return doc_utils.help4
    elif i == 'p':
        return doc_utils.ports
    else:
        return "Documentation not available"

print("Wrong file selected for running\nPlease run 'main.py' file by using 'python main.py' command")
