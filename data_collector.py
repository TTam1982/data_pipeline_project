import requests
import pandas as pd

def fetch_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        return df
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None

def process_data(df):
    # Chỉ lấy các cột cần thiết
    processed_df = df[['userId', 'id', 'title', 'body']]
    # Thực hiện các bước xử lý dữ liệu cần thiết khác
    return processed_df 
