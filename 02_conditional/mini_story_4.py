# Smart thermostat system

device_status = input("What is device status(active or not): ").lower()

if device_status == "active":
    current_temp = float(input("What is current temperature in c: "))
    if current_temp > 35:
        print("High Temperature!!!")
    else:
        print("normal Temperature")

else:
    print("device is offline")
