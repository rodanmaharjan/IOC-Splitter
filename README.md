# ⚡️ IOC-Splitter 🚀

![Python](https://img.shields.io/badge/python-v3.x-blue.svg) ![Contributions](https://img.shields.io/badge/contributions-welcome-brightgreen.svg) ![License](https://img.shields.io/github/license/rodanmaharjan/IOC-Splitter)

**IOC-Splitter** is a Python script designed to easily extract and categorize Indicators of Compromise (IOCs) from text files. With this tool, you can split out IP addresses, domains, URLs, and hash values into separate files, and generate a clean, consolidated output file.

---

## 🛠 Features

- 💡 **Extract and categorize IOCs**: Automatically separates IP addresses, domains, URLs, and hash values into individual files.
- 📂 **Organized output**: Creates separate files for IPs, domains, URLs, and hashes.
- 📝 **Consolidated IOC file**: Combines all extracted IOCs into a single file for easy use.
- 🏃‍♂️ **Simple and fast**: No external libraries required — just Python and your input file.

---

## 🔧 Requisites

- **Python 3.x**:  
  Install from [python.org](https://www.python.org/).

- **Input File (`input.txt`)**:  
  A text file that contains your IOCs, each on a new line (URLs, IPs, domains, hashes).

---

## 🚀 How to Use

1. **Clone the repository**:
   ```bash
   git clone https://github.com/rodanmaharjan/IOC-Splitter.git
   cd IOC-Splitter


2. **Prepare your `input.txt`**:  
   Add the IOCs to the `input.txt` file, with each IOC on a new line.

3. **Run the script**:
   ```bash
   python3 ioc_splitter.py
   ```

4. **Check the output**:  
   The script will create the following output files:
   - `ip.txt`: Extracted IP addresses.
   - `domain.txt`: Extracted domains.
   - `url.txt`: Extracted URLs.
   - `hash.txt`: Extracted hash values.
   - `final.txt`: A consolidated file containing all the IOCs in order.

---

## 📂 Example

**Input (`input.txt`):**
```
8.8.8.8
example.com
https://malicious-url.com
deadbeefdeadbeefdeadbeefdeadbeef
1.1.1.1
anotherexample.org
http://phishing-site.com
cafebabe0000dead0000cafebabe0000
```

**Output:**

- **`ip.txt`**:
  ```
  8.8.8.8
  1.1.1.1
  ```

- **`domain.txt`**:
  ```
  example.com
  anotherexample.org
  ```

- **`url.txt`**:
  ```
  https://malicious-url.com
  http://phishing-site.com
  ```

- **`hash.txt`**:
  ```
  deadbeefdeadbeefdeadbeefdeadbeef
  cafebabe0000dead0000cafebabe0000
  ```

- **`final.txt`** (combined file):
  ```
  8.8.8.8
  1.1.1.1
  example.com
  anotherexample.org
  https://malicious-url.com
  http://phishing-site.com
  deadbeefdeadbeefdeadbeefdeadbeef
  cafebabe0000dead0000cafebabe0000
  ```

---

## 📦 Installation & Requirements

- Python 3.x: Install from [python.org](https://www.python.org/downloads/).
- No external libraries needed — uses built-in Python functions for regular expressions and file handling.


---

## 💡 Contributing

Contributions are welcome! Feel free to fork this project, open issues, or submit pull requests to enhance **IOC-Splitter**.

---

## 👨‍💻 Author

**[Rodan Maharjan]**  
Check out more projects on [GitHub](https://github.com/rodanmaharjan).

---

## 🏁 Get Started

Ready to organize and manage your IOCs? [**Clone the repo**](https://github.com/rodanmaharjan/IOC-Splitter.git) and automate your IOC extraction process now!
```
