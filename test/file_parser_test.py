import pytest
from module import data_class
from module.file_parse import FileHandler




test_file_path = 'prototype_cosmetics.xlsx'



def test_open_excel_file_list():

    """file_path 에 있는 엑셀파일을 읽어 target_sheet_name 의 이름을 가진 시트의 row개수를 출력"""

    sheet = FileHandler.open_excel_file_list(file_path= test_file_path, target_sheet_name= '설화수')
    result = FileHandler.get_sheet_data(sheet)
    assert len(result.page_item_list) == 'a'