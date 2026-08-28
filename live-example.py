# device1 = {"name": "lyfey01", "ip":"10.0.0.1", "serial_number":"DFKI123"}
# device2 = {"name": "lyfey02", "ip":"10.0.0.2", "serial_number":"DFKI124"}
# list_devices = [device1, device2]
# look_for = "lyfey02"
# look_ip = "10.0.0.1"
# flag = 0
# for device in list_devices:
#     if device["name"] == look_for and device["ip"] == look_ip :
#         print("device found")
#         flag = 1
#         break
# if not flag:
#     print("device not found")


# numbers  = [2,4,1,3,4,5,6,7,8]
# def filter_numbers(numbers):
#     my_even_numbers = []
#     for number in numbers:
#         if number % 2 != 0:
#             continue
#         # print(number)
#         my_even_numbers.append(number)
#     return my_even_numbers
# returned_numbers =  filter_numbers(numbers)
# print(returned_numbers)
# print(type(returned_numbers))



class Device:
    def __init__(self, name, ip):
        self.name = name
        self.ip = ip
    def introduce_yourself(self):
        print(f"hello am {self.name}, you can reach out using {self.ip}")

dev1 = Device("lyfey01", "10.0.0.1")
# print(dev1.name)
# print(dev1.ip)
# print(dev1.introduce_yourself())

dev2 = Device("lyfey02", "10.0.0.2")

print(dev2.name)
print(dev2.ip)
print(dev2.introduce_yourself())