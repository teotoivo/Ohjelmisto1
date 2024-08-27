number_array = []

while True:
    number = input("Give a number: ")
    if number == "":
        break
    number_array.append(number)
print("max:", max(number_array))
print("min:", min(number_array))