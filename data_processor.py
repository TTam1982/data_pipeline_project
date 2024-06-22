def process_data(df):
    # Chỉ lấy các cột cần thiết
    processed_df = df[['userId', 'id', 'title', 'body']]
    # Thực hiện các bước xử lý dữ liệu cần thiết khác
    return processed_df
