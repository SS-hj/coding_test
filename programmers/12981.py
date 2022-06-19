def solution(n, words):
    answer = []
    play = [words.pop(0)]
    player = 2
    rot = 1
    for w in words:
        prior = play[-1][-1]
        if player > n:
            player = 1
            rot += 1
        if w in play or w[0] != prior:
            answer = [player, rot]
            break
        play.append(w)
        prior = w[-1]
        player += 1
    if not answer:
        answer = [0,0]
    return answer

''' 참고 코드
def solution(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
    else:
        return [0,0]
'''