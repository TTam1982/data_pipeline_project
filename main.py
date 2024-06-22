from data_collector import fetch_data
from data_processor import process_data
from sqlalchemy import create_engine

def save_to_db(df, db_url, table_name):
    engine = create_engine(db_url)
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)

if __name__ == "__main__":
    API_URL = "https://jsonplaceholder.typicode.com/posts"
    DB_URL = "sqlite:///data.db"  # Sử dụng SQLite cho đơn giản
    TABLE_NAME = "posts"

    # Thu thập dữ liệu
    data_df = fetch_data(API_URL)
    if data_df is not None:
        print("Fetched Data:")
        print(data_df.head())  # In ra vài dòng đầu tiên của dữ liệu thu thập được

        # Xử lý dữ liệu
        processed_df = process_data(data_df)
        print("Processed Data:")
        print(processed_df.head())  # In ra vài dòng đầu tiên của dữ liệu sau khi xử lý

        # Lưu trữ dữ liệu vào cơ sở dữ liệu
        save_to_db(processed_df, DB_URL, TABLE_NAME)
        print(f"Data saved to {TABLE_NAME} table in database.")
    else:
        print("No data to process and save.")