print("Welcome Customer")
print("Please Insert Your Identity")
name = input("Your Name: ")
birth_date = input("Your Year of Birth: ")
age = 2026 - int(birth_date)

if age >= 18:
    print(f"Nice to meet you {name}, and you're legal ({age})")
    print("Welcome to our new club")
else:
    print("Sorry you haven't met the required age")