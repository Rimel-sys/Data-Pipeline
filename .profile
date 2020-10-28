[ -f "$HOME/.bashrc" ] && source "$HOME/.bashrc"

export JAVA_HOME=$(/usr/libexec/java_home)
export SPARK_HOME=spark-2.4.7-bin-hadoop2.7
export PATH=$SPARK_HOME/bin:$SPARK_HOME/sbin
export PYSPARK_PYTHON=/usr/bin/python3
export PYTHONPATH=$SPARK_HOME/python/lib/py4j-0.10.7-src.zip:$PYTHONPATH
