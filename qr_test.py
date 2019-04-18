import pyqrcode as pq

# ssid = "NETGEAR78"
# security = "WPA"
# password = "mightyshrub907"
# qr = pq.create(f'WIFI:S:{ssid};T:{security};P:{password};;')
# print(qr.terminal())
#
# qr.png('code.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])


def test_qr_wifi(ssid: str, security: str, password: str):
    qr = pq.create(f'WIFI:S:{ssid};T:{security};P:{password};;')
    return qr


qr = test_qr_wifi('NETGEAR78', 'WPA', 'mightyscrub907')
qr.png('code2.png')
