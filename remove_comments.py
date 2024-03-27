import re # importing "re" module for regular expressions
'''
regular expressions are used for searching and manipulating strings, in this case we want to find single-line comments and multi-line comments.
But we also want to ignore all print statements that uses tripple quotes or tripple single quotes to create a multi-line print. 
In other words we want the script to skip all print statements that uses tripple quotes or tripple single quotes.
For this we use regular expression but we uses if statement to check if the line starts with print and if it does we skip it.
Also instead of directly using the regular expressions as for the single_comment we define it as a pattern instead for the "skip print function"
'''
# Coded by: Qyfashae
print("Choose an option below to start cleaning up your scripts")

def remove_comments_single(code): # function that removes single line comments
    code = re.sub(r'#.*', '', code) # match single-line comments
    return code # return the code

def remove_comments_multi(code): # function that removes multi-line comments
    pattern = r'print\s*\(\s*("""|\'\'\').*?\1|("""|\'\'\').*?\2' # match multi-line comments
    code = re.sub(pattern, lambda match: match.group(0) if match.group(0).strip()[:6] == 'print(' else '', code, flags=re.DOTALL) # remove multi-line comments but exclude print statements
    return code # return the code

def remove_all_comments(code): # function that removes both single and multi-line comments
    code = remove_comments_single(code) # remove single line comments
    code = remove_comments_multi(code) # remove multi-line comments
    return code # return the code

option = input("Do you want to remove only single line comments (0), multiline comments (1) or both (2) ?: ") # user input 
file_path = input("Enter the path of the file: ") # file path 

with open(file_path, 'r') as file: # open the specified file
    code = file.read() # opens and reads the file

if option == "0": # if the user wants to remove single line comments
    code = remove_comments_single(code) # remove single line comments
elif option == "1": # if the user wants to remove multiline comments
    code = remove_comments_multi(code) # remove multiline comments
elif option == "2": # if the user wants to remove both single and multiline comments
    code = remove_all_comments(code) # remove both single and multiline comments

output_file_path = input("Enter the path of the output file: ") # output file path

with open(output_file_path, 'w') as file: # open the output file
    file.write(code) # write the code
