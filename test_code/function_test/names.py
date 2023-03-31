from name_function import get_full_name

print("Enter q to stop")
while True:
    first = input("first name: ")
    if first == "q":
        break
    last = input("last name: ")
    if first == "q":
        break

    full_name = get_full_name(first, last)
    print(f"This is full name: {full_name}")