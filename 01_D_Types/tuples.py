masala_spices = ("cardamom", "cinnamon", "cloves")

(spice1, spice2, spice3) = masala_spices

print(f"main masala:{spice1}, {spice2}, {spice3}")

ginger_ratio, cardomom_ratio = 2,1
print(f"ratio of g:{ginger_ratio}, ratio of c: {cardomom_ratio}")
ginger_ratio, cardomom_ratio = cardomom_ratio, ginger_ratio
print(f"after swapping: ratio of g:{ginger_ratio}, ratio of c: {cardomom_ratio}") 

# membership

print(f"is ginger in masala?{'ginger' in masala_spices}")
