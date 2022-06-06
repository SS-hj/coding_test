s = input()

ones = [i for i in s.split('0') if i]
zeros = [i for i in s.split('1') if i]

if len(ones) >= len(zeros):
    print(len(zeros))
else:
    print(len(ones))