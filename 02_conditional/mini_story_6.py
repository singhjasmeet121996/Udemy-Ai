# Match case alt to if else

seat_type = input("please select your choice of seat: ").lower()

match seat_type:
    case "general":
        print("General - No garruanty seat but cheapest option")
    case "sleeper":
        print("sleepr - own bed for the ride")
    case "ac":
        print("AC - Air Conditioned coach with comfortable reide")
    case "luxury":
        print("Luxuary - Comfortable beds with AC and Meals")
    case _:
        print("please select a valid Seat Type")