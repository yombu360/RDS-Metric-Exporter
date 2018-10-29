import time
import random

from prometheus_client import start_http_server
from prometheus_client.core import Gauge, REGISTRY

from Util.ConfigParser import ConfigParser
from Logger.Logger import Logger


a = Gauge("rds_metric", "hello", ["func_name"])

def func1():
    return random.random()


def func2():
    return random.random()

config = ConfigParser("config.yaml").parse_config_file()
Logger.publish_log_info("Started RDS Metric Exporter")
start_http_server(config.get("PrometheusPort"))

while True:
    a.labels(func_name="func1").set(func1())

    a.labels(func_name="func2").set(func2())
