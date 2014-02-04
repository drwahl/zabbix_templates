#!/usr/bin/env python

for line in open('/var/log/puppet/puppet.log'):
    if "Finished catalog run in" in line:
        foo = line

print foo.strip('\n').split()[-2]
