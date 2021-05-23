def isPalindrome(s):
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        return strs[::-1] == strs

print(isPalindrome("race a car"))


# 정규식 및 슬라이싱 사용 풀이 (가장 빠름)
import re
def isPalindrome(s):
        s = s.lower()
        # 정규식으로 불필요한 문자 필터링
        s = re.sub('[^a-z0-9]', '', s)
        return s == s[::-1]


# 리스트 이용
def isPalindrome(s):
    strs =[]
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.pop(0) != strs.pop(): # 시간복잡도 O(n), O(1)
            return False


# deque를 이용한 최적화
from collections import deque
def isPalindrome(s):
    while len(strs) > 1:
        if strs.popleft() != strs.pop():  # 시간복잡도 O(1), O(1)
            return False