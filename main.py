# 모듈 사용 예제 코드

from module import data_class
from config.logconfig import logger
from module.file_parse import FileHandler
from module.get_body_text import  ParsePage_Selenium

def run_selenium(
    input_file_path : str,
    output_file_path : str ,
    output_file_name: str,
    geckodriver_path : str, 
):

    """  
    FileHandler로 탐색할 액셀파일의 값을 읽어온뒤 
    액셀 파일에 있는 페이지링크로 패이지를 탐색후 
    body 태그에 있는 텍스트를 모두 가져온다.(갸져온 텍스트는 특수문자(줄바꿈 포함) 이 제거되있음)
    이후 FileHandler를 이용해 저장한다.

    :param input_file_path: 프로그램이 읽어올 링크가 포함된 .xlsx 파일 포멧은 README.md 참조 
    :type input_file_path: str

    :param output_file_path: 결과물이 저장될 파일 경로
    :type output_file_path: str

    :param output_file_name: 결과물 파일의 이름
    :type output_file_name: str

    :param geckodriver_path: geckodriver의 파일 경로 
    :type geckodriver_path: str
    """
    
    # excel 파일을 읽어옴
    excel_sheet = FileHandler.open_excel_file_list(input_file_path, target_sheet_name='아이오페')

    # row들을 dataclass로 변환후 리스트업
    page_item_list = FileHandler.get_sheet_data(excel_sheet)

    # selenium 으로 페이지 파싱
    ParsePage_Selenium(page_item_list = page_item_list, driver_path = geckodriver_path).get_result()

    # 결과 파일생성
    FileHandler.write_csv(file_path = output_file_path ,file_name = output_file_name ,page_item_list= page_item_list)

if __name__ == "__main__":
    run_selenium(
        input_file_path = "prototype_cosmetics.xlsx",
        output_file_path = ".",
        output_file_name = "아이오페",
        geckodriver_path = "config/geckodriver",
    )