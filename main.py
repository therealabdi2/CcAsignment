import re
import time

import nltk

nltk.download('punkt')

# opens the c++ program text
f = open('example.txt', 'r')
# read the file line by line
program = f.read()

print("The original Program is: ")
print(program)

# a set is used to avoid duplication
Identifiers_Output = set()
Keywords_Output = set()
Symbols_Output = set()
Operators_Output = set()
Numerals_Output = set()
Headers_Output = set()


def remove_Spaces(program):
    scanned_Program = []
    for line in prog:
        if line.strip() != '':
            scanned_Program.append(line.strip())
    return scanned_Program


def remove_Comments(program):
    program_Multi_Comments_Removed = re.sub("/\*[^*]*\*+(?:[^/*][^*]*\*+)*/", "", program)
    program_Single_Comments_Removed = re.sub("//.*", "", program_Multi_Comments_Removed)
    program_Comments_removed = program_Single_Comments_Removed
    return program_Comments_removed


# the following are the regular expression for different types
RE_Keywords = "auto|break|case|char|const|continue|default|do|double|else|enum|extern|float|for|goto|if|int|long|register|return|short|signed|sizeof|static|struct|switch|typedef|union|unsigned|void|volatile|while|string|class|struc|include"
# backslash (\) is used before special symbols
RE_Operators = "(\++)|(-)|(=)|(\*)|(/)|(%)|(--)|(<=)|(>=)"
# this means any digit at the start or end of character
RE_Numerals = "^(\d+)$"
RE_Special_Characters = "[\[@&~!#$\^\|{}\]:;<>?,\.']|\(\)|\(|\)|{}|\[\]|\""
# any letter from a-z and after that anything can come (digits or letters)
RE_Identifiers = "^[a-zA-Z_]+[a-zA-Z0-9_]*"
# for header files
RE_Headers = "([a-zA-Z]+\.[h])"

program_Comments_removed = remove_Comments(program)

print("Removing comments...")
time.sleep(3)
print(program_Comments_removed)

# splitting the code line by line to later remove extra spaces in the line
prog = program_Comments_removed.split('\n')

# here we call the function to remove spaces which return the string with no extra spaces
remove_space_prog = remove_Spaces(prog)

# this will rejoin the program
scanned_Program = '\n'.join([str(elem) for elem in remove_space_prog])

print("Removing Extra Spaces...")
time.sleep(3)
print(scanned_Program)

scanned_Program_lines = scanned_Program.split('\n')
match_counter = 0

Source_Code = []
for line in scanned_Program_lines:
    Source_Code.append(line)

for line in Source_Code:
    if line.startswith("#include"):
        tokens = nltk.word_tokenize(line)
    else:
        tokens = nltk.wordpunct_tokenize(line)
    for token in tokens:
        if re.findall(RE_Keywords, token):
            Keywords_Output.add(token)
        elif re.findall(RE_Headers, token):
            Headers_Output.add(token)
        elif re.findall(RE_Operators, token):
            Operators_Output.add(token)
        elif re.findall(RE_Numerals, token):
            Numerals_Output.add(token)
        elif re.findall(RE_Special_Characters, token):
            Symbols_Output.add(token)
        elif re.findall(RE_Identifiers, token):
            Identifiers_Output.add(token)
    print(tokens)

print("Tokenizing...")
time.sleep(3)
print("There Are ", len(Keywords_Output), "Keywords: ", Keywords_Output)
print("\n")
print("There Are ", len(Identifiers_Output), "Identifiers: ", Identifiers_Output)
print("\n")
print("There Are ", len(Headers_Output), "Header Files: ", Headers_Output)
print("\n")
print("There Are", len(Symbols_Output), "Symbols:", Symbols_Output)
print("\n")
print("There Are ", len(Numerals_Output), "Numerals:", Numerals_Output)
print("\n")
