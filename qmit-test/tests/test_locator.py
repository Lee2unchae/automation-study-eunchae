import os
import re
import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page, expect

load_dotenv()
BASE_URL = os.getenv("BASE_URL")
QMIT_ID = os.getenv("QMIT_ID")
QMIT_PW = os.getenv("QMIT_PW")

def test_프로젝트_찾기(page: Page):
    page.goto(f"https://v369.dev.l-walk.com/")
    page.get_by_text("프로젝트 찾기").click()

    #카드 갯수
    cards = page.get_by_test_id("project-list-item")
    cards.first.wait_for(state="visible")
    total_count = cards.count()
    expect(cards).to_have_count(total_count)
    print(f"총 카드 갯수 : {total_count}")

    #선정 중인 카드 갯수
    progress_cards = page.get_by_test_id("project-list-item").filter(has_text="선정 진행 중")
    progress_count = progress_cards.count()
    expect(progress_cards).to_have_count(progress_count)
    print(f"선정 중인 카드 갯수 : {progress_count}")

    #비상주와 구분한 상주 필터
    #page.get_by_test_id("btn").filter(has_text=re.compile(r"^상주$")).click()
    page.get_by_text(re.compile(r"^상주$")).first.click()
    reside_cards = page.get_by_test_id("project-list-item")
    reside_count = reside_cards.count()
    expect(reside_cards).to_have_count

    #세번째 카드의 제목
    third_card = page.get_by_test_id("project-list-item").nth(2).locator("p").nth(1).inner_text()
    print(f"세번째 카드 제목 : {third_card}")

    # 세 번째 카드의 제목을 찾을때 순서로 찾게되면 카드가 추가되거나 삭제되면 테스트 결과가 달라질 수 있게 때문입니다.


    # pytest -s --headed tests/test_locator.py
