from pyspark import SparkContext
import os



os.environ['PYSPARK_PYTHON'] = '/usr/bin/python3'
logFile = "/liyuanshuo/README.md"
sc = SparkContext("local", "Simple App")
logData = sc.textFile(logFile).cache()
numAs = logData.filter(lambda s: 'a' in s).count()
numBs = logData.filter(lambda s: 'b' in s).count()
print("Lines with a: %i,lines with b: %i" % (numAs, numBs))
