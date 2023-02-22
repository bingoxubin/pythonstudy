from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("wordcount").getOrCreate()
sc = spark.sparkContext

counts = sc.textFile('E:\\60.test\\test.txt').flatMap(lambda line:line.split(" ")).map(lambda x:(x,1)).reduceByKey(lambda a,b:a+b)
output = counts.collect()
print(output)
sc.stop