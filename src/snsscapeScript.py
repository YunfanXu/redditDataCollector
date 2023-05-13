import os
import calendar
import time
import datetime

start  = 0
end = 522

for i in range(start,end):
    start_date = (str)(datetime.date.today() - datetime.timedelta(weeks=i + 1))
    end_date = (str)(datetime.date.today() - datetime.timedelta(weeks=i))

    scrape_option = 'reddit-subreddit'
    subreddit = 'sustainablefashion'
    output_file_name = subreddit+"_"+start_date+"_"+end_date
    print("Processing:", output_file_name)
    start_timestamp = (int)(time.mktime(time.strptime(start_date +' 00:00:00', '%Y-%m-%d %H:%M:%S')))

    end_timestamp = (int)(time.mktime(time.strptime(end_date +' 00:00:00', '%Y-%m-%d %H:%M:%S')))

    os.system("snscrape --jsonl %s %s --after %s --before %s >../sustainablefashion/%s.txt" %(scrape_option,subreddit, start_timestamp,end_timestamp, output_file_name))
    time.sleep(10)


