# Pythonic way (이게 더 빠름)
def reverseString(s):
    s.reverse() # 리스트에만 제공
    # s = s[::-1]

# 투 포인터로 구현
def reverseString(s):
    left, right = 0, len(s)-1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1