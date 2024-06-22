def process_data_from_url(df):
    # Chỉ lấy các cột cần thiết
    processed_df = df[['userId', 'id', 'title', 'body']]
    # Thực hiện các bước xử lý dữ liệu cần thiết khác
    return processed_df

def process_data_from_excel(df):
    # Không cần thực hiện thêm xử lý nào, chỉ trả về dataframe ban đầu
    return df

