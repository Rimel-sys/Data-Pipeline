import joblib
import warnings
import happybase
from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.streaming import StreamingContext

from properties import BROKER, HOSTNAME


def predict_result():
    sc = SparkContext(BROKER, "NetworkWordCount")
    ssc = StreamingContext(sc, 1)
    with warnings.catch_warnings():
          warnings.simplefilter("ignore", category=UserWarning)
          warnings.simplefilter("ignore", category=FutureWarning)
          estimator = joblib.load('model.pkl')

    columns = list(ssc.columns.values)[:-1]
    predicted_data = ssc.Series(estimator.predict(ssc[columns]))
    return predicted_data


def store_data():
    sc = SparkContext()
    sqlc = SQLContext(sc)


    connection = happybase.Connection(HOSTNAME)
    connection.open()
    connection.create_table(
    'SPEED',
    {'timestamp': int(),
     'average_speeds': int()),
    })
    connection.create_table(
    'ACTIVITY',
    {'start timestamp': int(),
     'end timestamp': int()),
     'duration': int(),
     'type': int()),
    })

    data_source_format = 'org.apache.hadoop.hbase.spark'

if __name__ == '__main__':
    predict_result()
    store_data()
