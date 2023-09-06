# Highest Value Palindrome 🌟

## Introduction

This Python program calculates the highest value palindrome that can be obtained by changing at most `k` characters in a given string `s`. A palindrome is a string that reads the same forwards and backward. This program ensures that the resulting palindrome has the maximum possible numerical value.

### Why This Exercise? 💡

I selected this exercise because it presents an intriguing challenge: transforming a string into a palindrome while maximizing its numerical value. This problem has real-world applications in data validation, error correction, and even game design. By solving this problem, I aimed to enhance my skills in string manipulation and algorithmic thinking.

## How to Run 🚀

To run the "Highest Value Palindrome" program, follow these simple steps:

1. **Prerequisites**:
   - Ensure you have Python 3.x installed on your system.

2. **Clone the Repository**:
   - Clone this repository to your local machine using your preferred method.

3. **Navigate to the Project Directory**:
   - Open a terminal or command prompt in the project directory.

4. **Run the Program**:
   - Execute the following command to start the program:

     ```bash
     python3 palindrome.py
     ```

5. **Output**:
   - The program will calculate and display the highest value palindrome based on your inputs.

## Example Usage 📝

Here are some example usages of the program:

1. Input string: `"1231"`, Length: `4`, Changes allowed: `3`
   - Output: `"9339"`

2. Input string: `"12321"`, Length: `5`, Changes allowed: `1`
   - Output: `"12921"`

3. Input string: `"12345"`, Length: `5`, Changes allowed: `2`
   - Output: `"54345"`

4. Input string: `"12345"`, Length: `5`, Changes allowed: `4`
   - Output: `"99399"`

5. Input string: `"12345"`, Length: `5`, Changes allowed: `5`
   - Output: `"99999"`

## Input Validation ✅

The program includes input validation to ensure that:
- The length `n` of the string is at least 1.
- The maximum number of changes allowed `k` is non-negative.

Here's an example of input validation in action:

```plaintext
4 1
0011
-1
```

The program will reject invalid input and provide an informative error message.

## Authors

* [**Obed Rayo**](https://github.com/ObedRav) <a href="https://github.com/ObedRav" rel="nofollow"><img align="center" alt="github" src="https://www.vectorlogo.zone/logos/github/github-tile.svg" height="24" /></a>

