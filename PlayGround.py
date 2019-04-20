import subprocess

ipconfig = subprocess.run('ipconfig', capture_output=True)

str1 = 'Hello your little rascal. Give me some sugar!'
str2 = ''
ipconfigLines = str1.split('. ')

networkInfo = ipconfig.stdout
networkInfo.decode
networkInfo.replace('W', '', 1)
print(networkInfo)

print()

print(str1)
print(ipconfigLines)
for lines in ipconfigLines:
    print(lines)