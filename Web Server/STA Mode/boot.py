import network
import gc

wifiStation = {
        "ssid" : "ESP-32 Web Server",
        "pwd" : "012345678",
}

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=wifiStation["ssid"], password=wifiStation["pwd"], authmode = network.AUTH_WPA_PSK)


