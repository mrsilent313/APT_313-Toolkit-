#!/usr/bin/env python3
"""
APT313 TOOLKIT
Coded by MR SILENT313 NASRU | TEAM APT 313

A legal, educational security toolkit for AUTHORIZED use only:
- your own systems/networks, or
- systems you have explicit written permission to test.

This toolkit contains no exploit code and does not attack anything on
its own. It only includes basic recon/utility functions that any
defender or student should know how to use responsibly.
"""

import sys
import os
import time
import socket
import hashlib
import base64
import random
import string
import re
import json
import urllib.request
import urllib.error

# ---------------------------------------------------------------------------
# THEME
# ---------------------------------------------------------------------------

G = "\033[92m"      # green
R = "\033[91m"       # red
C = "\033[96m"       # cyan
Y = "\033[93m"        # yellow
DIM = "\033[2m"
BOLD = "\033[1m"
RESET = "\033[0m"

BANNER = rf"""{G}
      .-' '-.
     /       \          {R}APT 313{G}
    |  .-. .-.  |       {C}GHOST PROTOCOL{G}
    |  | | | |  |
     \  '-' '-'  /       coded by {Y}MR SILENT313 NASRU{G}
      '--.U.--'          team: {Y}TEAM APT 313{G}
       /  |  \
      /   |   \          {DIM}authorized use only. no exploits included.{RESET}{G}
     '    |    '
{RESET}"""

LEGAL = f"""{Y}{BOLD}LEGAL NOTICE{RESET}
{DIM}This toolkit is for AUTHORIZED security testing and learning only:
  - systems you own, or
  - systems you have explicit written permission to test.
Running this against systems you do not own or lack permission for
may be illegal in your country. You are responsible for your own use.{RESET}
"""


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def type_out(text, delay=0.012):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def ghost_entry():
    clear()
    frames = [
        "booting apt313 kernel",
        "loading modules [##########] ok",
        "checking authorization flag",
        "spawning ghost shell",
    ]
    for f in frames:
        type_out(f"{G}> {f}{RESET}", 0.01)
        time.sleep(0.15)
    print(BANNER)
    print(LEGAL)
    ans = input(f"{C}Type YES to confirm you are authorized to proceed: {RESET}").strip().lower()
    if ans != "yes":
        print(f"{R}Access denied. Exiting.{RESET}")
        sys.exit(0)


# ---------------------------------------------------------------------------
# MODULES
# ---------------------------------------------------------------------------

def mod_port_scan():
    """Simple TCP connect scan against a host you are authorized to test."""
    print(f"\n{C}--- TCP Port Scanner (authorized targets only) ---{RESET}")
    host = input("Target host/IP: ").strip()
    rng = input("Port range (e.g. 1-1024) [default 1-1024]: ").strip() or "1-1024"
    try:
        start, end = (int(x) for x in rng.split("-"))
    except ValueError:
        print(f"{R}Invalid range.{RESET}")
        return
    confirm = input(f"{Y}Confirm you are authorized to scan {host}? (yes/no): {RESET}").strip().lower()
    if confirm != "yes":
        print(f"{R}Aborted.{RESET}")
        return

    print(f"{G}Scanning {host} ports {start}-{end}...{RESET}")
    try:
        target_ip = socket.gethostbyname(host)
    except socket.gaierror:
        print(f"{R}Could not resolve host.{RESET}")
        return

    open_ports = []
    for port in range(start, end + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.4)
        result = s.connect_ex((target_ip, port))
        if result == 0:
            try:
                service = socket.getservbyport(port)
            except OSError:
                service = "unknown"
            open_ports.append((port, service))
            print(f"  {G}[OPEN]{RESET} {port}/tcp  {DIM}{service}{RESET}")
        s.close()

    print(f"\n{C}Scan complete.{RESET} {len(open_ports)} open port(s) found.")


def mod_hash_id():
    """Identify a hash by its length/format and optionally generate hashes."""
    print(f"\n{C}--- Hash Identifier / Generator ---{RESET}")
    print("1) Identify a hash")
    print("2) Generate hash of text")
    choice = input("Choose [1/2]: ").strip()
    if choice == "1":
        h = input("Paste hash: ").strip()
        length = len(h)
        guesses = {
            32: "MD5 / NTLM",
            40: "SHA1",
            56: "SHA224",
            64: "SHA256",
            96: "SHA384",
            128: "SHA512",
        }
        guess = guesses.get(length, "Unknown / not a common hex hash length")
        print(f"Length: {length} -> likely: {G}{guess}{RESET}")
    elif choice == "2":
        text = input("Text to hash: ")
        for algo in ("md5", "sha1", "sha256", "sha512"):
            digest = hashlib.new(algo, text.encode()).hexdigest()
            print(f"  {algo.upper():<8} {G}{digest}{RESET}")
    else:
        print(f"{R}Invalid choice.{RESET}")


def mod_password_strength():
    """Check password strength with simple, transparent heuristics."""
    print(f"\n{C}--- Password Strength Checker ---{RESET}")
    pwd = input("Password to check: ")
    score = 0
    notes = []

    if len(pwd) >= 12:
        score += 2
    elif len(pwd) >= 8:
        score += 1
    else:
        notes.append("too short (use 12+ characters)")

    if re.search(r"[a-z]", pwd):
        score += 1
    else:
        notes.append("add lowercase letters")
    if re.search(r"[A-Z]", pwd):
        score += 1
    else:
        notes.append("add uppercase letters")
    if re.search(r"\d", pwd):
        score += 1
    else:
        notes.append("add numbers")
    if re.search(r"[^A-Za-z0-9]", pwd):
        score += 1
    else:
        notes.append("add special characters")
    if re.fullmatch(r"(.)\1*", pwd):
        score = 0
        notes.append("avoid repeated characters")

    levels = ["Very weak", "Weak", "Fair", "Good", "Strong", "Very strong", "Excellent"]
    level = levels[min(score, len(levels) - 1)]
    color = R if score <= 2 else (Y if score <= 4 else G)
    print(f"Score: {score}/6  ->  {color}{level}{RESET}")
    if notes:
        print("Suggestions:")
        for n in notes:
            print(f"  - {n}")


def mod_password_gen():
    """Generate strong random passwords."""
    print(f"\n{C}--- Password Generator ---{RESET}")
    try:
        length = int(input("Length [16]: ").strip() or "16")
    except ValueError:
        length = 16
    try:
        count = int(input("How many? [3]: ").strip() or "3")
    except ValueError:
        count = 3
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
    for _ in range(count):
        pwd = "".join(random.SystemRandom().choice(alphabet) for _ in range(length))
        print(f"  {G}{pwd}{RESET}")


def mod_base64():
    print(f"\n{C}--- Base64 Encode / Decode ---{RESET}")
    print("1) Encode  2) Decode")
    choice = input("Choose [1/2]: ").strip()
    text = input("Text: ")
    try:
        if choice == "1":
            print(G + base64.b64encode(text.encode()).decode() + RESET)
        elif choice == "2":
            print(G + base64.b64decode(text.encode()).decode(errors="replace") + RESET)
        else:
            print(f"{R}Invalid choice.{RESET}")
    except Exception as e:
        print(f"{R}Error: {e}{RESET}")


def mod_subdomains():
    """Passive subdomain lookup using the public crt.sh certificate transparency log.
    No active scanning of the target is performed here."""
    print(f"\n{C}--- Passive Subdomain Lookup (crt.sh) ---{RESET}")
    domain = input("Domain (e.g. example.com): ").strip()
    if not domain:
        return
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "apt313-toolkit"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode(errors="replace"))
    except Exception as e:
        print(f"{R}Lookup failed: {e}{RESET}")
        return

    found = set()
    for entry in data:
        name = entry.get("name_value", "")
        for line in name.split("\n"):
            line = line.strip().lstrip("*.")
            if line.endswith(domain):
                found.add(line)

    print(f"{G}{len(found)} unique subdomain(s) found:{RESET}")
    for s in sorted(found):
        print(f"  {s}")


def mod_ip_info():
    """Public IP geolocation/info via a free public API (passive, no scanning)."""
    print(f"\n{C}--- IP / Domain Info (passive) ---{RESET}")
    target = input("IP or domain: ").strip()
    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"{R}Could not resolve.{RESET}")
        return
    try:
        req = urllib.request.Request(f"https://ipinfo.io/{ip}/json", headers={"User-Agent": "apt313-toolkit"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            info = json.loads(resp.read().decode())
        print(f"IP:       {G}{ip}{RESET}")
        for k in ("hostname", "city", "region", "country", "org"):
            if k in info:
                print(f"{k.capitalize():<9} {info[k]}")
    except Exception as e:
        print(f"{R}Lookup failed: {e}{RESET}")


def mod_about():
    print(BANNER)
    print(LEGAL)


# ---------------------------------------------------------------------------
# MENU
# ---------------------------------------------------------------------------

MENU = [
    ("1", "TCP Port Scanner (authorized targets only)", mod_port_scan),
    ("2", "Hash Identifier / Generator", mod_hash_id),
    ("3", "Password Strength Checker", mod_password_strength),
    ("4", "Password Generator", mod_password_gen),
    ("5", "Base64 Encode / Decode", mod_base64),
    ("6", "Passive Subdomain Lookup (crt.sh)", mod_subdomains),
    ("7", "IP / Domain Info", mod_ip_info),
    ("8", "About / Legal", mod_about),
    ("0", "Exit", None),
]


def main_menu():
    while True:
        print(f"\n{G}{BOLD}=== APT313 TOOLKIT ==={RESET}  {DIM}MR SILENT313 NASRU{RESET}")
        for key, label, _ in MENU:
            print(f"  {C}[{key}]{RESET} {label}")
        choice = input(f"\n{Y}apt313>{RESET} ").strip()
        match = next((m for m in MENU if m[0] == choice), None)
        if not match:
            print(f"{R}Unknown option.{RESET}")
            continue
        key, label, func = match
        if key == "0":
            print(f"{G}Stay ethical. Goodbye.{RESET}")
            break
        try:
            func()
        except KeyboardInterrupt:
            print(f"\n{R}Interrupted.{RESET}")
        except Exception as e:
            print(f"{R}Error: {e}{RESET}")


if __name__ == "__main__":
    try:
        ghost_entry()
        main_menu()
    except KeyboardInterrupt:
        print(f"\n{R}Exiting.{RESET}")
