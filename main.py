"""
APT313 TOOLKIT (v2)
Coded by MR SILENT313 NASRU | TEAM APT 313

A legal, educational security toolkit for AUTHORIZED use only:
  - your own systems/networks, or
  - systems you have explicit written permission to test.

No exploit code, no malware, no brute-force attacks on live accounts.
Just encoding/hashing/password/passive-recon/text/CTF utilities that
any defender, student or CTF player should know how to use responsibly.

Runs on stock Python 3 standard library only (works in Pydroid3 too).
"""
import sys
import os
import time
import socket
import ssl
import hashlib
import hmac
import base64
import zlib
import random
import string
import re
import json
import csv
import io
import uuid
import difflib
import ipaddress
import datetime
import urllib.request
import urllib.error
import urllib.parse
G = '\x1b[92m'
R = '\x1b[91m'
C = '\x1b[96m'
Y = '\x1b[93m'
DIM = '\x1b[2m'
BOLD = '\x1b[1m'
RESET = '\x1b[0m'
BANNER = '\n         _______\n       /         \\\n      /  (o)  (o)  \\        APT 313 :: GHOST PROTOCOL\n     |       ^       |\n     |     \\___/     |       coded by MR SILENT313 NASRU\n      \\_____________/        team: TEAM APT 313\n      /  |  |  |  |  \\\n     ^   ^   ^   ^   ^        authorized use only. no exploits included.\n'
LEGAL = 'LEGAL NOTICE\nThis toolkit is for AUTHORIZED security testing and learning only:\n  - systems you own, or\n  - systems you have explicit written permission to test.\nRunning this against systems you do not own or lack permission for\nmay be illegal in your country. You are responsible for your own use.\n'

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_out(text, delay=0.01):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def ghost_entry():
    clear()
    frames = ['booting apt313 kernel', 'loading modules [##########] ok', 'checking authorization flag', 'spawning ghost shell']
    for f in frames:
        type_out(G + '> ' + f + RESET, 0.008)
        time.sleep(0.12)
    print(G + BANNER + RESET)
    print(Y + BOLD + LEGAL + RESET)
    ans = input(C + 'Type YES to confirm you are authorized to proceed: ' + RESET).strip().lower()
    if ans != 'yes':
        print(R + 'Access denied. Exiting.' + RESET)
        sys.exit(0)

def pause():
    input(DIM + '\n[enter to continue]' + RESET)

def confirm_authorized(target):
    a = input(Y + "Confirm you are authorized to test '%s'? (yes/no): " % target + RESET).strip().lower()
    return a == 'yes'

def a_base64():
    mode = input('1) Encode  2) Decode : ').strip()
    text = input('Text: ')
    try:
        if mode == '1':
            print(G + base64.b64encode(text.encode()).decode() + RESET)
        else:
            print(G + base64.b64decode(text.encode()).decode(errors='replace') + RESET)
    except Exception as e:
        print(R + 'Error: %s' % e + RESET)

def a_base32():
    mode = input('1) Encode  2) Decode : ').strip()
    text = input('Text: ')
    try:
        if mode == '1':
            print(G + base64.b32encode(text.encode()).decode() + RESET)
        else:
            print(G + base64.b32decode(text.encode()).decode(errors='replace') + RESET)
    except Exception as e:
        print(R + 'Error: %s' % e + RESET)

def a_base16():
    mode = input('1) Encode  2) Decode : ').strip()
    text = input('Text: ')
    try:
        if mode == '1':
            print(G + base64.b16encode(text.encode()).decode() + RESET)
        else:
            print(G + base64.b16decode(text.encode().upper()).decode(errors='replace') + RESET)
    except Exception as e:
        print(R + 'Error: %s' % e + RESET)

def a_base85():
    mode = input('1) Encode  2) Decode : ').strip()
    text = input('Text: ')
    try:
        if mode == '1':
            print(G + base64.b85encode(text.encode()).decode() + RESET)
        else:
            print(G + base64.b85decode(text.encode()).decode(errors='replace') + RESET)
    except Exception as e:
        print(R + 'Error: %s' % e + RESET)

def a_url():
    mode = input('1) Encode  2) Decode : ').strip()
    text = input('Text: ')
    if mode == '1':
        print(G + urllib.parse.quote(text) + RESET)
    else:
        print(G + urllib.parse.unquote(text) + RESET)

def a_html():
    import html
    mode = input('1) Encode  2) Decode : ').strip()
    text = input('Text: ')
    if mode == '1':
        print(G + html.escape(text) + RESET)
    else:
        print(G + html.unescape(text) + RESET)

def _caesar(text, shift):
    out = []
    for ch in text:
        if ch.isalpha():
            base = 65 if ch.isupper() else 97
            out.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            out.append(ch)
    return ''.join(out)

def a_caesar():
    mode = input('1) Encode  2) Decode : ').strip()
    text = input('Text: ')
    shift = int(input('Shift (0-25): ').strip() or '3')
    shift = shift if mode == '1' else -shift
    print(G + _caesar(text, shift) + RESET)

def a_rot13():
    text = input('Text: ')
    print(G + _caesar(text, 13) + RESET)

def a_rot47():
    text = input('Text: ')
    out = []
    for ch in text:
        o = ord(ch)
        out.append(chr(33 + (o - 33 + 47) % 94) if 33 <= o <= 126 else ch)
    print(G + ''.join(out) + RESET)

def a_vigenere():
    mode = input('1) Encode  2) Decode : ').strip()
    text = input('Text: ')
    key = input('Key: ').strip() or 'key'
    out = []
    ki = 0
    for ch in text:
        if ch.isalpha():
            base = 65 if ch.isupper() else 97
            k = ord(key[ki % len(key)].lower()) - 97
            k = k if mode == '1' else -k
            out.append(chr((ord(ch) - base + k) % 26 + base))
            ki += 1
        else:
            out.append(ch)
    print(G + ''.join(out) + RESET)

def a_xor():
    text = input('Text: ')
    key = input('Key: ').strip() or 'key'
    data = text.encode()
    kb = key.encode()
    result = bytes((data[i] ^ kb[i % len(kb)] for i in range(len(data))))
    print('Hex: ' + G + result.hex() + RESET)
    try:
        print('As text: ' + G + result.decode(errors='replace') + RESET)
    except Exception:
        pass
MORSE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}
MORSE_REV = {v: k for k, v in MORSE.items()}

def a_morse():
    mode = input('1) Encode  2) Decode : ').strip()
    if mode == '1':
        text = input('Text: ').upper()
        print(G + ' '.join((MORSE.get(c, '') for c in text if c != ' ')) + RESET)
    else:
        code = input('Morse (space-separated): ').strip()
        print(G + ''.join((MORSE_REV.get(tok, '') for tok in code.split())) + RESET)

def a_binary():
    mode = input('1) Text->Binary  2) Binary->Text : ').strip()
    if mode == '1':
        text = input('Text: ')
        print(G + ' '.join((format(b, '08b') for b in text.encode())) + RESET)
    else:
        b = input('Binary (space-separated bytes): ').strip()
        try:
            data = bytes((int(x, 2) for x in b.split()))
            print(G + data.decode(errors='replace') + RESET)
        except Exception as e:
            print(R + 'Error: %s' % e + RESET)

def a_hex_text():
    mode = input('1) Text->Hex  2) Hex->Text : ').strip()
    if mode == '1':
        text = input('Text: ')
        print(G + text.encode().hex() + RESET)
    else:
        h = input('Hex: ').strip()
        try:
            print(G + bytes.fromhex(h).decode(errors='replace') + RESET)
        except Exception as e:
            print(R + 'Error: %s' % e + RESET)

def a_decimal():
    mode = input('1) Text->Decimal  2) Decimal->Text : ').strip()
    if mode == '1':
        text = input('Text: ')
        print(G + ' '.join((str(ord(c)) for c in text)) + RESET)
    else:
        d = input('Decimal codes (space-separated): ').strip()
        try:
            print(G + ''.join((chr(int(x)) for x in d.split())) + RESET)
        except Exception as e:
            print(R + 'Error: %s' % e + RESET)

def a_atbash():
    text = input('Text: ')
    out = []
    for ch in text:
        if ch.isalpha():
            base = 65 if ch.isupper() else 97
            out.append(chr(base + (25 - (ord(ch) - base))))
        else:
            out.append(ch)
    print(G + ''.join(out) + RESET)

def _hash_text(algo):
    text = input('Text: ')
    print(G + hashlib.new(algo, text.encode()).hexdigest() + RESET)

def b_md5():
    _hash_text('md5')

def b_sha1():
    _hash_text('sha1')

def b_sha256():
    _hash_text('sha256')

def b_sha512():
    _hash_text('sha512')

def b_sha3_256():
    _hash_text('sha3_256')

def b_blake2b():
    _hash_text('blake2b')

def b_all_hashes():
    text = input('Text: ')
    for algo in ('md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512', 'sha3_256', 'sha3_512', 'blake2b', 'blake2s'):
        print('  %-10s %s%s%s' % (algo, G, hashlib.new(algo, text.encode()).hexdigest(), RESET))

def b_hmac():
    text = input('Message: ')
    key = input('Key: ')
    algo = input('Algorithm [sha256]: ').strip() or 'sha256'
    print(G + hmac.new(key.encode(), text.encode(), algo).hexdigest() + RESET)

def b_crc32():
    text = input('Text: ')
    print(G + format(zlib.crc32(text.encode()) & 4294967295, '08x') + RESET)

def b_identify():
    h = input('Paste hash: ').strip()
    length = len(h)
    guesses = {32: 'MD5 / NTLM', 40: 'SHA1', 56: 'SHA224', 64: 'SHA256 / SHA3-256', 96: 'SHA384', 128: 'SHA512 / SHA3-512'}
    print('Length %d -> likely: %s%s%s' % (length, G, guesses.get(length, 'Unknown'), RESET))

def b_file_hash():
    path = input('File path: ').strip()
    algo = input('Algorithm [sha256]: ').strip() or 'sha256'
    try:
        h = hashlib.new(algo)
        with open(path, 'rb') as f:
            for chunk in iter(lambda: f.read(65536), b''):
                h.update(chunk)
        print(G + h.hexdigest() + RESET)
    except Exception as e:
        print(R + 'Error: %s' % e + RESET)

def b_file_compare():
    p1 = input('File 1: ').strip()
    p2 = input('File 2: ').strip()
    try:

        def fh(p):
            h = hashlib.sha256()
            with open(p, 'rb') as f:
                for chunk in iter(lambda: f.read(65536), b''):
                    h.update(chunk)
            return h.hexdigest()
        h1, h2 = (fh(p1), fh(p2))
        same = h1 == h2
        print(('%sMATCH%s' if same else '%sDIFFERENT%s') % ((G, RESET) if same else (R, RESET)))
    except Exception as e:
        print(R + 'Error: %s' % e + RESET)

def c_strength():
    pwd = input('Password: ')
    score, notes = (0, [])
    if len(pwd) >= 12:
        score += 2
    elif len(pwd) >= 8:
        score += 1
    else:
        notes.append('too short (use 12+ chars)')
    if re.search('[a-z]', pwd):
        score += 1
    else:
        notes.append('add lowercase')
    if re.search('[A-Z]', pwd):
        score += 1
    else:
        notes.append('add uppercase')
    if re.search('\\d', pwd):
        score += 1
    else:
        notes.append('add numbers')
    if re.search('[^A-Za-z0-9]', pwd):
        score += 1
    else:
        notes.append('add special characters')
    if re.fullmatch('(.)\\1*', pwd or 'x'):
        score = 0
        notes.append('avoid repeated characters')
    levels = ['Very weak', 'Weak', 'Fair', 'Good', 'Strong', 'Very strong', 'Excellent']
    level = levels[min(score, len(levels) - 1)]
    color = R if score <= 2 else Y if score <= 4 else G
    print('Score %d/6 -> %s%s%s' % (score, color, level, RESET))
    for n in notes:
        print('  - ' + n)

def c_generator():
    length = int(input('Length [16]: ').strip() or '16')
    count = int(input('How many? [3]: ').strip() or '3')
    alphabet = string.ascii_letters + string.digits + '!@#$%^&*()-_=+'
    for _ in range(count):
        print(G + ''.join((random.SystemRandom().choice(alphabet) for _ in range(length))) + RESET)
WORDS = ['ghost', 'shadow', 'cipher', 'vector', 'nebula', 'falcon', 'ember', 'quartz', 'raven', 'nova', 'cobalt', 'lunar', 'ridge', 'ember', 'drift', 'onyx', 'silent', 'tango', 'zenith', 'crimson']

def c_passphrase():
    n = int(input('Number of words [4]: ').strip() or '4')
    words = [random.choice(WORDS).capitalize() for _ in range(n)]
    sep = input('Separator [-]: ').strip() or '-'
    print(G + sep.join(words) + str(random.randint(10, 99)) + RESET)

def c_pin():
    length = int(input('PIN length [6]: ').strip() or '6')
    print(G + ''.join((random.SystemRandom().choice(string.digits) for _ in range(length))) + RESET)

def c_entropy():
    pwd = input('Password: ')
    pool = 0
    if re.search('[a-z]', pwd):
        pool += 26
    if re.search('[A-Z]', pwd):
        pool += 26
    if re.search('\\d', pwd):
        pool += 10
    if re.search('[^A-Za-z0-9]', pwd):
        pool += 32
    import math
    bits = len(pwd) * math.log2(pool) if pool else 0
    print('Estimated entropy: %s%.1f bits%s' % (G, bits, RESET))
COMMON_PWDS = {'123456', 'password', '123456789', 'qwerty', 'abc123', '111111', '123123', 'admin', 'letmein', 'iloveyou', 'welcome', 'monkey'}

def c_common_check():
    pwd = input('Password: ')
    if pwd.lower() in COMMON_PWDS:
        print(R + 'This is a very common password. Do not use it.' + RESET)
    else:
        print(G + 'Not found in the small offline common-password list.' + RESET)

def c_hibp():
    """Checks a password against HaveIBeenPwned using k-anonymity:
    only the first 5 chars of the SHA1 hash are sent, never the password."""
    pwd = input('Password: ')
    sha1 = hashlib.sha1(pwd.encode()).hexdigest().upper()
    prefix, suffix = (sha1[:5], sha1[5:])
    try:
        req = urllib.request.Request('https://api.pwnedpasswords.com/range/' + prefix, headers={'User-Agent': 'apt313-toolkit'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            lines = resp.read().decode().splitlines()
        found = next((l for l in lines if l.split(':')[0] == suffix), None)
        if found:
            count = found.split(':')[1]
            print(R + 'Found in %s breach(es). Change this password.' % count + RESET)
        else:
            print(G + 'Not found in known breaches.' + RESET)
    except Exception as e:
        print(R + 'Lookup failed: %s' % e + RESET)

def c_bulk_gen():
    length = int(input('Length [16]: ').strip() or '16')
    count = int(input('How many? [10]: ').strip() or '10')
    alphabet = string.ascii_letters + string.digits + '!@#$%^&*()-_=+'
    pwds = [''.join((random.SystemRandom().choice(alphabet) for _ in range(length))) for _ in range(count)]
    path = input('Save to file [passwords.txt]: ').strip() or 'passwords.txt'
    try:
        with open(path, 'w') as f:
            f.write('\n'.join(pwds))
        print(G + 'Saved %d passwords to %s' % (count, path) + RESET)
    except Exception as e:
        print(R + 'Error: %s' % e + RESET)

def c_token():
    length = int(input('Token byte length [32]: ').strip() or '32')
    raw = os.urandom(length)
    print('Hex:    ' + G + raw.hex() + RESET)
    print('Base64: ' + G + base64.urlsafe_b64encode(raw).decode() + RESET)

def c_uuid():
    n = int(input('How many UUIDs? [1]: ').strip() or '1')
    for _ in range(n):
        print(G + str(uuid.uuid4()) + RESET)
COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3306, 3389, 8080, 8443]

def d_ip_info():
    target = input('IP or domain: ').strip()
    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(R + 'Could not resolve.' + RESET)
        return
    try:
        req = urllib.request.Request('https://ipinfo.io/%s/json' % ip, headers={'User-Agent': 'apt313-toolkit'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            info = json.loads(resp.read().decode())
        print('IP: ' + G + ip + RESET)
        for k in ('hostname', 'city', 'region', 'country', 'org'):
            if k in info:
                print('%-9s %s' % (k.capitalize(), info[k]))
    except Exception as e:
        print(R + 'Lookup failed: %s' % e + RESET)
SEC_HEADERS = ['Strict-Transport-Security', 'Content-Security-Policy', 'X-Frame-Options', 'X-Content-Type-Options', 'Referrer-Policy', 'Permissions-Policy']

def d_subnet_calc():
    cidr = input('CIDR (e.g. 192.168.1.0/24): ').strip()
    try:
        net = ipaddress.ip_network(cidr, strict=False)
        print('Network:    ' + G + str(net.network_address) + RESET)
        print('Broadcast:  ' + G + str(net.broadcast_address) + RESET)
        print('Netmask:    ' + G + str(net.netmask) + RESET)
        print('Hosts:      ' + G + str(net.num_addresses - 2 if net.num_addresses > 2 else net.num_addresses) + RESET)
    except Exception as e:
        print(R + 'Error: %s' % e + RESET)

def d_my_ip():
    try:
        with urllib.request.urlopen('https://api.ipify.org?format=json', timeout=8) as resp:
            print(G + json.loads(resp.read().decode())['ip'] + RESET)
    except Exception as e:
        print(R + 'Error: %s' % e + RESET)

def e_word_count():
    text = input('Text: ')
    words = text.split()
    print('Characters: %s%d%s' % (G, len(text), RESET))
    print('Words:      %s%d%s' % (G, len(words), RESET))
    print('Lines:      %s%d%s' % (G, len(text.splitlines()) or 1, RESET))

def e_case():
    text = input('Text: ')
    print('UPPER:      ' + G + text.upper() + RESET)
    print('lower:      ' + G + text.lower() + RESET)
    print('Title Case: ' + G + text.title() + RESET)
    print('sWaP cAsE:  ' + G + text.swapcase() + RESET)

def e_reverse():
    text = input('Text: ')
    print(G + text[::-1] + RESET)

def e_palindrome():
    text = re.sub('[^a-z0-9]', '', input('Text: ').lower())
    print(G + 'Palindrome!' + RESET if text == text[::-1] else R + 'Not a palindrome.' + RESET)

def e_anagram():
    a = re.sub('[^a-z0-9]', '', input('Word/phrase 1: ').lower())
    b = re.sub('[^a-z0-9]', '', input('Word/phrase 2: ').lower())
    print(G + 'Anagram!' + RESET if sorted(a) == sorted(b) else R + 'Not an anagram.' + RESET)

def e_json_tool():
    print('Paste JSON, empty line to finish:')
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    try:
        obj = json.loads('\n'.join(lines))
        print(G + json.dumps(obj, indent=2) + RESET)
    except Exception as e:
        print(R + 'Invalid JSON: %s' % e + RESET)
LOREM = 'Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam'.split()

def g_mac_gen():
    n = int(input('How many? [1]: ').strip() or '1')
    for _ in range(n):
        mac = [2, random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        print(G + ':'.join(('%02x' % b for b in mac)) + RESET)
MENU = [('ENCODING / CIPHERS', [('1', 'Base64 Encode/Decode', a_base64), ('2', 'Base32 Encode/Decode', a_base32), ('3', 'Base16 (Hex) Encode/Decode', a_base16), ('4', 'Base85 Encode/Decode', a_base85), ('5', 'URL Encode/Decode', a_url), ('6', 'HTML Entity Encode/Decode', a_html), ('7', 'Caesar Cipher Encode/Decode', a_caesar), ('8', 'ROT13', a_rot13), ('9', 'ROT47', a_rot47), ('10', 'Vigenere Cipher Encode/Decode', a_vigenere), ('11', 'XOR Cipher (key)', a_xor), ('12', 'Morse Code Encode/Decode', a_morse), ('13', 'Binary <-> Text', a_binary), ('14', 'Hex <-> Text', a_hex_text), ('15', 'Text <-> Decimal (ASCII codes)', a_decimal), ('16', 'Atbash Cipher', a_atbash)]), ('HASHING & INTEGRITY', [('17', 'MD5 Hash', b_md5), ('18', 'SHA1 Hash', b_sha1), ('19', 'SHA256 Hash', b_sha256), ('20', 'SHA512 Hash', b_sha512), ('21', 'SHA3-256 Hash', b_sha3_256), ('22', 'BLAKE2b Hash', b_blake2b), ('23', 'Hash With Every Algorithm', b_all_hashes), ('24', 'HMAC Generator', b_hmac), ('25', 'CRC32 Checksum', b_crc32), ('26', 'Hash Identifier', b_identify), ('27', 'File Hash Calculator', b_file_hash), ('28', 'File Integrity Compare', b_file_compare)]), ('PASSWORD & SECRETS', [('29', 'Password Strength Checker', c_strength), ('30', 'Password Generator', c_generator), ('31', 'Passphrase Generator', c_passphrase), ('32', 'PIN Generator', c_pin), ('33', 'Password Entropy Calculator', c_entropy), ('34', 'Common Password Checker (offline)', c_common_check), ('35', 'HaveIBeenPwned Breach Check', c_hibp), ('36', 'Bulk Password Generator (save to file)', c_bulk_gen), ('37', 'API Key / Token Generator', c_token), ('38', 'UUID Generator', c_uuid)]), ('NETWORK & PASSIVE RECON (authorized only)', [('42', 'IP / Domain Info (geolocation)', d_ip_info), ('53', 'Subnet / CIDR Calculator', d_subnet_calc), ('55', 'My Public IP', d_my_ip)]), ('TEXT & DATA UTILITIES', [('57', 'Word & Character Counter', e_word_count), ('58', 'Case Converter', e_case), ('59', 'Text Reverser', e_reverse), ('60', 'Palindrome Checker', e_palindrome), ('61', 'Anagram Checker', e_anagram), ('63', 'JSON Pretty Printer / Validator', e_json_tool)]), ('SYSTEM / MISC', [('76', 'Random MAC Address Generator', g_mac_gen)])]
FLAT = {key: (label, func) for _, items in MENU for key, label, func in items}

def print_menu():
    print('\n' + G + BOLD + '=== APT313 TOOLKIT ===' + RESET + '  ' + DIM + 'MR SILENT313 NASRU' + RESET)
    for category, items in MENU:
        print(Y + '\n-- %s --' % category + RESET)
        for key, label, _ in items:
            print('  %s[%s]%s %s' % (C, key, RESET, label))
    print(R + '\n  [0] Exit' + RESET)

def main_menu():
    while True:
        print_menu()
        choice = input('\n' + Y + 'apt313> ' + RESET).strip()
        if choice == '0':
            print(G + 'Stay ethical. Goodbye.' + RESET)
            break
        if choice not in FLAT:
            print(R + 'Unknown option.' + RESET)
            continue
        label, func = FLAT[choice]
        print(C + '\n--- %s ---' % label + RESET)
        try:
            func()
        except KeyboardInterrupt:
            print(R + '\nInterrupted.' + RESET)
        except Exception as e:
            print(R + 'Error: %s' % e + RESET)
        pause()
if __name__ == '__main__':
    try:
        ghost_entry()
        main_menu()
    except KeyboardInterrupt:
        print(R + '\nExiting.' + RESET)
