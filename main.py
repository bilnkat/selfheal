import subprocess as sp
import ctypes

guestSSID = 'CJ'
currentSSID = ''

def getCurrentSSID():
    global currentSSID
    output = sp.check_output('netsh wlan show interface')
    x = output.split()
    try:
        i = x.index(b'SSID')
        y = (x[i + 2])
        currentSSID = y.decode('utf-8')
    except ValueError:
        ctypes.windll.user32.MessageBoxW(0, "Oops!  Please connect to a WiFi network...", "Error!", 0)

def ssidChecker(ssid):
    global currentSSID, guestSSID
    if currentSSID == guestSSID:
        ssidAlert(ssid)

def ssidAlert(wifi):
    ctypes.windll.user32.MessageBoxW(0, "You are connected to " + wifi + ". To access internal sites, please connect to MULE.", "Suggestion", 0)

if __name__ == '__main__':
    getCurrentSSID()
    ssidChecker(guestSSID)