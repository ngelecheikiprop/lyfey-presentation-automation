from netmiko import ConnectHandler

device = {
    "device_type": "juniper_junos",
    "host": "192.168.100.2",
    "username": "lab",
    "password": "lab123",
}

config_commands = [
    "set interfaces ge-0/0/1 description CONNECTED_TO_ROUTER_2",
    "set interfaces ge-0/0/1 unit 0 family inet address 10.10.12.1/30",
]

connection = ConnectHandler(**device)

print("Connected to device")

output = connection.send_config_set(config_commands)
print(output)

output = connection.commit()
print(output)

connection.disconnect()

print("Configuration completed")