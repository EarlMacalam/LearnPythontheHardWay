from sys import argv
script, filename = argv

print("I'll open my file:")
file = open(filename, 'w')

# reformat file content using truncate
print("Gonna delete file content, I mean ALL.")
file.truncate()

# Write something
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

# write to file
file.write(f"{line1}\n{line2}\n{line3}")

# closing the file
file.close()
