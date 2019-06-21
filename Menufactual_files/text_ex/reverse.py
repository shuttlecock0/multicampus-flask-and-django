# line을 불러오기
# 뒤집기
# 다시 작성하기

lines = None
with open('number.txt', 'r') as f:
    lines = f.readlines()

lines.reverse()

with open('number.txt', 'w') as f:
    for line in lines:
        f.write(line)
