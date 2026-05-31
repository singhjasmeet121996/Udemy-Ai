ingretients = ["water", "milk", "sugar"]

print(f"origianal list: {ingretients}")

# add a item

ingretients.append("tea leaves")

print(f"ingretients after adding new item: {ingretients}")

# remove a item

ingretients.remove("sugar")

print(f"ingretients after removing an item:: {ingretients}")

# join 2 list together a item

spice_options = ["ginger","cardamom"]
ingretients.extend(spice_options)

print(f"ingretients after combining 2 lists: {ingretients}")

# adding an item at a specific index

ingretients.insert(2,"honey")

print(f"ingretients after adding an item at a 2nd index: {ingretients}")

#removing last item

last_item = ingretients.pop() # remove and save the last item into a var

print(f"last item was:{last_item}")

print(f"ingretients after removing last item:: {ingretients}")

# reverse the list

ingretients.reverse()

print(f"ingretients after reversing: {ingretients}")

#sorting the list

ingretients.sort()

print(f"ingretients after sorting: {ingretients}")


sugar_levels = [5, 3, 8, 1, 4]

print(f"max sugar level: {max(sugar_levels)}")
print(f"min sugar level: {min(sugar_levels)}")


#operator overloading

base_l = ["water", "milk"]
additional_l = ["sugar", "tea leaves"]
full_l = base_l + additional_l
print(f"full list: {full_l}")
