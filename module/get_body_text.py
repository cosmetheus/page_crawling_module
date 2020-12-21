import random, time
import re
from module import data_class  
import logging
from fake_useragent import UserAgent

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class ParsePage_Selenium:
    """
    data_class.PageItemList 안의 data_class.PageItem 의 link가 가르키는 페이지를
    selenium으로 접속하여 body 태그내부에 있는 text를 모두 가져온뒤
    특수문자(줄바꿈 포함)를 모두 제거한 문자열을
    data_class.PageItem 의 text에 할당한다
    """
    def __init__(self, page_item_list : data_class.PageItemList, driver_path:str):
        self.page_item_list = page_item_list
        self.driver_path = driver_path


    def get_page_body(self, page_item:data_class.PageItem, driver:webdriver.Firefox, max_try_num:int =3):
        """
            driver가 위치한 페이지 body태그의 html을 가져온뒤
            특수문자(줄바꿈 포함) 를 제가한 text를 반환한다
        """
        
        # 에러가 발생할 경우 try_count 만큼 제시도
        for _ in range(max_try_num):

            try:
                # 페이지 로드가 10초이상 걸리면 timeout 에러를 발생
                driver.set_page_load_timeout(30)

                # page_item.link의 주소로 페이지 이동
                driver.get(page_item.link)
                logging.info(f"search  page : {page_item.link}")

                # body가 로딩될때까지 10토동안 기다린후 body element를 가져옴
                body_web_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "body"))
                )
                
                # innertext 추출
                inner_text = body_web_element.text

                #regex 로 특수문자 제거
                result = re.sub("[^가-힣ㄱ-ㅎ|\ |0-9|a-zA-Z]","",inner_text)


                page_item.text = result
                
                # 제시도 반복문 종료
                break

            except TimeoutException as error:
                page_item.text = 'this page was time out'
                logging.exception(error)
                break

            except Exception as error:
                page_item.text = f"""unexpected error
                page_item:{page_item} """
                logging.exception("""unexpected error""")


    def driver_generator(self):
        """
            webdriver.Firefox를 생성하고 
            self.page_item_list.page_item_list 에 항목 수만큼 self.get_page_body를 실행하는 yield를 생성한다.
            이후 webdriver.Firefox를 종료하는 yield를 생성한다.
        """

        # Firerfox webdriver 생성
        profile = webdriver.FirefoxProfile()
        profile.set_preference("general.useragent.override", UserAgent().random)
        driver = webdriver.Firefox(profile, executable_path = self.driver_path)

        # Firerfox webdriver로 수행할 작업 정의
        for page_item in self.page_item_list.page_item_list:
            yield self.get_page_body(page_item, driver=driver)

        # Firerfox webdriver 종료
        yield driver.quit()


    def get_result(self):
        """text 값이 채워진 list[data_class.PageItem] 를 반환한다

        :return: text 값이 채워진 list[data_class.PageItem]
        :rtype: data_class.PageItemList
        """

        [page for page in self.driver_generator()]

        return self.page_item_list