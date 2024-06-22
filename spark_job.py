from pyspark.sql import SparkSession
import os

# Đường dẫn đến tệp CSV
SOURCE_CSV_FILE = os.path.abspath("./datasets/dataset-for-bank-loan-prediction.csv")

# Kiểm tra tệp có tồn tại không
if not os.path.isfile(SOURCE_CSV_FILE):
    raise FileNotFoundError(f"Tệp {SOURCE_CSV_FILE} không tồn tại.")

# Khởi tạo Spark Session
spark = SparkSession.builder \
    .appName("DataPipelineProject") \
    .getOrCreate()

# Đọc dữ liệu từ tệp CSV
try:
    df = spark.read.csv(SOURCE_CSV_FILE, header=True, inferSchema=True)
except Exception as e:
    print("Đã xảy ra lỗi khi đọc tệp CSV:", e)
    spark.stop()
    raise e

# Hiển thị vài dòng dữ liệu đầu tiên để kiểm tra
df.show()

# Thực hiện một số thao tác xử lý dữ liệu
df_filtered = df.filter(df["Credit Score"].isNotNull())

# Hiển thị dữ liệu đã được lọc
df_filtered.show()

# Đường dẫn lưu kết quả
OUTPUT_CSV_FILE = os.path.abspath("./datasets/dataset-for-bank-loan-prediction_filtered_cs.csv")

# Lưu dữ liệu đã được xử lý vào tệp CSV
df_filtered.write.csv(OUTPUT_CSV_FILE, header=True, mode="overwrite")

# Dừng Spark Session
spark.stop()
