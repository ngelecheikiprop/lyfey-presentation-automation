from netmiko import ConnectHandler


device = {
    "device_type": "juniper_junos",
    "host": "192.168.100.2",
    "username": "lab",
    "password": "lab123",
}

# "set interfaces ge-0/0/1 unit 0 family inet address 10.10.11.1/30",
config_commands = [
    "set interfaces ge-0/0/4 description CONFIGURED_USING_NETMIKO",
    "set interfaces ge-0/0/4 unit 0 family inet address 10.10.15.1/30"
]


connection = ConnectHandler(**device)

print("Connected to device")

output = connection.send_config_set(config_commands)
print(output)

output = connection.commit()
print(output)

print(
    connection.send_command(
        "show interfaces ge-0/0/1 terse"
    )
)

connection.disconnect()

print("Netmiko configuration completed")