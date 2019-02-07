import network, time
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
# Tries to connect to the "VG3Data" school network
sta_if.connect("VG3Data", "*Password removed for GitHub*")
# Waits for the connection to be established
while not sta_if.isconnected():
    time.sleep(0.1)
# Prints the IP address
print(sta_if.ifconfig())
