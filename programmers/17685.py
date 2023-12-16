def solution(words):
    words.sort()
    cnt = 0
    visited = set()
    n = len(words)
    for i in range(n-1):
        for j in range(1, len(words[i])+1):
            if words[i][:j] not in visited and words[i][:j]!=words[i+1][:j]:
                break
            else:
                visited.add(words[i][:j])
        cnt += j
        visited.add(words[i][:j])
    for j in range(1, len(words[-1])+1):
        if words[-1][:j] not in visited:
            cnt += j
            break
        j += 1
    return cnt