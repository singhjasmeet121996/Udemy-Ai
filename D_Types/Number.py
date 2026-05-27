# Integer

black_tea_g = 14
ginger_g = 3

total_grams = black_tea_g + ginger_g
print(f"Total tea grams: {total_grams}")

remain_tea =black_tea_g - ginger_g
print(f"Remaining tea grams: {remain_tea}")

milk_ml = 200
servings = 4
milk_per_serving = milk_ml / servings
print(f"Milk per serving: {milk_per_serving} ml")

total_tea_bags = 10
pots = 4
bags_per_pot = total_tea_bags // pots
print(f"Bags per pot: {bags_per_pot}")

total_cardamom_pods = 10
pods_per_cup = 3
leaftover_pods = total_cardamom_pods % pods_per_cup
print(f"Leftover cardamom pods: {leaftover_pods}")

base_flaver_strenth = 2
scale_fctor = 3
powerful_flovor= base_flaver_strenth ** scale_fctor
print(f"Powerful flavor: {powerful_flovor}")

total_tea_leaves_harvested = 1_000_000_000
print(f"Total tea leaves harvested: {total_tea_leaves_harvested}")  