# Using slices

list_1 = ["Mechatronics Engineering"]  # Create a list only one element

print(len(list_1))  # Show size of the list 1

list_2 = list("Mechatronics Engineering")  # Create second list with more elements

print(len(list_2))  # Show size of the list 2

list_3 = list("Cello")

# You can write slices without values (initial value of the list: final value of the list)
print(list_3[:])

print(list_3[1:4])

print(list_3[0:5:2])

print(list_3[5:0:-1])
