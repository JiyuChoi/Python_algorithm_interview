def isPalindrome(s):
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        return strs[::-1] == strs

print(isPalindrome("race a car"))


# 정규식 및 슬라이싱 사용 풀이 (가장 빠름)
import re
        s = s.lower()
        # 정규식으로 불필요한 문자 필터링
        s = re.sub('[^a-z0-9]', '', s)
        return s == s[::-1]
