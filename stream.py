import json
import pyspark
from pyspark import SparkConf
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

from properties import BROKER, TOPIC, DURATION, APPNAME, MASTER


class KafkaStream(object):
    def __init__(self):
        self.sparkConf = SparkConf()
        self.sparkConf.set("spark.driver.allowMultipleContexts", "true")
        self.sparkConf.setAll([
                            ('spark.executor.memory', '2g'),
                           ('spark.executor.cores', '1'),
                           ('spark.cores.max', '24'),
                           ('spark.driver.memory', '5g'),
                           ("spark.master", "spark://127.21.0.4:7070")])

    def get_data(self, data):
        dataframe = spark.createDataFrame([data])
        return dataframe

    def add_data(self, data):
        dataframe = data
        avgColumns1 = [col(dataframe.select('boom_lift')), col(dataframe.select('boom_lower'))]
        avgColumns2 = [col(dataframe.select('boom_forward')), col(dataframe.select('boom_backward'))]
        avgColumns3 = [col(dataframe.select('drill_boom_turn_left')), col(dataframe.select('drill_boom_turn_right'))]
        avgColumns4 = [col(dataframe.select('drill_boom_turn_forward')), col(dataframe.select('drill_boom_turn_backward'))]
        avgColumns5 = [col(dataframe.select('beam_left')), col(dataframe.select('beam_right'))]

        averageFunc1 = sum(x for x in avgColumns1)/len(avgColumns1)
        averageFunc2 = sum(x for x in avgColumns2)/len(avgColumns2)
        averageFunc3 = sum(x for x in avgColumns3)/len(avgColumns3)
        averageFunc4 = sum(x for x in avgColumns4)/len(avgColumns4)
        averageFunc5 = sum(x for x in avgColumns5)/len(avgColumns5)

        dataframe.withColumn('boom_long', averageFunc1).show(truncate=False)
        dataframe.withColumn('boom_lati', averageFunc2).show(truncate=False)
        dataframe.withColumn('drill_boom_long', averageFunc3).show(truncate=False)
        dataframe.withColumn('drill_boom_lati', averageFunc4).show(truncate=False)
        dataframe.withColumn('beam', averageFunc5).show(truncate=False)
        dataframe.withColumn('boom_lati', averageFunc2).show(truncate=False)
        return dataframe

    def select_data(self, data):
        dataframe = data
        dataframe.select('engine_speed', 'hydraulic_drive_off',
            'drill_boom_in_anchor_position', 'pvalve_drill_forward', 'bolt',
            'boom_long', 'boom_lati', 'drill_boom_long', 'drill_boom_lati', 'beam')
        return dataframe

    def fill_missing_values(self, data):
        return data.na.fill(0)

    def scale_data(self, data):
        scaler = StandardScaler(inputCol="features", outputCol="scaledFeatures",
                                withStd=True, withMean=False)
        scalerModel = scaler.fit(data)
        dataframe = scalerModel.transform(data)
        return dataframe

    def start_stream(self):
        spark_context = SparkContext(appName=APPNAME, conf=self.sparkConf)
        stream_context = StreamingContext(spark_context, batchDuration=DURATION)
        data_stream = KafkaUtils.createDirectStream(stream_context, topics=[TOPIC],
                                                    kafkaParams={"metadata.broker.list": BROKER})
        # Stream data_stream with Spark
        data_stream = self.get_data(data_stream)
        # Add new avgColumns
        data_stream = self.add_data(data_stream)
        # Fill missing values with zero
        data_stream = self.fill_missing_values(data_stream)
        # Scale data
        data_stream = self.scale_data(data_stream)

        data_stream.pprint()
        stream_context.start()
        stream_context.awaitTermination()


if __name__ == '__main__':
    stream_kafka = KafkaStream()
    stream_kafka.start_stream()
