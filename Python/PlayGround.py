import subprocess

ipconfig = subprocess.run(
    'ipconfig',
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
    )

networkInfo = ''

for lines in ipconfig.stdout:
    text = lines.decode("unicode")
    networkInfo.join()

networkInfo.replace('W', '', 1)
print(networkInfo)

print(networkInfo)
