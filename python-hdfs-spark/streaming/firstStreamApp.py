from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from time import sleep
try:
    # Create a local StreamingContext with two working thread and batch interval of 1 second
    sc = SparkContext("local[2]", "NetworkWordCount")
    ssc = StreamingContext(sc, 1)
    sc.setLogLevel("ERROR")

    # Create a DStream that will connect to hostname:port, like localhost:9999
    lines = ssc.socketTextStream("localhost", 9999)

    # Split each line into words
    words = lines.flatMap(lambda line: line.split(" "))

    # Count each word in each batch
    pairs = words.map(lambda word: (word, 1))
    wordCounts = pairs.reduceByKey(lambda x, y: x + y)

    # Print the first ten elements of each RDD generated in this DStream to the console
    wordCounts.pprint()

    ssc.start()             # Start the computation

    sleep(5)
    ssc.awaitTermination()  # Wait for the computation to terminate
    #ssc.stop(stopSparkContext=True,stopGraceFully=True)
except:
    pass