# EDITING FILES

# WRITE
country_file = open ('country.txt', 'w')

country_file.write("This is the new country file")
# If we use this command on our existing file, it will overwrite the previous file. All our content will be removed and replaced by whatever is inside ""
# It's best to use this to create a new file

# APPEND
country_file = open ('country.txt', 'a')
country_file.write("\nThis is the next line") # \n is added so that it is in the next line

# Can be done with any type of file. Here we've used .txt
# Try with .py