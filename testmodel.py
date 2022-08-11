from pyspark.sql.session import SparkSession
from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext
import pandas as pd
from pyspark.mllib.evaluation import MulticlassMetrics
from pyspark.mllib.tree import RandomForestModel
from sklearn.metrics import accuracy_score, f1_score

sc = SparkContext.getOrCreate();

spark = SparkSession(sc)

traindata = spark.read.format("csv").load(sc,"S3://winequalityapplication/ValidationDataset.csv",delimiter=";", inferSchema=True, header=True)

da_df= traindata.rdd.map(lambda row: LabeledPoint(row[-1], Vectors.dense(row[0:-1])))

Rfm = RandomForestModel.load(sc,'S3://winequalityapplication/RFModel')

predictions = Rfm.predict(da_df.map(lambda lp: lp.features))

labelandPredictions = (da_df.map(lambda lp: lp.label).zip(predictions)).toDF(["label", "Prediction"])

lp_df = labelandPredictions.toPandas()

print("Accuracy Measure: ", accuracy_score(lp_df['label'], lp_df['Prediction']))
print("F1 Measure: ", f1_score(lp_df['label'], lp_df['Prediction'], average='micro'))