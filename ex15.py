
# load module
from sys import argv

# argument variables
script, filename = argv

# open the file
txt = open(filename)

# just a simple text
print(f"Here's your file:")

# read the file
print(txt.read())
#txt.close()

# just a simple text
print("Type filename again:")

# prompt for the file, notice here > is ignored
file_again = input("> ")

# open the file
txt_again = open(file_again)

# read the file
print(txt_again.read())
#txt_again.close()
