# Ashik's Automated Vulnerability Scanner

## Overview

**Ashik's Automated Vulnerability Scanner** is a powerful, multi-tool script designed to detect XSS and CSRF vulnerabilities in web applications. Leveraging the capabilities of popular tools like XSStrike, Dalfox, and XSRFProbe, this script automates the scanning process and generates comprehensive vulnerability reports in PDF format.

## Features

- **Multiple Tools Integration**: Utilizes XSStrike, Dalfox, and XSRFProbe for robust vulnerability detection.
- **Multi-threaded Scanning**: Parallel execution of scans for faster results.
- **Payload Management**: Easily load custom payloads from text files.
- **Automated Updates**: Includes functionality to keep all integrated tools up-to-date.
- **Comprehensive Reports**: Generates detailed PDF reports of vulnerabilities.

## Usage

### Prerequisites

- Python 3.x
- Go programming language (for Dalfox)
- Virtual environment (recommended)

### Installation

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/fathiashik/ASHIK.git
   cd ASHIK
   chmod +xashik.py

2. **Set up Virtual Environment:**
    ```sh 
    python3 -m venv myenv
   source myenv/bin/activate

   
