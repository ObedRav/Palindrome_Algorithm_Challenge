import doctest
import sys

def highestValuePalindrome(s: str, n: int, k: int) -> str:
    """
    The function takes a string `s`, its length `n`, and the maximum number of
    changes allowed `k`, and returns the highest value palindrome that can be obtained by changing at
    most `k` characters in `s`.
    
    :param s: The input string that we want to convert into a palindrome
    :param n: The parameter `n` represents the length of the input string `s`
    :param k: The parameter `k` represents the maximum number of changes allowed to convert the string
    `s` into a palindrome
    :return: a string, which is the highest value palindrome that can be obtained by changing at most k
    characters in the input string s.
    
    ## Tests:
    >>> highestValuePalindrome("1231", 4, 3)
    '9339'

    >>> highestValuePalindrome("12321", 5, 1)
    '12921'

    >>> highestValuePalindrome("12345", 5, 2)
    '54345'

    >>> highestValuePalindrome("12345", 5, 4)
    '99399'

    >>> highestValuePalindrome("12345", 5, 5)
    '99999'

    >>> highestValuePalindrome("", 0, 0)
    'Invalid input: n should be at least 1, and k should be non-negative.'
    """
    # Step 0: Check for invalid input
    if n < 1 or k < 0:
        return "Invalid input: n should be at least 1, and k should be non-negative."

    # Step 1: Convert the input string to a list for easy manipulation
    s = list(s)

    # Step 2: Count differences between characters at corresponding positions
    differences_count = 0
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            differences_count += 1
    
    # Step 3: Check if differences exceed allowed changes (k)
    if differences_count > k:
        return '-1'  # Impossible to create a palindrome
        
    # Step 4: Iterate to maximize the palindrome while staying within k changes
    for i in range(n // 2):
        left_char, right_char = s[i], s[n - 1 - i]

        # If characters at this position are different
        if left_char != right_char:
            differences_count -= 1

        # Decide which character to change to '9' to maximize value
        if k == differences_count or (left_char == '9' and right_char == '9'):
            continue
        if left_char == right_char and k == differences_count + 1:
            continue
        
        # Check if we can use multiple changes to make both '9'
        if k - differences_count > 1:
            k -= (left_char != '9') + (right_char != '9')
            s[i] = s[n - 1 - i] = '9'
        else:
            # Otherwise, choose the maximum of the two characters
            s[i] = s[n - 1 - i] = max(left_char, right_char)
            k -= 1

    # Step 5: Handle the case of an odd-length string with remaining changes
    if n % 2 == 1 and k > 0:
        s[n // 2] = '9'

    # Step 6: Convert the list of characters back to a string and return
    return "".join(s)


if __name__ == "__main__":
    try:
        s = input("Please enter a string representation of an integer (e.g., '12345'): ")
        n = int(input("Please enter the length of the string (1 or greater): "))
        k = int(input("Please enter the maximum number of changes allowed (0 or greater): "))
    except ValueError:
        print("\nInvalid input. Please enter valid integers for n and k.")
        sys.exit(1)

    result = highestValuePalindrome(s, n, k)
    print(f"\nHighest Value Palindrome: {result} \n")
    
    # Run doctests and display test results
    print("Running Tests")
    doctest.testmod()
    print("Tests Completed")
