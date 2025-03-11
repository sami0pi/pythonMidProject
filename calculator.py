import math

print("==================")
print("Area Calculator")
print("==================", end="\n\n")

print("1. Triangle")
print("2. Rectangle")
print("3. Square")
print("4. Circle")
print("5. Quit", end="\n\n")

print("Enter your choice: ", end="")
choice = int(input())

if choice == 5:
    exit()

if choice == 1:
    print("Enter base: ", end="")
    base = float(input())
    print("Enter height: ", end="")
    height = float(input())
    area = 0.5 * base * height
elif choice == 2:
    print("Enter base: ", end="")
    base = float(input())
    print("Enter height: ", end="")
    height = float(input())
    area = base * height
elif choice == 3:
    print("Enter side: ", end="")
    side = float(input())
    area = side * side
elif choice == 4:
    print("Enter radius: ", end="")
    radius = float(input())
    area = math.pi * radius * radius

print(f"Area: {area}")