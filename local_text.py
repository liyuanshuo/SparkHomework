import os


air_quality_data_folder = "hdfs://liyuanshuo:9000/liyuanshuo/csvs_per_year"
for file in os.listdir(air_quality_data_folder):
    print(file)