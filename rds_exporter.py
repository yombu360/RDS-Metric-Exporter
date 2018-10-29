import time

from prometheus_client import start_http_server

from Util.ConfigParser import ConfigParser
from Metrics import Metrics
from Logger.Logger import Logger


config = ConfigParser("config.yaml").parse_config_file()
Logger.publish_log_info("Started RDS Metric Exporter on port: {}".format(config.get("PrometheusPort")))

period = config.get("Period")
port   = config.get("PrometheusPort")

start_http_server(port)

while True:
    for db_instance_data in config.get("DBInstances"):
        db_instance_identifier = db_instance_data.get("DBInstanceIdentifier")
        region                 = "us-east-1" if db_instance_data.get("Region") is None or len(db_instance_data.get("Region")) == 0 else db_instance_data.get("Region")
        access_key             = db_instance_data.get("AWSAccessKey")
        secret_access_key      = db_instance_data.get("AWSSecretKey")
        db_engine              = db_instance_data.get("DBEngine")
        availability_zone      = db_instance_data.get("AvailabilityZone")

        db_metric_object = Metrics(period=period,
                                   db_name=db_instance_identifier,
                                   db_engine=db_engine,
                                   availability_zone=availability_zone,
                                   region=region,
                                   access_key=access_key,
                                   secret_access_key=secret_access_key)

        db_metrics = db_metric_object.get_metrics_from_cloud_watch()

        METRICS = db_metric_object.METRICS.get(db_engine)
        LABELS  = db_metric_object.LABELS

        for metric_result in db_metrics.get("MetricDataResults"):
            label = metric_result.get("Label")

            if len(metric_result.get("Values")) > 0:
                gauge = METRICS.get(label)

                gauge.labels(db_name=db_instance_identifier,
                             db_engine=db_engine,
                             az_name=availability_zone).set(metric_result.get("Values")[0])

    time.sleep(60)
