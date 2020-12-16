# 파일 형식 분석
# 해당 파일 내용 리스트업 
import csv
import os

import dataclasses
from config import setting
from module import data_class
from config.logconfig import logger 


class FileHandler:
    def __init__(self, file_path:str):
        self.file_path = file_path
        self.file_type = os.path.splitext(file_path)[-1]
        self.file_name = os.path.splitext(file_path)[0].split("/")[-1]

    def get_file_list(self) -> data_class.NewsItemList:
        """
        self.file_type 에 따라 self.file_path의 파일분석후 파일정보로 data_class.NewsItem 객체를 생성한다.
        """

        with open(self.file_path, 'r', encoding='utf-8') as csv_file:        
            csv_list =  list(csv.reader(csv_file))
            
        csv_news_list = []

        for csv_news in csv_list[1:]:

            # csv_news[0] : news name
            # csv_news[1] : news link
            news_item = data_class.NewsItem(
                name= csv_news[0],
                link= csv_news[1]
                )

            csv_news_list.append(news_item)

        logger.info("load {len(csv_news_list)} csv row")

        return data_class.NewsItemList(csv_news_list)

    def write_csv(self, news_list: data_class.NewsItemList):
        
        with open(f"{setting.SAVE_FILE_PATH}/{self.file_name}_string.csv", 'w', encoding='utf-8') as csv_file:
            # csv파일의 첫번째 row에 들어갈 컬럼 이름을 정의
            csv_columns = ['name','link','text']
            
            # 컬럼 이름이 정의된 csv 파일 객체를 생성
            writer = csv.DictWriter(csv_file, fieldnames=csv_columns)

            # csv 파일의 row를 생성
            writer.writeheader()
            for news_item in news_list.news_item_list:
                
                writer.writerow(dataclasses.asdict(news_item))
        
        logger.info(f"create file : {setting.SAVE_FILE_PATH}/{self.file_name}_string.csv")
            