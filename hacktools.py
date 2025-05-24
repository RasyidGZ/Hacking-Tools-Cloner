import os
import subprocess
import time
from colorama import init, Fore, Back, Style

# Initialize colorama
init(autoreset=True)

# Color scheme
COLOR_TITLE = Fore.CYAN + Style.BRIGHT
COLOR_HEADER = Fore.YELLOW + Style.BRIGHT
COLOR_SUCCESS = Fore.GREEN
COLOR_WARNING = Fore.YELLOW
COLOR_ERROR = Fore.RED
COLOR_PROGRESS = Fore.BLUE
COLOR_REPO = Fore.MAGENTA
COLOR_CATEGORY = Fore.CYAN
COLOR_AUTHOR = Fore.LIGHTRED_EX
COLOR_INFO = Fore.LIGHTYELLOW + Style.UNDERLINE

def print_banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(COLOR_TITLE + r"""
  ____ _ _   _   _       _          _____ _                 _       _             
 / ___(_) |_| | | |_   _| |__      |_   _| |__   ___   ___ | | ___ | |_ ___  _ __ 
| |  _| | __| |_| | | | | '_ \ _____| | | '_ \ / _ \ / _ \| |/ _ \| __/ _ \| '__|
| |_| | | |_|  _  | |_| | | | |_____| | | | | | (_) | (_) | | (_) | || (_) | |   
 \____|_|\__|_| |_|\__,_|_| |_|     |_| |_| |_|\___/ \___/|_|\___/ \__\___/|_|   
    """)
    print(COLOR_INFO + "ini akan mengclone semua tools")
    print(COLOR_HEADER + "untuk fitur lengkap sebaiknya gunakan proot Ubuntu.")
    print(COLOR_AUTHOR + "Created by: @RasyidGZ")
    print(Style.RESET_ALL + "="*60 + "\n")

def clone_repos():
    # Repository list - add more as needed
    repos = [
        ("Metasploit Framework", "https://github.com/rapid7/metasploit-framework", "Exploitation"),
        ("Nmap", "https://github.com/nmap/nmap", "Reconnaissance"),
        ("Sqlmap", "https://github.com/sqlmapproject/sqlmap", "Database Exploitation"),
        ("Hydra", "https://github.com/vanhauser-thc/thc-hydra", "Password Cracking"),
        ("John the Ripper", "https://github.com/openwall/john", "Password Cracking"),
        ("Hashcat", "https://github.com/hashcat/hashcat", "Password Cracking"),
        ("Aircrack-ng", "https://github.com/aircrack-ng/aircrack-ng", "Wireless Testing"),
        ("Wireshark", "https://github.com/wireshark/wireshark", "Network Analysis"),
        ("Impacket", "https://github.com/fortra/impacket", "Network Exploitation"),
        ("Responder", "https://github.com/lgandx/Responder", "Network Exploitation"),
        ("CrackMapExec", "https://github.com/byt3bl33d3r/CrackMapExec", "Post-Exploitation"),
        ("BloodHound", "https://github.com/BloodHoundAD/BloodHound", "Active Directory"),
        ("Sn1per", "https://github.com/1N3/Sn1per", "Automated Scanning"),
        ("LinPEAS/WinPEAS", "https://github.com/carlospolop/PEASS-ng", "Privilege Escalation"),
        ("SecLists", "https://github.com/danielmiessler/SecLists", "Wordlists"),
        ("ExploitDB", "https://github.com/offensive-security/exploitdb", "Exploit Collection"),
        # DDOS Tools
        ("Slowloris", "https://github.com/gkbrk/slowloris", "DDOS Attack"),
        ("LOIC", "https://github.com/NewEraCracker/LOIC", "DDOS Attack"),
        ("HOIC", "https://github.com/MatrixTM/HOIC", "DDOS Attack"),
        ("GoldenEye", "https://github.com/jseidl/GoldenEye", "DDOS Attack"),
        ("DDOS-Ripper", "https://github.com/palahsu/DDoS-Ripper", "DDOS Attack"),
        ("UFONet", "https://github.com/epsylon/ufonet", "DDOS Attack"),
    ]

    target_dir = os.path.expanduser("~/hacking_tools")
    os.makedirs(target_dir, exist_ok=True)

    print(COLOR_HEADER + f"\n[+] Target Directory: {target_dir}")
    print(COLOR_HEADER + f"[+] Total Repositories: {len(repos)}")
    print("\n" + "="*60 + "\n")

    success_count = 0
    skip_count = 0
    fail_count = 0

    for i, (name, url, category) in enumerate(repos, 1):
        print(COLOR_REPO + f"\n[{i}/{len(repos)}] {name}")
        print(COLOR_CATEGORY + f"Category: {category}")
        print(Fore.WHITE + f"URL: {url}")
        
        repo_dir = os.path.join(target_dir, name)
        
        # Progress animation
        print(COLOR_PROGRESS + "Status: ", end='', flush=True)
        
        if os.path.exists(repo_dir):
            print(COLOR_WARNING + "Already exists, skipping...")
            skip_count += 1
            continue
        
        try:
            # Show progress spinner during clone
            spinner = ['|', '/', '-', '\\']
            p = subprocess.Popen(["git", "clone", url, repo_dir], 
                                stdout=subprocess.PIPE, 
                                stderr=subprocess.PIPE)
            
            # Animate while process runs
            while p.poll() is None:
                for char in spinner:
                    print(COLOR_PROGRESS + f"\rStatus: Cloning {char}", end='', flush=True)
                    time.sleep(0.1)
            
            # Check result
            if p.returncode == 0:
                print(COLOR_SUCCESS + "\rStatus: Successfully cloned!          ")
                success_count += 1
            else:
                error = p.stderr.read().decode().strip()
                print(COLOR_ERROR + f"\rStatus: Failed! {error}")
                fail_count += 1
                
        except Exception as e:
            print(COLOR_ERROR + f"\rStatus: Error! {str(e)}")
            fail_count += 1

    # Summary
    print("\n" + "="*60)
    print(COLOR_HEADER + "\n[+] Clone Summary:")
    print(COLOR_SUCCESS + f"Success: {success_count}")
    print(COLOR_WARNING + f"Skipped: {skip_count}")
    print(COLOR_ERROR + f"Failed: {fail_count}")
    print(COLOR_HEADER + f"\nTotal repositories: {len(repos)}")
    print("\n" + "="*60)
    print(COLOR_AUTHOR + "Author: @RasyidGZ")
    print(COLOR_SUCCESS + "\nDone! All repositories processed.\n")

if __name__ == "__main__":
    print_banner()
    
    # Check if git is installed
    try:
        subprocess.run(["git", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except:
        print(COLOR_ERROR + "[!] Git is not installed. Please install git first:")
        print(Fore.WHITE + "Run: pkg install git")
        exit(1)
    
    # Start cloning
    input(COLOR_HEADER + "\nPress Enter to start cloning..." + Style.RESET_ALL)
    clone_repos()