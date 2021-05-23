from collections import defaultdict

def groupAnagrams(strs):
    # key Error 방지를 위해 defaultdict 선언
    ana = defaultdict(list)

    for word in strs:
        # 문자열 sorted 가능, value로 2개 이상의 값을 가지고 싶다면 append
        ana[''.join(sorted(word))].append(word)

    return list(ana.values())

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))