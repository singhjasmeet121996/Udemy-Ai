essential_sp ={"cardamom", "cinnamon", "cloves"}
optional_sp ={"ginger", "cinnamon", "pepper"}

all_spices = essential_sp | optional_sp # union of 2 sets
print(f"all spices: {all_spices}")

common_sp = essential_sp & optional_sp # intersection of 2 sets
print(f"common spices: {common_sp}")

only_essential = essential_sp - optional_sp # difference of 2 sets
print(f"only essential spices: {only_essential}")

