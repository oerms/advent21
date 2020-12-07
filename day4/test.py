#!/usr/bin/env python3

import re

rexpHgt = re.compile('^[0-9]*((cm)|(in))$')
print(rexpHgt.match('120cm'))

rexpHcl = re.compile('^#[0-9A-Fa-f]{6}$')
print(rexpHcl.match('#123e56'))

rexpEcl = re.compile('^((amb)|(blu)|(brn)|(gry)|(grn)|(hzl)|(oth))$')
print(rexpEcl.match('blu'))

rexpPid = re.compile('^[0-9]{9}$')
print(rexpPid.match('123123123'))


