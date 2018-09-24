import subprocess as sp

sp.call('netsh wlan show profiles')
output = sp.check_output('netsh wlan show profiles')
print(output)
x = output.split()
y = (x[-1])
print(y.decode('utf-8'))