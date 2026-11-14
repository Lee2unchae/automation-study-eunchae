import os
from dotenv import load_dotenv  
from playwright.sync_api import Page, expect

load_dotenv()
BASE_URL = os.getenv("BASE_URL")
BASE_URL_LOGIN = os.getenv("BASE_URL_LOGIN")
QMIT_ID = os.getenv("QMIT_ID")      
QMIT_PW = os.getenv("QMIT_PW")       

def 로그인(page: Page, 이메일, 비밀번호):
	# 로그인 페이지 접속
	page.goto(BASE_URL_LOGIN)
	page.get_by_placeholder("이메일을 입력해주세요.").fill(이메일)
	page.get_by_placeholder("비밀번호를 입력해주세요.").fill(비밀번호)
	page.get_by_role("button", name="로그인 하기").click()
	
def test_로그인_성공(page: Page):
	로그인(page, QMIT_ID, QMIT_PW)
	expect(page).to_have_url(f"{BASE_URL}/")
	expect(page.get_by_role("button", name="마이페이지")).to_be_visible()
	
def test_틀린_비밀번호(page: Page):
	로그인(page, QMIT_ID, "wrongpass1234!")
	expect(page.get_by_text("비밀번호가 올바르지 않습니다. 다시 한번 확인해주세요.")).to_have_text("비밀번호가 올바르지 않습니다. 다시 한번 확인해주세요.")
	expect(page).to_have_url(BASE_URL_LOGIN)
	
def test_가입하지_않은_이메일(page: Page):
	로그인(page, "qa@l-walk.com", "wrongpass1234!")
	msg = page.get_by_text("이메일이 올바르지 않습니다. 다시 한번 확인해주세요.")
	expect(msg).to_have_text("이메일이 올바르지 않습니다. 다시 한번 확인해주세요.") #오류 창 문구가 화면 문구와 같은지
	
def test_이메일_형식_오류(page: Page):
    page.goto(BASE_URL_LOGIN)
    msg = page.get_by_text("이메일이 올바르지 않습니다. 다시 한번 확인해주세요.") 
    expect(msg).to_be_hidden() #누르기 전: 형식 안내 문구가 숨어 있음
    page.get_by_placeholder("이메일을 입력해주세요.").fill("qal-walkcom")
    page.get_by_placeholder("비밀번호를 입력해주세요.").fill("wrongpass1234!")
    page.get_by_role("button", name="로그인 하기").click()
    expect(msg).to_be_visible() #누른 뒤: 형식 안내 문구가 보임

def test_로그인_버튼_활성화(page: Page):
	page.goto(BASE_URL_LOGIN)
	expect(page.get_by_role("button", name="로그인 하기")).to_be_disabled() #아무것도 입력하지 않음 (비활성)
	page.get_by_placeholder("이메일을 입력해주세요.").fill(QMIT_ID)
	expect(page.get_by_role("button", name="로그인 하기")).to_be_disabled() #이메일만 (비활성)
	page.get_by_placeholder("비밀번호를 입력해주세요.").fill(QMIT_PW)
	expect(page.get_by_role("button", name="로그인 하기")).to_be_enabled() #이메일, 비밀번호 입력 (활성)

def test_로그아웃(page: Page):
	로그인(page, QMIT_ID, QMIT_PW)
	page.get_by_role("button", name="마이페이지").click()
	page.get_by_role("button", name="로그아웃").click()
	expect(page.get_by_role("button", name="로그인", exact=True)).to_be_visible()


    # pytest -s --headed tests/test_login.py