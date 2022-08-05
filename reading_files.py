# READING FILES

# Created a file named countries.txt
# To read this file, we have to import it into this file

country_file = open ('countries.txt', 'r')
# We mention path in the first field of open() method. Here countries.text is in the same folder
# To read a file from Documents folder : country_file = open ('/Users/<username>/Documents/<filename>', 'r')

# 'r' means we want to read on this file
# 'w' means we want to write/edit on this file
# 'r+' means we want to read as well as write on this file
# 'a' means we want to append(add to the end) to the file

# SEE IF FILE IS READABLE OR NOT. RETURNS TRUE/FALSE
print(country_file.readable())

# Read first line, then first and second, and so on
print(country_file.readline()) # reads first line
print(country_file.readline()) # reads first and second line. Output will have a blank line in between because our .txt has newline character(\n) between two country names

# READ ALL LINES AT ONCE
print(country_file.readlines()) # A list is returned. Comment it for Line 26 to work

# READ SPECIFIC LINE
print(country_file.readlines()[3]) # will give IndexError: list index out of range if we uncomment line 23 as it would have already read and returned all the lines

# Looping through it
for countries in country_file.readlines():
    print(countries)

# Whenever we have opened a file, we also have to ensure that we close the file once our work is done
country_file.close()