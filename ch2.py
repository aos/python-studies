# Exercise 2.2 :

# 1. Calculate the volume of a sphere (v = (4/3) * PI * r^3)
r = 5
v = (4/3) * 3.1415 * (r**3)
print(v)

# 2. Wholesale cost of 60 copies
cover = 24.95
book_cover = cover * 0.6
num_copies = 60
shipping = 3 + (0.75 * (num_copies - 1))
total = (book_cover * num_copies) + shipping
print(total)

# 3. Time for breakfast
leave = (6 * 60 * 60) + (52 * 60)
easy = 2 * ((8 * 60) + 15)
tempo = 3 * ((7 * 60) + 12)
breakfast_sec = (easy + tempo) / 60
print(breakfast_sec)
