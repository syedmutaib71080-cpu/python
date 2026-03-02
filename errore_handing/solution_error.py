file = open("file.txt", "w")
try:
    file.write("Hello, World!")

finally:
    file.close()

with open("file.txt", "w") as file:
    file.write("Hello, World!")