#!/usr/bin/python3
"""
    A script that reads stdin line by line and computes metrics input format\
    <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"\
        <status code> <file size>

    201.67.113.164 - [2023-01-19 19:24:28.419400]\
        "GET /projects/260 HTTP/1.1" 200 510

    if not input format skip line

"""
# Get the line from std output
# scan the line for time, status code, file size

import sys

line_counter = 0
total_file_size = 0
stat_code_dict = {"200": 0, "301": 0, "400": 0, "401": 0,
                  "403": 0, "404": 0, "405": 0, "500": 0}
code = 0


def output(stat_code_dict, total_file_size):
    """Prints to the standard output"""
    print("File size: {}".format(total_file_size))
    for k, v in sorted(stat_code_dict.items()):
        if v != 0:
            print("{}: {}".format(k, v))


try:
    for line in sys.stdin:
        if 'Exit' == line.rstrip():
            break
        # time = line.split(" ")[2].split("[")[1]
        status_code = line.split(" ")[-2]
        file_size = int(line.split(" ")[-1].rstrip())
        parsed_line = line.split()

        if len(parsed_line) > 2:
            line_counter += 1

            if line_counter <= 10:
                total_file_size += file_size

                # count the number of times a status_code is used
                if status_code in stat_code_dict.keys():
                    stat_code_dict[status_code] += 1

                if line_counter == 10:
                    output(stat_code_dict, total_file_size)
                    line_counter = 0
finally:
    output(stat_code_dict, total_file_size)
