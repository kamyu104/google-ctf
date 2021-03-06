#!/usr/bin/python
# -*- coding: utf8 -*-
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http:#www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import platform
import sys
import marshal
import types

print """
\x1b[38;5;196m ___   ___   ___   _     ____  ____\x1b[m
\x1b[38;5;202m| |_) | |_) / / \ | |\ |  / / | |_\x1b[m
\x1b[38;5;208m|_|_) |_| \ \_\_/ |_| \| /_/_ |_|__\x1b[m
\x1b[38;5;214mWinja CTF                      2018\x1b[m
"""

def check(s):
  f = '\xc3\xc9\xc4\xc2\xde\x9d\x9d\x80\xe6\xca\xd5\xd5\xc0\xd7\x8e\x94\x97\x80\xf1\xcc\xcb\xd8'
  if len(s) != len(f):
    return False;

  checksum = 0
  for a, b in zip(f, s):
    checksum += ord(b) ^ ord(a) ^ 0xa5

  return checksum == 0

if (sys.version_info.major != 2 or sys.version_info.minor != 7):
  sys.exit("This application requires Python 2.7.")

if len(sys.argv) != 2:
  sys.exit("usage: bronze.pyc <flag>")

flag = sys.argv[1]
if len(flag) >= 32:
  print "Meh."
  sys.exit(1)

alphabet = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}!@#$%+")
for ch in flag:
  if ch not in alphabet:
    print "No."
    sys.exit(1)

if check(flag):
  print "Well done!"
  sys.exit(0)
else:
  print "Nope."
  sys.exit(1)
