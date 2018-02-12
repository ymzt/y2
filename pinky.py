#!/usr/bin/env python

import os
import re
import sys
import base58

dir = os.path.dirname(os.path.abspath(__file__))

encode = lower  = False
digits, length, n = (9009, 4, 0)

# print (sys.argv)

if re.match("^help$", sys.argv[1]):
    print("pinky.py [encode][lower] <digits> <length> <shift>")
    sys.exit()
    
if re.match("^en(c|co|cod|code)$", sys.argv[1]):
    encode = True
    sys.argv.pop(1)

if re.match("^lo(w|we|wer)$", sys.argv[1]):
    lower = True
    sys.argv.pop(1)

try:    
    digits = sys.argv[1]
    length = int(sys.argv[2])
    n      = int(sys.argv[3])
except (IndexError, ValueError) as e:
    pass

pi = open('%s/pi1000000.txt'%dir, 'r').read()
nn = max(0, n+length-len(digits))
print(r'regex=(%s.{%s})'%(digits, nn))
ma = re.search(r'(%s.{%s})'%(digits, nn), pi)
if ma is None:
    print("%s is not found in PI"%digits)
    sys.exit()

str = ma.group(1)
print(str, file=sys.stderr)
str = str[n:length+n]

if encode:
    str = base58.b58encode(str.encode(encoding='utf-8'))
    str = str[:length]

if lower:
    str = str.lower()
    
print(str, end="")

#bstr = cstr.encode(encoding='utf-8')
#print(base58.b58encode(bstr))
