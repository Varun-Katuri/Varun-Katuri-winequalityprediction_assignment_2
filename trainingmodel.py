from pyspark.sql.session import SparkSession
from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext
from pyspark.mllib.linalg import Vectors
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.ml.feature import VectorAssembler
from sklearn.metrics import confusion_matrix
import pandas as pd
from sklearn.metrics import f1_score
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.tree import RandomForest

conf = SparkConf().setAppName('winequalityapplication').setMaster('local')
sc = SparkContext.getOrCreate();
spark = SparkSession(sc)
traindata = spark.read.format("csv").load("TrainingDataset.csv",delimiter=";", inferSchema=True, header=True)


va = VectorAssembler(inputCols=traindata.columns[:11], outputCol="features")

va_df = va.transform(traindata)
data_y = va_df.select("features", '""""quality"""""')
va_df = data_y.withColumnRenamed('""""quality"""""', "label")
va_df = va_df.select(['features', 'label'])

va_df=va_df.rdd.map(lambda row: LabeledPoint(row[-1], Vectors.dense(row[0:-1])))
dtc= RandomForest.trainClassifier(va_df,numClasses=10,categoricalFeaturesInfo={}, numTrees=50, maxBins=64, maxDepth=20, seed=33)
pred = dtc.predict(va_df)
predlabel=va_df.map(lambda x: x.label).zip(pred)
dtc.save(sc,'S3://winequalityapplication/RFModel')