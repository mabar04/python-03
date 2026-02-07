import sys
"""
This program demonstrates how to receive command-line arguments
using sys.argv.

sys.argv[0] contains the program name.
The remaining elements contain the arguments provided by the user.
"""
print("=== Command Quest ===")
if len(sys.argv) < 2:
    print("No arguments provided!")
    print("Program name: " + sys.argv[0])
else:
    print("Program name: " + sys.argv[0])
    print(f"Arguments received: {len(sys.argv) - 1}")
    i = 1
    while i < len(sys.argv):
        print(f"Argument {i}: {sys.argv[i]}")
        i = i + 1
print("Total arguments:", len(sys.argv))
