# python-03

# Exercise 1
## Description:
This program demonstrates how to receive command-line arguments in Python using `sys.argv`.

It prints:
- The program name
- The number of arguments received
- Each argument provided
- The total number of arguments

## Answers:
1. How does your program know what the user wants it to do?
The program knows what the user wants by reading the command-line arguments stored in sys.argv.

2. What’s the difference between the program name and the arguments?
The program name (sys.argv[0]) is the name of the script being executed, while the arguments (sys.argv[1:]) are the values the user provides as input.

3. What does sys.argv contain?
sys.argv contains a list where the first element is the program name and the remaining elements are the arguments given by the user.

4. Does the program correctly demonstrate command-line argument processing?
Yes, the program correctly reads arguments, counts them, and displays them.

# Exercise 2

## Description:
This program receives player scores from the command line using `sys.argv`.  
It stores the scores in a list, ignores invalid inputs using try/except, and calculates basic statistics such as total score, average score, highest score, lowest score, and score range.

## Answers:

1. How does sys.argv work?
`sys.argv` is a list that contains the command-line arguments passed to the program.  
The first element is the program name, and the remaining elements are the values entered by the user.

2. How are the scores processed in the program?
The program loops through the arguments starting from index 1, converts each value to an integer using `int()`, and stores valid scores in a list.  
If a value cannot be converted to an integer, a try/except block handles the error and skips the invalid input.

3. Why is a list used?
A list is used to store all valid scores so the program can count them, calculate totals, find the highest and lowest scores, and compute the average.

4. How does the program handle invalid input?
The program uses a try/except block to catch conversion errors.  
If the user enters a non-numeric value, the program prints a message and continues processing the remaining scores.

# Exercise 3

## Description:
This program demonstrates a 3D coordinate system using tuples.  
It creates fixed positions, parses coordinate strings into tuples, calculates 3D Euclidean distances from the origin, and handles invalid input gracefully.  
It also demonstrates tuple unpacking for accessing x, y, z coordinates.

## Answers:

1. How does tuple unpacking work?
Tuple unpacking allows you to assign each element of a tuple to a separate variable in a single statement.  
Example:
```python
x, y, z = (3, 4, 0)


