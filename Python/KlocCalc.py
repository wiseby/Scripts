#!/usr/bin/env python3

'''
Script that counts KLOC (Thousand Lines Of Code)
Recursivly walks a directory structure specified as first argument
or current working dir if not specified

Displays number of lines, characters and KLOC as decimal value.

TODO: Add input to only count from a specified time on last modified.
'''

import os
import sys
import re

ignore = ['.git', 'bin', 'obj', 'node_modules', 'dist', 'env']
defaultExtensions = ['.cs', '.py', '.html', '.ts', '.js']
hits = []
lineCount = 0
charCount = 0

args = sys.argv
processPath = ''
if len(args) >= 2:
    processPath = args[1]
else:
    processPath = os.getcwd()

fileExtensionRegex = re.compile(r'(.{1}[a-z]+)$')


print('Processing files in directory ', processPath)


for root, dirs, files in os.walk(processPath):
    for folder in ignore:
        if folder in dirs:
            dirs.remove(folder)

    for file in files:
        matches = re.findall(fileExtensionRegex, file)
        firstOrDefault = matches[0] if len(matches) > 0 else ''
        if firstOrDefault in defaultExtensions:
            hits.append(root + "/" + file)

for file in hits:
    with open(file) as f:
        for line in f:
            lineCount += 1
            charCount += len(line.replace(" ", ""))


totalFiles = len(hits)
kloc = round(lineCount / 1000, 2)
for file in hits:
    print(file)

print('---------------')
print('Number of files mathing extensions: ', totalFiles)
print('---------------')
print(f'A total of {lineCount} lines with {charCount} characters was found')
print('---------------')
print(f'KLOC result: {kloc}')
