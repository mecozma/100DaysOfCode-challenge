"""
Given a filename and a string on the commandline, print all lines from the file
that contain the string.
Example: grep world input.txt
input.txt
    Hello world,
    today is Monday
    and I say hello
    to the world.
Output:
    Hello world,
    to the world.
"""

import sys


if len(sys.argv) < 3:
    print("Please provide a string and the source list!")
    exit()

string = sys.argv[1]
source_file = sys.argv[2]
output = ""
# Open the source file.
with open(source_file, "r") as file:
    # Iterate each line in the file.
    for line in file:
        # Check if the the passes string is contained by the text line.
        if string.lower() in line.lower():
            # If the condition is true concatenate the line with he output var.
            output += line + "\n"
    print(output)
# Write the output value to the output.txt file.
with open("output.txt", "a") as output_data:
    output_data.write(output)
