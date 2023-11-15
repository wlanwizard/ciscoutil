import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description='SSH into Cisco devices using IP addresses from a file.')
parser.add_argument('file_path', help='Path to the file containing IP addresses')
parser.add_argument('tags_path', help='Path to the file containing tag names')
args = parser.parse_args()

# Reading IP addresses
file_path = args.file_path
tags_path = args.tags_path

#file_path = "mac_only.txt"

with open(file_path, "r") as file:
    for line in file:
        value = line.rstrip()
        print("")
        print(f"ap {value}")
        with open(tags_path, "r") as tags:
            for tag in tags:
             tag = tag.rstrip()
             print(tag)


# example:
# ap REPLACE
# policy-tag pol_tag_leb
# rf-tag 5ghz_mlh_draeger
# site-tag site_tag_leb