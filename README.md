<div align="center">

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Tool](https://img.shields.io/badge/target-Cameradar-orange.svg)
![Cybersec](https://img.shields.io/badge/sector-Pentesting-red.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

# 🎥 Universal Wordlist to JSON Converter
### (Cameradar Compatible)

</div>

A lightweight Python utility designed to bridge the gap between raw password lists and structured data. It transforms standard `.txt` wordlists into a versatile JSON format, optimized for **Cameradar** but adaptable for any security auditing tool.

## ✨ Features
* **Automated Pairing:** Automatically pairs each password with industry-standard camera usernames (`admin`, `root`, `administrator`).
* **Structured Output:** Generates a clean JSON array ready for immediate use in security workflows.
* **Robust Error Handling:** Seamlessly handles various file encodings (UTF-8, etc.) to prevent crashes during large wordlist processing.
* **Lightweight & Fast:** Minimal dependencies, high-speed execution.

## 🚀 Usage

1. **Prepare your wordlist:** Ensure you have a `.txt` file with one password per line.
2. **Run the converter:**
   ```bash
   python3 convert_txt_to_json.py -f passwords.txt -o credentials.json

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


## 🧩 Compatibility

While specifically designed for **Cameradar**, the generated JSON follows standard key-value pairing, making it easily adaptable for:

* Custom Python/C++ security scripts.

* Brute-force tools supporting JSON input.

* Database imports (NoSQL/SQL).


## ⚠️ Disclaimer

This tool is for educational purposes and authorized security auditing only. Using this tool against systems without permission is illegal. 
