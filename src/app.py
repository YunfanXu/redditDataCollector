import pmaw
import datetime as dt
import pandas as pd

api = pmaw.PushshiftAPI()
before = int(dt.datetime(2023, 1, 25, 0, 0).timestamp())
after = int(dt.datetime(2023, 1, 1, 0, 0).timestamp())
subreddit = "wallstreetbets"
size =10
comments = api.search_comments(subreddit=subreddit, size=size, until=before, since=after)
print(f'Retrieved {len(comments)} comments from Pushshift')

comments_df = pd.DataFrame(comments)
comments_df.to_csv('./wsb_comments.csv', header=True, index=False, columns=list(comments_df.axes[1]))