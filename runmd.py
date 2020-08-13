#!/usr/bin/env python3
import re
import sys

if len(sys.argv) < 2:
    print('Usage: runpymd <file.md>')
    exit()

data = open(sys.argv[1]).read()

output = ''
def print_mock(*args, **kwargs):
    global output
    output += ' '.join(args) + '\n'


offset = 0

for match in re.finditer('```(python|py)\n([^`]*)\n```', data):
    code = match.group(2)
    exec(code, {'print': print_mock})
    addition = '\nOutput:\n```\n' + output + '```\n'
    data = data[:match.end()+offset] + addition + data[match.end()+offset:]
    output = ''
    offset += len(addition)

print(data)
