#!/usr/bin/python3
'''this smodule reads stdin and computes metric'''
import re
import sys

status_code = [200, 301, 400, 401, 403, 404, 405, 500]
stats = {}
size = {'File size': 0}


def print_stats(stat):
    '''this function prints static stored
    args:
        -stat (dictionary): containng the stats
    '''
    print('File size: {}'.format(size.get('File size')))
    stat = dict(sorted(stat.items(), key=lambda x: x[0]))
    for key, val in stat.items():
        print('{}: {}'.format(key, val))


pattern = r'^.*? - \[.*?\] "GET \/projects\/260 HTTP\/1.1" (.*?) (.*)$'
# reading from the stdin
try:
    count = 0
    for line in sys.stdin:
        line = line.strip('\n')
        match = re.match(pattern, line)
        if match:
            status = match.group(1)
            filesize = match.group(2)
            size['File size'] = size.get('File size') + int(filesize)

            try:
                status = int(status)
                if status in status_code:
                    stats[status] = stats.get(status, 0) + 1
            except Exception as e:
                pass
        count += 1

        if count == 10:
            print_stats(stats)
            count = 0
except KeyboardInterrupt as e:
    pass
finally:
    print_stats(stats)
