from jnpr.junos import Device

device = Device(
    host="192.168.100.2",
    user="lab",
    passwd="lab123"
)

device.open()

interfaces = device.rpc.get_interface_information(
    terse=True
)

for interface in interfaces.xpath(
    ".//physical-interface/name"
):
    print(interface.text.strip())

device.close()