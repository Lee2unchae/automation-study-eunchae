import json
from datetime import datetime

#메모 불러오기
def load_memo():
    try:
        with open("memos.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return [] #파일이 없으면 빈 리스트로 시작   
    except json.JSONDecodeError:
        return []  # 파일 손상 시 예외 처리
    except Exception as e:
        return []  # 혹시 모를 기타 예외 처리

#메모 저장하기
def save_memo(memos):
    try:
        with open("memos.json", "w", encoding="utf-8") as f:
            json.dump(memos, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print("저장 중 오류 발생")

#메모 기능 구현
def main():
    memos = load_memo()

    while True:
        print("<메모 관리 프로그램>")
        print("1. 메모 추가")
        print("2. 전체 메모 조회")
        print("3. 메모 검색")
        print("4. 프로그램 종료")
        print("원하는 기능의 번호를 입력하세요")

        a = input()

        #1. 메모 추가
        if a == "1":
            print("추가할 메모를 입력하세요")
            add_memo = input()
            if add_memo:
                # id : 기존 메모가 있으면 최대 id + 1, 없으면 1
                memo_id = max([m["id"] for m in memos], default=0) + 1 if memos else 1
                # 작성일 생성
                created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # 식별값, 내용, 작성일을 딕셔너리로 저장
                memo_data = {
                    "id": memo_id,
                    "content": add_memo,
                    "created": created
                }

                memos.append(memo_data)
                save_memo(memos)
                print("메모 저장 완료")
            else:
                print("빈 메모는 저장할 수 없습니다.")

        #2. 전체 메모 조회
        elif a == "2":
            if not memos:
                print("저장된 메모 없음")
            else:
                print("전체 메모 조회")
                for i, memo in enumerate(memos, 1):
                    # 딕셔너리 또는 기존 문자열 형식 모두 대응하여 출력
                    if isinstance(memo, dict):
                        print(f"{memo['id']} {memo['content']} {memo['created']}")
                    else:
                        print(memo)

        #3. 메모 검색
        elif a == "3":
            if not memos:
                print("저장된 메모 없음")
            else:
                print("검색할 메모를 입력하세요")
                search = input()
                found = False

                for index, memo in enumerate(memos, 1):
                    memo_text = memo["content"] if isinstance(memo, dict) else memo

                    if search.lower() in memo_text.lower():
                        if not found:
                            print("검색 결과")
                        if isinstance(memo, dict):
                            print(f"{memo['id']} {memo['content']} {memo['created']}")
                        else:
                            print(memo)
                        found = True  # 검색 결과를 찾았으므로 True로 변경
                
                # 일치하는 메모가 없는 경우
                if not found:
                    print("검색 결과가 없습니다.")

        #4. 프로그램 종료
        elif a == "4":
            print("프로그램을 종료합니다.")
            break

        # 예외 (1~4 이외의 숫자 입력)  
        else:
            print("잘못된 입력입니다. 기능 번호를 확인해주세요.")

main()