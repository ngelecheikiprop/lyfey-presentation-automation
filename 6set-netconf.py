from jnpr.junos import Device
from jnpr.junos.utils.config import Config


device = Device(
    host="192.168.100.2",
    user="lab",
    passwd="lab123"
)


config_commands = """
set interfaces ge-0/0/5 description CONFIGURED_USING_NETCONF
set interfaces ge-0/0/5 unit 0 family inet address 10.10.16.1/30

"""

# set interfaces ge-0/0/5 unit 0 family inet address 10.10.16.1/30
device.open()

print("Connected using NETCONF")

config = Config(device)

config.lock()

config.load(
    config_commands,
    format="set"
)

config.commit()

config.unlock()


interfaces = device.rpc.get_interface_information(
    interface_name="ge-0/0/5",
    terse=True
)

print(interfaces)

device.close()

print("NETCONF configuration completed")