# 모듈 사용 예제 코드
from config import setting
from module import data_class
from config.logconfig import logger
from module.file_parse import FileHandler
from module.get_body_text import ParsePage

def run():
    """
    input csv경로로 들어온 csv파일을 읽어 (title,link 컬럼을 가지고있음)
    link가 가르키느 페이지의 body에 있는 text를 가져와 특수문자를 제거하고 
    결과를 output csv의 경로로 반환한다.

    input csv 파일과   output csv파일의 경로는 ./config/setting.py 에서 수정할수 있다.
    """

    try:

        # csv파일을 일고 쓰는 객체를 만듬
        file_handller = FileHandler(file_path= setting.SEARCH_FILE_PATH)

        # csv파일을 읽어옴
        csv_row_list = file_handller.get_file_list()
        
        # 파싱된 data_class.NewsItem이 저장될 변수
        item_list = []

        # csv파일의 링크에서 body의 text를 가져옴
        for csv_row in csv_row_list.news_item_list:
            
            
            page_text_obj = ParsePage(news_item = csv_row)
            result_csv_item = page_text_obj.parsing()

            item_list.append(result_csv_item)

        item_list_dataclass = data_class.NewsItemList(item_list)
        file_handller.write_csv(item_list_dataclass)
        
    except Exception as error:
        logger.exception(f"occured {error}")
        


if __name__ == "__main__":
    run()
