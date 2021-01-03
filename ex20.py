# obtain argv from sys module
from sys import argv

# argument variables to be unpack
script, input_file = argv

# function that read all content in the file
def print_all(f):
    print(f.read())

# restart the position of the curser to 0, i.e, the very first position
def rewind(f):
    f.seek(0)

# read the line of the file content one by one starting at first line
# the line count is just a dummy variable indicator, we can rmv it
def print_a_line(line_count, f):
    print(line_count, f.readline(), end = "")

# open the input_file
current_file = open(input_file)

# simple string
print("First let's print the whole file:\n")

# read all the content of current_file
print_all(current_file)

# simple string
print("Now let's rewind, kind of like a tape.")

# restarting the cursor back to 0 position
rewind(current_file)

# simple string
print("Let's print three lines:")

# print 1st line with its dummy indicator var
current_line = 1
print_a_line(current_line, current_file)

# print 2nd line with its dummy indicator var
current_line += 1
print_a_line(current_line, current_file)

# print 3rd line with its dummy indicator var
current_line += 1
print_a_line(current_line, current_file)
