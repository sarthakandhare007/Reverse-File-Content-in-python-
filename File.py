# Open the input file and read its content
try:
    with open("input.txt", "r") as inFile:
        content = inFile.read()
except FileNotFoundError:
    print("Error: input.txt file not found!")
    exit()

# Reverse the content
reversed_content = content[::-1]

# Write the reversed content to the output file
with open("output.txt", "w") as outFile:
    outFile.write(reversed_content)

print("File content reversed successfully!")
