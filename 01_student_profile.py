# Student Profile

name = input("Enter your name: ")
branch = input("Enter your branch: ")
cgpa = float(input("Enter your CGPA: "))

print("\n--- Student Profile ---")
print(f"Name   : {name}")
print(f"Branch : {branch}")
print(f"CGPA   : {cgpa}")

if cgpa >= 8:
    print("Performance: Excellent")
elif cgpa >= 7:
    print("Performance: Good")
else:
    print("Performance: Keep improving")
