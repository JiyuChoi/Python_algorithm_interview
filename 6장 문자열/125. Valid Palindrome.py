def isPalindrome(s):
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        return strs[::-1] == strs

print(isPalindrome("race a car"))