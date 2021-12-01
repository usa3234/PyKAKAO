
import os
import json
import requests 
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select

def sendMessage(text):

    header = {"Authorization": 'Bearer ' + KAKAO_TOKEN}
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send" #나에게 보내기 주소
    post = {
        "object_type": "text",
        "text": text,
        "link": {
            "web_url": "https://developers.kakao.com",
            "mobile_web_url": "https://developers.kakao.com"
        },
        "button_title": "바로 확인"
    }

    data = {"template_object": json.dumps(post)}
    return requests.post(url, headers=header, data=data, verify=False) 

if __name__ == "__main__":

    driver_path = "E:/chromedriver.exe"
    url = "https://www.ketep.re.kr/businessAcment/businessAcmentList.do?srch_menu_nix=aIDGohUo"

    browser = webdriver.Chrome(executable_path=driver_path)
    # 웹 자원 로드를 위해 3초까지 기다린다.
    browser.implicitly_wait(1)

    browser.get(url)

    selectInfo = Select(browser.find_element_by_id('subj_dmsy_tc'))
    selectStatus = Select(browser.find_element_by_id('status'))

    # select by value 
    #selectInfo.select_by_value('과제')
    selectStatus.select_by_value('ING')

    browser.find_element_by_css_selector('[class="btn btn-md btn-1st"]').click()

    # page 변수에 url 주소 저장
    page = browser.page_source  
    browser.quit()
    
    soup = BeautifulSoup(page, "html.parser")
    msgList = []
    key = soup.find_all(class_="ellipsis")
    for a in key:
        res = a.find("span")
        msgList.append(res["title"])
        #msg += res["title"]
       
        #print(title)
    #text = "나에게 보내는 카톡("+os.path.basename(__file__).replace(".py", ")")
    text = "\n".join(msgList)
    print(text)
    KAKAO_TOKEN = '토큰넘버'
    print(sendMessage(text).text)
