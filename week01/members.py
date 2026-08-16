#3. 회원 정보 관리
 
#회원 3명의 정보
members = [
    {"name": "이은채", "age": 26, "region": "서울"},
    {"name": "홍길동", "age": 32, "region": "부산"},
    {"name": "성심당", "age": 22, "region": "대전"}
]
# 전체 회원 출력하기
print("전체 회원 정보 출력")
for member in members:
    print("이름:", member["name"], "나이:", member["age"], "지역:", member["region"])

# 30세 이상 회원만 별도로 출력
for member in members:
    if member["age"] >= 30:  # 나이 비교
        print("30세 이상 회원:", member["name"])