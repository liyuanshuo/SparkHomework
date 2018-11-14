import os
import re
from pyspark.sql import SparkSession

os.environ['PYSPARK_PYTHON'] = '/usr/bin/python3'

if __name__ == "__main__":

    spark = SparkSession.builder.getOrCreate()
    df_array = []
    years = []
    air_quality_data_folder = "/home/liyuanshuo/Downloads/csvs_per_year"
    for file in os.listdir(air_quality_data_folder):
        print(file)
        if '2018' not in file:
            year = re.findall("\d{4}", file)
            years.append(year[0])
            file_path = os.path.join('/liyuanshuo/csvs_per_year/', file)
            df = spark.read.csv(file_path, header="true")
            # print(df.columns)
            df1 = df.withColumn('yyyymm', df['date'].substr(0, 7))
            df_final = df1.filter(df1['yyyymm'].substr(0, 4) == year[0]).groupBy(df1['yyyymm']).agg({'PM10': 'avg'})
            df_array.append(df_final)

    pm10_months = [0] * 12
    # print(range(12))
    for df in df_array:
        for i in range(12):
            rows = df.filter(df['yyyymm'].contains('-'+str(i+1).zfill(2))).first()
            # print(rows[1])
            pm10_months[i] += (rows[1]/12)

    years.sort()
    print(years[0] + ' - ' + years[len(years)-1] + '年，每月平均PM10统计')
    m_index = 1
    for data in pm10_months:
        print(str(m_index).zfill(2) + '月份: ' + '||' * round(data))
        m_index += 1