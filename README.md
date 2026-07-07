# SyntecxHub SQL Injection Scanner

## Description
An educational SQL Injection detection project developed during the SyntecxHub Cybersecurity Internship.

## Features
- SQL payload management
- SQL error detection
- Logging support
- Report generation
- Modular Python architecture
- Safe testing using DVWA

## Project Structure

```text
Syntecxhub_SQL_Injection_Scanner/
│
├── scanner.py
├── payloads.py
├── detector.py
├── logger.py
├── report.py
├── config.py
├── requirements.txt
├── README.md
│
├── logs/
│
└── reports/
```

## Technologies Used
- Python 3
- Requests
- Git
- GitHub
- DVWA
- Kali Linux

## Installation

```bash
git clone https://github.com/peterthesalem/Syntecxhub_SQL_Injection_Scanner.git
cd Syntecxhub_SQL_Injection_Scanner

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

## Usage

```bash
python scanner.py
```

## Example Output

```text
Testing payload: '
Status Code: 200
No SQL Errors Found.
```

## Ethical Use

This project is intended strictly for educational purposes and authorized testing environments such as DVWA and local laboratories.

## Author

PeterTheSalem
Cybersecurity Student | SOC Analyst Path | SyntecxHub Intern
