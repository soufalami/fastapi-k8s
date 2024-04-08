from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Ejemplo dedice app actividad 3") \
    .master("k8s://https://kubernetes.default.svc.cluster.local") \
    .config("spark.kubernetes.namespace", "virtualizacion") \
    .config("spark.kubernetes.authenticate.driver.serviceAccountName", "spark") \
    .config("spark.executor.instances", "2") \
    .config("spark.kubernetes.container.image", "spark:3.5.1") \
    .config("spark.driver.host", "spark-driver-headless") \
    .config("spark.driver.bindAddress", "0.0.0.0") \
    .config("spark.driver.blockManager.port", "7777") \
    .config("spark.driver.port", "2222") \
    .getOrCreate()

resultados = [random.randint(1, 6) for _ in range(6)]


df = spark.createDataFrame([(r,) for r in resultados], ["resultado"])
df.show()

spark.stop()
