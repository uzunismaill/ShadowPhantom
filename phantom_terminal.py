import os
import sys
import time
import random
import threading
from datetime import datetime

# ANSI Color Codes
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    GREY = '\033[90m'
    WHITE = '\033[97m'

# Enable ANSI escape codes in Windows CMD
from ctypes import windll, byref, Structure, c_short, c_ushort, c_long
try:
    kernel32 = windll.kernel32
    handle = kernel32.GetStdHandle(-11)
    mode = c_long()
    kernel32.GetConsoleMode(handle, byref(mode))
    # ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004
    mode.value |= 0x0004
    kernel32.SetConsoleMode(handle, mode)
except:
    pass

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_print(text, delay=0.03, color=Colors.GREEN):
    for char in text:
        sys.stdout.write(color + char + Colors.ENDC)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_logo():
    logo = f"""
{Colors.GREEN}{Colors.BOLD}
   _____ _    _          _____  ________          __
  / ____| |  | |   /\   |  __ \|  ____\ \        / /
 | (___ | |__| |  /  \  | |  | | |__   \ \  /\  / / 
  \___ \|  __  | / /\ \ | |  | |  __|   \ \/  \/ /  
  ____) | |  | |/ ____ \| |__| | |____   \  /\  /   
 |_____/|_|  |_/_/    \_\_____/|______|   \/  \/    
                                                    
{Colors.WHITE} P H A N T O M   A C C E S S   T E R M I N A L
{Colors.ENDC}
"""
    print(logo)

def boot_sequence():
    lines = [
        ("Initializing ShadowPhantom Kernel...", 0.05),
        ("Loading modules: [====================] 100%", 0.02),
        (" > crypto_module... OK", 0.05),
        (" > network_sniffer... OK", 0.05),
        (" > brute_force_kit... OK", 0.05),
        ("Establishing secure connection to server...", 0.05),
        (" ...", 0.5),
        ("Connection established (latency: 12ms)", 0.05),
        ("User identity: SHADOW_PHANTOM", 0.05),
        (f"{Colors.FAIL}Access Level: GOD_MODE{Colors.GREEN}", 0.1),
        (f"{Colors.WHITE}Welcome back, Sir.{Colors.GREEN}", 0.1)
    ]
    
    for line, speed in lines:
        if "..." in line and len(line) < 5:
            time.sleep(speed)
            continue
        type_print(f"[{datetime.now().strftime('%H:%M:%S')}] {line}", delay=speed/2)
        time.sleep(0.1)

def draw_bar_chart(value, max_val=20, label=""):
    filled = int((value / 100) * max_val)
    bar = "█" * filled + "░" * (max_val - filled)
    return f"{label:<15} [{bar}] {value}%"

def radar_animation():
    chars = ["|", "/", "-", "\\"]
    return chars[int(time.time() * 4) % 4]

def main_interface():
    try:
        while True:
            # Move cursor to top left (using ANSI) without clearing to reduce flicker, 
            # or just clear screen fast. Clearing is easier for now but flickering.
            # A better way is to print updates at specific positions, but let's stick to clear for simplicity 
            # or just append if it's a log. 
            # The user wants "Hacker Style", which usually means static UI + updating numbers.
            
            # Let's try to simulate a static dashboard by re-printing everything
            # To avoid flicker, we build a single string and print it.
            
            now = datetime.now()
            time_str = now.strftime("%H:%M:%S")
            
            # Simulated Data
            cpu_usage = random.randint(10, 40)
            mem_usage = random.randint(20, 60)
            net_activity = random.randint(10, 90)
            
            buffer = ""
            buffer += f"{Colors.GREEN}{Colors.BOLD}"
            buffer += f"SHADOW PHANTOM SYSTEM v2.0                          SYSTEM: {Colors.WHITE}ONLINE{Colors.GREEN}\n"
            buffer += f"User: root                                          Time: {time_str}\n"
            buffer += f"{Colors.GREY}" + "-"*80 + f"{Colors.GREEN}\n"
            
            # Dashboard
            buffer += f"\n{Colors.CYAN}[ SYSTEM STATUS ]{Colors.GREEN}\n"
            buffer += f"{draw_bar_chart(cpu_usage, label='CPU Load')}\n"
            buffer += f"{draw_bar_chart(mem_usage, label='Memory')}\n"
            buffer += f"{draw_bar_chart(net_activity, label='Network Traffic')}\n"
            
            buffer += f"\n{Colors.CYAN}[ TARGET ANALYSIS ]{Colors.GREEN}\n"
            buffer += f"Scanning Area... {radar_animation()}\n"
            
            # Simulated Targets
            targets = [
                "EE:AA:55:12:34:56 (Weak WEP)",
                "A0:B1:C2:D3:E4:F5 (WPA2)",
                "11:22:33:44:55:66 (Open)"
            ]
            
            buffer += f"Detected Targets:\n"
            for t in targets:
                # Randomly highlight one
                if random.random() > 0.7:
                    buffer += f" > {Colors.FAIL}{t}{Colors.GREEN}\n"
                else:
                    buffer += f" > {t}\n"

            buffer += "\n" + f"{Colors.GREY}" + "-"*80 + f"{Colors.ENDC}\n"
            buffer += f"{Colors.WHITE}Press Ctrl+C to exit.{Colors.ENDC}"

            # Clear and print
            # \033[H moves cursor to home
            sys.stdout.write('\033[H' + buffer)
            sys.stdout.flush()
            
            time.sleep(0.5)
            
    except KeyboardInterrupt:
        print(f"\n{Colors.FAIL}System Shutdown Initiated...{Colors.ENDC}")

if __name__ == "__main__":
    clear_screen()
    print_logo()
    time.sleep(1)
    boot_sequence()
    time.sleep(1)
    clear_screen()
    main_interface()
