import pytest
from module import data_class
from module.file_parse import FileHandler

test_file_path = 'test/test_file/test_link_list.csv'

fileHandler_obj = FileHandler(test_file_path)

def test_get_file_list():
    result = fileHandler_obj.get_file_list()
    assert result == 'a'

def test_write_csv():

    # 테스트용 dataclass
    test_news_item = data_class.NewsItem(
        name='test', 
        link='http://www.yakup.com/news/?nid=246818&mode=view', 
        text=' 약업닷컴을 시작페이지로'
    )
    test_news_item_list = data_class.NewsItemList([test_news_item])

    fileHandler_obj.write_csv(news_list=test_news_item_list)
