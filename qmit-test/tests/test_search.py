import re
import os
from dotenv import load_dotenv
from playwright.sync_api import Page, expect

load_dotenv()
BASE_URL_SEARCH = os.getenv("BASE_URL_SEARCH")

def test_제목_검색(page: Page):
    page.goto(BASE_URL_SEARCH)
    page.get_by_placeholder("제목을 입력해주세요.").fill("자동화")
    page.get_by_placeholder("제목을 입력해주세요.").press("Enter")
    card = page.get_by_test_id("project-list-item")
    expect(card).to_have_count(8) #261114 카드 갯수 8개
    matched_cards = page.get_by_test_id("project-list-item").filter(has_text="자동화")
    expect(matched_cards).to_have_count(8) #모든 카드에 검색어가 들어 있음
	

def test_검색_결과_없음(page: Page):
	page.goto(BASE_URL_SEARCH)
	page.get_by_placeholder("제목을 입력해주세요.").fill("없음")
	page.get_by_placeholder("제목을 입력해주세요.").press("Enter")
	msg = page.get_by_text("찾으시는 프로젝트를 찾지 못했습니다.").first
	card = page.get_by_test_id("project-list-item")
	expect(card).to_have_count(0) #카드가 0개
	expect(msg).to_contain_text("찾으시는 프로젝트를 찾지 못했습니다.") #결과 없음 안내 문구가 보임

def test_진행_중만_보기(page: Page):
	page.goto(BASE_URL_SEARCH)
	switch = page.get_by_role("checkbox")
	switch.check()
	expect(switch).to_be_checked()
	expect(page).to_have_url(re.compile(r"isActvProjYn=Y"))

    # pytest -s --headed tests/test_search.py