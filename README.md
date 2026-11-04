# APT_313-Toolkit-
JUST FOR FUN AND EDUCATIONAL PURPOSES ONLY.

<div align="center">

# APT313 TOOLKIT

**A legal, educational security toolkit with 78 modules for ethical hackers, students, and CTF players.**

Coded by **MR SILENT313 NASRU** · Team **APT 313**

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-brightgreen)
![Platform](https://img.shields.io/badge/platform-cross--platform-lightgrey)

</div>

---

## ⚠️ Legal Notice

This toolkit is for **authorized security testing and learning only**:

- systems you own, **or**
- systems you have **explicit written permission** to test.

Running this against systems you do not own or do not have permission for may be illegal in your country. **You are responsible for your own use.** This project contains no exploit code, no malware, and no tools for brute-forcing live accounts.

---

## About

**APT313 Toolkit** is a single-file, menu-driven command-line toolkit built for ethical hackers, red teamers, security students, and CTF players. It bundles 78 small, focused modules covering encoding, hashing, password security, passive reconnaissance, text utilities, and CTF helpers — all built on the Python standard library, so there's nothing extra to install.

The toolkit opens with a themed boot sequence and requires explicit confirmation before use, keeping authorized use front and center every time it runs.

## Features

- 🔐 **78 modules** across 7 categories
- 📦 **Zero dependencies** — pure Python standard library
- 📱 **Cross-platform** — runs on Linux, macOS, Windows, and Android (via Pydroid3)
- 🛡️ **Authorization prompts** before any active network action (port scans, banner grabs)
- 🎨 Themed CLI with a boot sequence, ASCII banner, and color output

## Module Categories

| Category | Modules | Examples |
|---|---|---|
| Encoding / Ciphers | 16 | Base64/32/16/85, URL, HTML, Caesar, Vigenère, XOR, Morse, Atbash |
| Hashing & Integrity | 12 | MD5, SHA-family, SHA3, BLAKE2, HMAC, CRC32, file hashing |
| Password & Secrets | 10 | Strength checker, generator, passphrase, HaveIBeenPwned check, UUID |
| Network & Passive Recon | 18 | Port scanner, DNS lookups, WHOIS, subdomain enum, SSL info, security headers |
| Text & Data Utilities | 14 | Word count, JSON/CSV tools, regex tester, diff, timestamp converter |
| CTF / Crypto Helpers | 5 | Caesar brute force, XOR brute force, frequency analysis, base converter |
| System / Misc | 3 | MAC generator, directory tree, about/legal |

See [`MODULES.md`](MODULES.md) for the full numbered list, or just run the toolkit — every module is listed in-app.

## Installation

```bash
git clone https://github.com/<your-username>/apt313-toolkit.git
cd apt313-toolkit
python3 apt313_toolkit.py
```

No `pip install` required — everything runs on Python 3.8+ standard library.

### Running on Android (Pydroid 3)

1. Install [Pydroid 3](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3) from the Play Store.
2. Copy `apt313_toolkit.py` to your device.
3. Open it in Pydroid 3 and tap **Run**.

## Usage

On launch, the toolkit shows a boot sequence and asks you to confirm you're authorized to proceed:

```
> booting apt313 kernel
> loading modules [##########] ok
> checking authorization flag
> spawning ghost shell

Type YES to confirm you are authorized to proceed:
```

Once inside, pick a module by number from the categorized menu:

```
=== APT313 TOOLKIT ===  MR SILENT313 NASRU

-- ENCODING / CIPHERS --
  [1] Base64 Encode/Decode
  [2] Base32 Encode/Decode
  ...

apt313>
```

Active network modules (port scanner, banner grabber) ask for an explicit authorization confirmation for the specific target before running.

## Requirements

- Python 3.8 or newer
- Internet connection (only needed for network-lookup modules — encoding, hashing, password and text modules work fully offline)

## Disclaimer

This project is provided for **educational and authorized professional use only**. The author and Team APT 313 are not responsible for misuse or damage caused by this program. Always get written authorization before testing any system you do not own.

## Contributing

Pull requests are welcome. For major changes, open an issue first to discuss what you'd like to add or change. Please keep new modules legal, passive/defensive in nature, and dependency-free where possible.

## License

Released under the [MIT License](LICENSE).

## Author

**MR SILENT313 NASRU**
Red Teamer · Ethical Hacker · Team **APT 313**

> Hack legally. Stay ethical.
