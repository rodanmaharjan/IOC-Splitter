import re

# Define the input file path and output file paths
input_file_path = 'input.txt'
ip_output_path = 'ip.txt'
domain_output_path = 'domain.txt'
url_output_path = 'url.txt'
hash_output_path = 'hash.txt'
final_output_path = 'final.txt'

# Initialize empty lists to store IP, Domain, URL, and Hash values
ip_values = []
domain_values = []
url_values = []
hash_values = []

# Regular expression pattern for URL matching
url_pattern = r'^(http|https)://\S+'

# Regular expression pattern for a valid IP address with an optional port
ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(:\d+)?'

# Open the input file for reading
with open(input_file_path, 'r') as input_file:
    # Iterate over each line in the input file
    for line in input_file:
        line = line.strip()

        # Check if the line matches the URL pattern
        if re.match(url_pattern, line):
            url_values.append(line)

        # Check if the line matches the IP address pattern
        elif re.match(ip_pattern, line):
            ip_values.append(line)

        # If none of the above conditions are met, consider it a hash
        else:
            domain_values.append(line)

# Write IP values to ip.txt
with open(ip_output_path, 'w') as ip_file:
    for ip in ip_values:
        ip_file.write(ip + '\n')

# Write Domain values to domain.txt
with open(domain_output_path, 'w') as domain_file:
    for domain in domain_values:
        domain_file.write(domain + '\n')

# Write URL values to url.txt
with open(url_output_path, 'w') as url_file:
    for url in url_values:
        url_file.write(url + '\n')

# Write Hash values to hash.txt
with open(hash_output_path, 'w') as hash_file:
    for hash_value in hash_values:
        hash_file.write(hash_value + '\n')

print("Separation complete.")

# Create final.txt in the correct order
with open(final_output_path, 'w') as final_file:
    with open(ip_output_path, 'r') as ip_file:
        final_file.write(ip_file.read())

    with open(domain_output_path, 'r') as domain_file:
        final_file.write(domain_file.read())

    with open(url_output_path, 'r') as url_file:
        final_file.write(url_file.read())

    with open(hash_output_path, 'r') as hash_file:
        final_file.write(hash_file.read())

print("final.txt created.")
