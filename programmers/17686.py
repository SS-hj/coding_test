import re
def solution(files):
    head = re.compile('[^0-9]+')   # + : 1회 이상 반복
    num = re.compile('[0-9]{1,5}') # {n, m} : n회 이상 m회 이하 반복
    return sorted(files, key = lambda x : (head.search(x)[0].lower(),int(num.search(x)[0])))