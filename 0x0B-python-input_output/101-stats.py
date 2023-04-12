#!/usr/bin/python3

"""
This script reads stdin line by line and computes metrics.

Input format: <IP Address> - "GET HTTP/1.1" <status code> <file size>
Each 10 lines and after a keyboard interruption (CTRL C):
Total file size: File size: <total size>
where <total size> is the sum of all previous (see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear, don’t print anything for this status code
format: <status code>: <number>
status codes should be printed in ascending order
"""

import sys
from collections import defaultdict

total_size = 0
status_counts = defaultdict(int)
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.strip().split()
        status_code = parts[-2]
        total_size += int(parts[-1])
        status_counts[status_code] += 1
        if line_count == 10:
            print(f"Total file size: {total_size}")
            for code in sorted(status_counts.keys()):
                print(f"{code}: {status_counts[code]}")
            line_count = 0
            status_counts.clear()
except KeyboardInterrupt:
    print(f"Total file size: {total_size}")
    for code in sorted(status_counts.keys()):
        print(f"{code}: {status_counts[code]}")
