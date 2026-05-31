# simulate tea heating using while loop

current_temp = float(input("please enter current temp: "))

while current_temp <=100:
    print(f"Current temp is: {current_temp}")
    current_temp = current_temp+15

print("serve tea")