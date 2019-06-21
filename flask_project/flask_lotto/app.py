from flask import Flask, render_template, request
import requests
import json
import random

app = Flask(__name__)

@app.route('/lotto_check')
def lotto_check():
    return render_template('lotto_check.html')

@app.route('/lotto_result')
def lotto_result():
    lotto_round = request.args.get('lotto_round')
    response = requests.get(f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=860')
    lotto = response.json()
    # winner = []
    # for i in range(1, 7):
    #     winner.append(lotto[f'drwNo{i}'])
    # list comprehension 위 3세줄과 같음
    winner = [lotto[f'drwtNo{i}'] for i in range(1, 7)]

    # 내 번호 리스트 만들기
    # my_lotto = random.sample(list(range(1, 46)), 7)

    my_lotto = []
    for i in range(1, 7):
        my_lotto.append(int(request.args.get(f'my_lotto{i}')))

    # 내 번호를 lotton_check 에서 입력 받는 6개 번호로 만들기
    # 당첨번호와의 교집합

    cnt = 0
    bonus = False
    for my_num in my_lotto:
        if my_num in winner:
            cnt += 1
    if lotto["bnusNo"] in my_lotto:
        bonus = True

    if cnt < 3:
        rank = '꽝'
    elif cnt == 3:
        rank = '5등'
    elif cnt == 4:
        rank = '4등'
    elif cnt == 5:
        if bonus:
            rank = '2등'
        else:
            rank = '3등'
    else:
        rank = '1등'
    my_lotto.sort()

    # 조건에 따라 1등부터 꽝까지 결과값을 lotto_result로 보내준다.
    return render_template('lotto_result.html', lotto_round=lotto_round, winner=f'{winner} + {lotto["bnusNo"]}', rank=rank, my_lotto=my_lotto)

if __name__ == '__main__':
    app.run(debug=True)