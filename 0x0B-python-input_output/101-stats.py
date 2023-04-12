#!/usr/bin/python3

import sys
from collections import defaultdict

# Define a defaultdict to count the number of status codes
status_codes = defaultdict(int)

# Initialize the total file size to 0
total_file_size = 0

try:
    # Loop over the lines in the input
    for i, line in enumerate(sys.stdin):
        # Parse the line and extract the relevant information
        parts = line.strip().split()
        ip_address = parts[0]
        status_code = parts[-2]
        file_size = int(parts[-1])

        # Update the status code count and total file size
        status_codes[status_code] += 1
        total_file_size += file_size

        # Print the statistics every 10 lines
        if (i + 1) % 10 == 0:
            print(f"Total file size: {total_file_size}")
            for code in sorted(status_codes.keys()):
                print(f"{code}: {status_codes[code]}")

except KeyboardInterrupt:
    # Handle the keyboard interrupt (CTRL + C)
    print(f"Total file size: {total_file_size}")
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")
