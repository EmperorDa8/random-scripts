#!/usr/bin/env python3

import sys
import re
import csv
import operator

errors = {}  # number of diff error messages
per_user = {}

errors_report = 'error_message.csv'
per_user_report = 'user_statistics.csv'

logfile = 'C:\\Users\\USER\\Downloads\\log folder\\syslog.log'


pattern = r'(?P<messageType>INFO|ERROR):?\s*(?P<message>.*?)\((?P<username>\w+)\)$'

with open(logfile, 'r') as file:
    for line in file.readlines():
        regex_result = re.search(pattern, line)
        if regex_result:
            message_type = regex_result.group('messageType')
            message = regex_result.group('message')
            username = regex_result.group('username')
            if message_type == 'ERROR':
                errors.setdefault(message, 0)
                errors[message] += 1
                per_user.setdefault(username, [0, 0])[1] += 1
            else:
                per_user.setdefault(username, [0, 0])[0] += 1

error_sorted = sorted(errors.items(), key=operator.itemgetter(1), reverse=True)
per_user_sorted = sorted(per_user.items())

with open(errors_report, 'w', newline='') as error_report:
    writer = csv.writer(error_report)
    writer.writerow(['Error', 'Count'])
    writer.writerows(error_sorted)

with open(per_user_report, 'w', newline='') as user_report:
    writer = csv.writer(user_report)
    writer.writerow(['Username', 'INFO', 'ERROR'])
    for item in per_user_sorted:
        Onerow = [item[0], item[1][0], item[1][1]]
        writer.writerow(Onerow)

