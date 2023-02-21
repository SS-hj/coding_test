def to_days(date):
    year, month, day = map(int, date.split("."))
    return year * 28 * 12 + month * 28 + day

def solution(today, terms, privacies):
    months = {v[0]: int(v[2:]) * 28 for v in terms}
    today = to_days(today)
    expire = [i + 1 for i, privacy in enumerate(privacies) if to_days(privacy[:-2]) + months[privacy[-1]] <= today]
            
    return sorted(expire)