import os
import calendar
import time
import datetime
from pandas.tseries.offsets import DateOffset
import pandas as pd

def fetchDataByKeyword(keyword = 'fastFashion'):
   
    # end_date = pd.Timestamp(2023, 4, 8, 12)
    diff_days = pd.date_range(start="2020-01-01 00:00:00", end="2023-04-08 00:00:00")

    scrape_option = 'reddit-search'
    directory = "../dataForSearchKeyword/"+scrape_option+'_'+keyword

    errorData = []
    # Check if the directory exists
    if not os.path.exists(directory):
        # If it doesn't exist, create it
        os.makedirs(directory)

    for  startTime in diff_days:
        output_file_name = keyword+"_"+startTime.strftime('%Y%m%d')

        print("Processing:", output_file_name)
        
        start_timestamp = (int)(pd.Timestamp(startTime).timestamp())
        end_timestamp = (int)(pd.Timestamp(startTime + DateOffset(days=1)).timestamp())


        if os.system("snscrape --jsonl %s %s --after %s --before %s >%s/%s.txt" %(scrape_option,keyword, start_timestamp,end_timestamp, directory, output_file_name)) != 0:
            errorData.append("snscrape --jsonl %s %s --after %s --before %s >%s/%s.txt" %(scrape_option,keyword, start_timestamp,end_timestamp, directory, output_file_name))
    print(errorData)
    return errorData


if __name__ == "__main__":
    keywordsList = ["fastFashion", "fast-fashion", "fastfashion", "fashionIndustry", "fashionindustry", "cheapfashion", "cheapFashion", "sustainablefashion", "sustainableFashion", "ecofashion", "ethicalfashion", "eco-friendlyFashion", "slowfashion", "greenfashion", "organicfashion", "fairfashion", "recycledfashion"]
    for keyword in keywordsList:
        fetchDataByKeyword(keyword=keyword)

