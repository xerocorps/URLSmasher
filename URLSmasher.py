import os
import re
import argparse
import sys

# Define command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-u", "--urls", type=argparse.FileType('r'), default=sys.stdin,
                    help="file containing URLs, one per line (default: read from stdin)")
args = parser.parse_args()

# Read the list of URLs from the specified file or standard input
urls = [line.strip() for line in args.urls]

# Loop over each URL
for url in urls:
    # Extract the path from the URL
    match = re.search("(?<=://)[^/]*(/.*)?", url)
    if match:
        path = match.group(1) or "/"
    else:
        print(f"Invalid URL: {url}")
        continue
    
    # Create a list of all possible subdirectories in the path
    subdirs = path.split("/")
    abs_paths = [os.path.join("/", "/".join(subdirs[:i+1])) for i in range(len(subdirs))]
    
    # Print the absolute paths for each variant, with the URL prefix added
    for abs_path in abs_paths:
        print(f"{url}{abs_path}")
    print()
