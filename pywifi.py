import pywifi
import time
# для работы нужен модуль comtypes - pip install comtypes

#from secrets import password

wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]

print("Your interface:", iface.name())
iface.scan()
time.sleep(2)

result = iface.scan_results()
print("Available networks:")

for i in range(len(result)):
    print(result[i].ssid, result[i].bssid, result[i].auth, result[i].akm)

ssid = 'kraus.pnh'
key = '789456123789'

def ConnectToPoint(ssid, key):
    profile = pywifi.Profile()
    profile.ssid = 'kraus.pnh'
    profile.auth = pywifi.const.AUTH_ALG_OPEN
    profile.akm.append(pywifi.const.AKM_TYPE_WPA2PSK)
    profile.cipher = pywifi.const.CIPHER_TYPE_CCMP
    profile.key = '789456123789'

    profile = iface.add_network_profile(profile)
    iface.connect(profile)

    result = iface.status()
    if result == pywifi.const.IFACE_CONNECTED:
        print("Соединение установлено")

ConnectToPoint(ssid, key)
