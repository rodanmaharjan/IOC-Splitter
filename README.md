⚡️ IOC-Splitter 🚀

IOC-Splitter is a simple and powerful Python script designed to help you extract and categorize Indicators of Compromise (IOCs) from raw text files. With this tool, you can quickly and efficiently split out IP addresses, domains, URLs, and hash values into separate files — all while generating a clean, combined output file.

🛠 Features
💡 Extract and categorize IOCs: Quickly separates IP addresses, domains, URLs, and hash values into individual files.
📂 Organized output: Creates separate output files for IPs, domains, URLs, and hashes.
📝 Consolidated IOC file: Combines all extracted IOCs into a single, well-ordered file.
🏃‍♂️ Easy to run: No external dependencies — just Python and your input file.

🔧 Requisites
Before running the script, make sure you have:
Python 3.x:
Install Python 3.x from python.org.
Input File (input.txt):
Prepare a text file containing your IOCs (URLs, IPs, domains, and hash values), each on a new line.

🚀 How to Use
Clone the repository:
git clone https://github.com/yourusername/IOC-Splitter.git
cd IOC-Splitter

Prepare your input.txt:
Include your IOCs in the input file, with each IOC on a new line.

Run the script:

python3 ioc_splitter.py

Check the output:
The following files will be created:

ip.txt: Extracted IP addresses.
domain.txt: Extracted domain names.
url.txt: Extracted URLs.
hash.txt: Extracted hash values.
final.txt: A consolidated file containing all IOCs in the correct order.

📂 Example
Input (input.txt):
  arduino
  Copy code
  8.8.8.8
  example.com
  https://malicious-url.com
  deadbeefdeadbeefdeadbeefdeadbeef
  1.1.1.1
  anotherexample.org
  http://phishing-site.com
  cafebabe0000dead0000cafebabe0000
  
Output:

ip.txt:
  8.8.8.8
  1.1.1.1

domain.txt:
  example.com
  anotherexample.org
  
url.txt:
  https://malicious-url.com
  http://phishing-site.com
  
hash.txt:
  deadbeefdeadbeefdeadbeefdeadbeef
  cafebabe0000dead0000cafebabe0000
  
final.txt (combined file):
  Copy code
  8.8.8.8
  1.1.1.1
  example.com
  anotherexample.org
  https://malicious-url.com
  http://phishing-site.com
  deadbeefdeadbeefdeadbeefdeadbeef
  cafebabe0000dead0000cafebabe0000
  
📦 Installation & Requirements
Python 3.x: Install from python.org.
No additional libraries required. The script uses built-in Python libraries such as re for regular expressions and basic file handling.

💡 Contributing
We welcome contributions! Feel free to fork the project, open issues, or submit pull requests to improve IOC-Splitter.

🏁 Get Started
Ready to separate and manage your IOCs? Clone the repo and start automating your IOC extraction process today!

