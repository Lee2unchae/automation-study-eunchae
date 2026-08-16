#2. 성적 처리

#점수 입력받기
scores = []  #점수 리스트 생성

for i in range(5): #for문을 이용해 5개의 점수를 받음
    score = int(input())
    scores.append(score)  #입력받은 점수를 점수 리스트에 추가

#리스트에 저장된 점수 등급 출력
print("등급 출력:")
for score in scores:
    if score >= 90:
        print(score, "A")
    elif score >= 80:
        print(score, "B")
    elif score >= 70:
        print(score, "C")
    else:
        print(score, "D")

#전체 평균 계산
avg = sum(scores)/len(scores)
print("전체 평균:", avg)

#최고점 / 최저점 출력
max_s = max(scores)
min_s = min(scores)
print("최고점:", max_s)
print("최저점:", min_s)

