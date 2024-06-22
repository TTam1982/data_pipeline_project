import requests
import pandas as pd

# fetch data from an url
def fetch_data_from_url(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        return df
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None

# fetch data from an excel file
def fetch_data_from_excel(excel_file=None):
    df = pd.read_excel(excel_file)
    return df

