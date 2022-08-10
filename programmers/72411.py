import collections
import itertools

def solution(orders, course):
    result = []
    for n in course:
        comb = []
        for order in orders:
            comb += itertools.combinations(sorted(order), n)
        most_comb = collections.Counter(comb).most_common()
        if most_comb[0][1] < 2: break
        result += [k for k, v in most_comb if v == most_comb[0][1]]
    return list(map(''.join,sorted(result)))