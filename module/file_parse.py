# 파일 형식 분석
# 해당 파일 내용 리스트업 
import csv
import os
import logging
import dataclasses
import openpyxl
from openpyxl import load_workbook
from module import data_class



class FileHandler:
    @classmethod
    def open_excel_file_list(cls, file_path:str) -> openpyxl.worksheet._read_only.ReadOnlyWorksheet:
        """
        openpyxl 라이브러리를 사용하여
        self.file_path 경로의 excel 파일을 읽어 openpyxl 객체를 생성후
        self.excel_sheet에 할당
        """

        file_type = os.path.splitext(file_path)[-1]

        if file_type == '.xlsx':

            excle_file = load_workbook(file_path, read_only=True)
            sheet = excle_file.active
            
            return sheet
        
        else:
            # 파일 타입이 .xlsx 가 아닐겨우 
            raise TypeError('chack file_path file type / this program suport .xlsx file')
    
    
    @classmethod
    def get_sheet_data(cls, excel_sheet:openpyxl.worksheet._read_only.ReadOnlyWorksheet) -> data_class.PageItemList:
        """
        openpyxl.worksheet._read_only.ReadOnlyWorksheet 객체를 읽어 링크데이터들 을 
        data_class.NewsItemList객체로 만들어 반환
        """

        # slef.sheet를 row의 배열로 만든다 (가장 상위 row는 column name 임으로 제외 
        row_list = list(excel_sheet)[1:]
        

        # input.xlsx column을 data_class.PageItem객체로 만들어 저장
        page_item_list = []
        
        # input.xlsx columns
        # article_type [0]
        # brand [1]
        # title [2]
        # date [3]
        # link [4]

        for row in row_list:
            page_item = data_class.PageItem(
                article_type = row[0].value,
                brand = [i.strip() for i in  row[1].value.split(',')],
                title = row[2].value,
                published_at = row[3].value,
                link = row[4].value
            )
            page_item_list.append(page_item)

        logging.info(f"load {len(page_item_list)} csv row")

        return data_class.PageItemList(page_item_list)
    

    @classmethod
    def write_csv(cls, file_path:str,file_name:str ,page_item_list: data_class.PageItemList):
        
        with open(f"{file_path}/{file_name}.csv", 'w', encoding='utf-8') as csv_file:
            # csv파일의 첫번째 row에 들어갈 컬럼 이름을 정의
            csv_columns = ['link','text']
            
            # 컬럼 이름이 정의된 csv 파일 객체를 생성
            writer = csv.DictWriter(csv_file, fieldnames=csv_columns)

            # csv 파일의 row를 생성
            writer.writeheader()
            for news_item in page_item_list.page_item_list:
                
                writer.writerow(news_item.get_row())
        
        logging.info(f"create file : {file_path}/{file_name}.csv")
            