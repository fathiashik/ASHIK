import subprocess
import threading
import argparse
import os
from fpdf import FPDF

# Function to install tools
def install_tools():
    tools = {
        "XSStrike": "pip3 install XSStrike",
        "dalfox": "go install github.com/hahwul/dalfox/v2@latest",
        "XSRFProbe": "pip3 install XSRFProbe"
    }
    for tool, command in tools.items():
        print(f"Ashik's tool installer is now installing: {tool}")
        subprocess.run(command, shell=True)

# Function to update tools
def update_tools():
    tools = {
        "XSStrike": "pip3 install --upgrade XSStrike",
        "dalfox": "go install github.com/hahwul/dalfox/v2@latest",
        "XSRFProbe": "pip3 install --upgrade XSRFProbe"
    }
    for tool, command in tools.items():
        print(f"Ashik's tool updater is now updating: {tool}")
        subprocess.run(command, shell=True)

# Function to load payloads from a text file
def load_payloads(file_path):
    try:
        with open(file_path, 'r') as file:
            print(f"Ashik's script is loading payloads from: {file_path}")
            return file.read().splitlines()
    except FileNotFoundError:
        print(f"Ashik's script could not find the file: {file_path}")
        return []

# Function to run XSStrike
def run_xsstrike(url):
    print(f"Ashik's XSStrike is scanning: {url}")
    subprocess.run(["python3", "-m", "XSStrike.xsstrike", "--crawl", "--skip-dom", "-u", url])

# Function to run Dalfox
def run_dalfox(url):
    print(f"Ashik's Dalfox is scanning: {url}")
    subprocess.run(["dalfox", "url", url])

# Function to run XSRFProbe
def run_xsrfprobe(url):
    print(f"Ashik's XSRFProbe is scanning: {url}")
    subprocess.run(["xsrfprobe", "-u", url])

# Function to create PDF report
class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, "Ashik's Vulnerability Report", 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(10)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

    def add_vulnerability(self, vuln):
        self.chapter_title(f"{vuln['type']} Vulnerability")
        self.chapter_body(f"URL: {vuln['url']}\nPayload: {vuln['payload']}")

def create_pdf_report(vulnerabilities, filename="ashik_vulnerability_report.pdf"):
    pdf = PDFReport()
    pdf.add_page()
    for vuln in vulnerabilities:
        pdf.add_vulnerability(vuln)
    pdf.output(filename)

def main():
    print("""
       _         _     _ _     
      / \\  _   _| |__ (_) |___ 
     / _ \\| | | | '_ \\| | / __|
    / ___ \\ |_| | |_) | | \\__ \\
   /_/   \\_\\__,_|_.__/|_|_|___/
    """)

    parser = argparse.ArgumentParser(description="Ashik's Automated Vulnerability Scanner")
    parser.add_argument('-u', '--urls', required=True, help='URL or path to text file containing URLs')
    parser.add_argument('--generate-pdf', action='store_true', help='Generate PDF report')
    parser.add_argument('--update-tools', action='store_true', help='Update tools to the latest version')

    args = parser.parse_args()

    if args.update_tools:
        update_tools()
    else:
        install_tools()

    urls = []
    if os.path.isfile(args.urls):
        urls = load_payloads(args.urls)
    else:
        urls.append(args.urls)

    all_vulnerabilities = []
    threads = []
    for url in urls:
        threads.append(threading.Thread(target=run_xsstrike, args=(url,)))
        threads.append(threading.Thread(target=run_dalfox, args=(url,)))
        threads.append(threading.Thread(target=run_xsrfprobe, args=(url,)))

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    if args.generate_pdf:
        create_pdf_report(all_vulnerabilities)

if __name__ == "__main__":
    main()
