FROM python:3.10
RUN apt-get update && \
    apt-get install -y openjdk-11-jre-headless && \
    apt-get clean;
RUN  pip install numpy 
RUN  pip install pandas 
RUN  pip install sklearn
RUN  pip install pyspark



RUN mkdir /winequalityapplication
COPY testmodel.py /winequalityapplication/
COPY ValidationDataset.csv /winequalityapplication/
COPY TrainingDataset.csv /winequalityapplication/
COPY RFModel /winequalityapplication/




ENTRYPOINT ["spark-submit","winequalityapplication/testmodel.py"]