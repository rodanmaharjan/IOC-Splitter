import re
import argparse

class IOCSplitter:
    """Class to separate IPs, Domains, URLs, and Hashes from an input file."""
    def __init__(self, input_file_path, ip_output_path, domain_output_path, url_output_path, hash_output_path, final_output_path):
        """Initializes the IOCSplitter with input and output file paths."""
        self.input_file_path = input_file_path
        self.ip_output_path = ip_output_path
        self.domain_output_path = domain_output_path
        self.url_output_path = url_output_path
        self.hash_output_path = hash_output_path
        self.final_output_path = final_output_path
        
        self.ip_values = []
        self.domain_values = []
        self.url_values = []
        self.hash_values = []
        
        self.url_pattern = re.compile(r'^(http|https)://\S+') # Regex for URLs
        self.ip_pattern = re.compile(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(:\d+)?\b') # Regex for IPs
        self.hash_pattern = re.compile(r'\b[A-Fa-f0-9]{32}\b|\b[A-Fa-f0-9]{40}\b|\b[A-Fa-f0-9]{64}\b|\b[A-Fa-f0-9]{128}\b') # Regex for Hashes
        self.domain_pattern = re.compile(r'(?=^.{4,253}$)(^((?!-)[a-zA-Z0-9-]{1,63}(?<!-)\.)+[a-zA-Z]{2,63}$)') # Regex for Domains

    
    def process_file(self):
        """Reads the input file and categorizes each line as IP, URL, Domain, or Hash."""
        with open(self.input_file_path, 'r', encoding='utf-8', errors='ignore') as input_file:
            for line in input_file:
                line = line.strip()

                if self.url_pattern.match(line):
                    self.url_values.append(line)
                elif self.ip_pattern.match(line):
                    self.ip_values.append(line)
                elif self.hash_pattern.match(line):
                    self.hash_values.append(line)
                elif self.domain_pattern.match(line):
                    self.domain_values.append(line)
                else:
                    print(f'Could not categorize: {line}')

    def write_output(self, values, file_path):
        """Writes the categorized values to the respective output file."""
        with open(file_path, 'w', encoding='utf-8') as file:
            for value in values:
                file.write(value + '\n')

    def write_all_files(self):
        """Writes IP, Domain, URL, and Hash values to their respective files."""
        self.write_output(self.ip_values, self.ip_output_path)
        self.write_output(self.domain_values, self.domain_output_path)
        self.write_output(self.url_values, self.url_output_path)
        self.write_output(self.hash_values, self.hash_output_path)

    def create_final_output(self):
        """Creates the final.txt file by combining the contents of all output files."""
        with open(self.final_output_path, 'w', encoding='utf-8') as final_file:
            for file_path in [self.ip_output_path, self.domain_output_path, self.url_output_path, self.hash_output_path]:
                with open(file_path, 'r', encoding='utf-8') as file:
                    final_file.write(file.read())

    def run(self):
        """Main method to process the input file, write outputs, and create the final output."""
        self.process_file()
        self.write_all_files()
        self.create_final_output()

def main():
    """Main function to parse arguments and run the IOCSplitter."""
    parser = argparse.ArgumentParser(description='Separate IPs, Domains, URLs, and Hashes from an input file.')
    parser.add_argument('--input', help='Input file path.', default='input.txt')
    parser.add_argument('--ip_output', help='Output file for IP addresses.', default='ip.txt')
    parser.add_argument('--domain_output', help='Output file for domains.', default='domain.txt')
    parser.add_argument('--url_output', help='Output file for URLs.', default='url.txt')
    parser.add_argument('--hash_output', help='Output file for hashes.', default='hash.txt')
    parser.add_argument('--final_output', help='Final output file combining all outputs.', default='final.txt')

    args = parser.parse_args()

    separator = IOCSplitter(
        input_file_path=args.input,
        ip_output_path=args.ip_output,
        domain_output_path=args.domain_output,
        url_output_path=args.url_output,
        hash_output_path=args.hash_output,
        final_output_path=args.final_output
    )

    separator.run()

if __name__ == '__main__':
    main()
