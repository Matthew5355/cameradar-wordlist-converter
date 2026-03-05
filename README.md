![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Tool](https://img.shields.io/badge/target-Cameradar-orange.svg)
![Cybersec](https://img.shields.io/badge/sector-Pentesting-red.svg)

# 🎥 Cameradar Wordlist Converter

A lightweight Python utility to convert standard password wordlists (`.txt`) into the specific JSON format required by **Cameradar**.

## ✨ Features
* **Automated Pairing:** Automatically pairs each password with common camera usernames (`admin`, `root`, `administrator`).
* **Clean Output:** Generates a JSON array ready to be used with the `--credentials` flag in Cameradar.
* **Error Handling:** Robust handling of different file encodings (UTF-8, etc.).

## 🚀 Usage

1. **Prepare your wordlist:** Make sure you have a `.txt` file with one password per line.
2. **Run the converter:**
   ```bash
   python3 convert_txt_to_json.py -f passwords.txt -o credentials.json
   ```

### Arguments:
| Flag | Description | Required |
| :--- | :--- | :--- |
| `-f`, `--file` | Path to your input `.txt` wordlist | Yes |
| `-o`, `--output` | Name of the output `.json` file | Yes |

## 🛠️ Example Output
For a password `12345`, the tool generates:
```json
[
  {
    "username": "admin",
    "password": "12345"
  },
  {
    "username": "root",
    "password": "12345"
  }
]
```

## ⚠️ Disclaimer
This tool is for educational purposes and authorized security auditing only. Using this tool against systems without permission is illegal.
