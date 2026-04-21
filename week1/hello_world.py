#!/usr/bin/env python3
"""Write 'Hello world' to a file and print it to the screen."""

text = "Hello world"

# Print to screen
print(text)

# Write to file
with open('content.txt', 'w') as file:
    file.write(text)
