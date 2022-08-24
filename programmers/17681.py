def solution(n, arr1, arr2):
    return [format(i | j,'b').zfill(n).replace("1","#").replace("0"," ") for i,j in zip(arr1,arr2)]