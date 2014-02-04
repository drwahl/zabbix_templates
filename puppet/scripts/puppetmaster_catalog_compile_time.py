#!/usr/bin/env python

import datetime
from dateutil.parser import parse

compiled_catalog_lines = []
for line in open('/var/log/puppet/puppetmaster.log'):
    if "Compiled catalog for" in line:
        linedate_lst = line.split()[:3]
        linedate = parse(' '.join(linedate_list))
        if (datetime.datetime.now() - linedate) > datetime.timedelta (minutes=5):
            compile_time = float(line.strip('\n').split()[-2])
            compiled_catalog_lines.append(compile_time)

print round(reduce(lambda x, y: x + y, compiled_catalog_lines) / len(compiled_catalog_lines), 2)
