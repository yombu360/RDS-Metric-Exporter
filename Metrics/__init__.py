# https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MonitoringOverview.html#monitoring-cloudwatch
# https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Monitoring.html
from datetime import datetime, timedelta

import boto3
from prometheus_client import Gauge

from Logger.Logger import Logger


class Metrics:
    NAMESPACE = "AWS/RDS"

    LABELS = [
        "db_name",
        "db_engine",
        "az_name"
    ]

    METRICS = {
        "basic": {
            "maria": {
                "WriteLatency"                 : Gauge("rds_exporter_maria_write_latency_seconds", "The average amount of time taken per disk I/O operation", LABELS),
                "ReadLatency"                  : Gauge("rds_exporter_maria_read_latency_seconds", "The average amount of time taken per disk I/O operation", LABELS),
                "WriteIOPS"                    : Gauge("rds_exporter_maria_write_IOPS_per_second", "The average number of disk write I/O operations per second", LABELS),
                "ReadIOPS"                     : Gauge("rds_exporter_maria_read_IOPS_per_second", "The average number of disk read I/O operations per second", LABELS),
                "ReadThroughput"               : Gauge("rds_exporter_maria_read_throughput_bytes_per_second", "The average number of bytes read from disk per second", LABELS),
                "WriteThroughput"              : Gauge("rds_exporter_maria_write_throughput_bytes_per_second", "The average number of bytes written to disk per second", LABELS),
                "CPUCreditBalance"             : Gauge("rds_exporter_maria_cpu_credit_count", "CPU credit count", LABELS),
                "BurstBalance"                 : Gauge("rds_exporter_maria_burst_balance_percent", "The percent of General Purpose SSD (gp2) burst-bucket I/O credits available", LABELS),
                "NetworkTransmitThroughput"    : Gauge("rds_exporter_maria_network_transmit_throughput_bytes_per_second", "Network transmission throughput", LABELS),
                "NetworkReceiveThroughput"     : Gauge("rds_exporter_maria_network_receive_throughput_bytes_per_second", "Network receive throughput", LABELS),
                "FreeStorageSpace"             : Gauge("rds_exporter_maria_free_space_bytes", "The amount of available storage space", LABELS),
                "DiskQueueDepth"               : Gauge("rds_exporter_maria_disk_queue_depth_count", "The number of outstanding IOs (read/write requests) waiting to access the disk.", LABELS),
                "CPUUtilization"               : Gauge("rds_exporter_maria_cpu_utilization_percent", "The percentage of CPU utilization", LABELS),
                "DatabaseConnections"          : Gauge("rds_exporter_maria_database_connections_count", "The number of database connections in use", LABELS),
                "SwapUsage"                    : Gauge("rds_exporter_maria_swap_usage_bytes", "The amount of swap space used on the DB instance", LABELS),
                "FreeableMemory"               : Gauge("rds_exporter_maria_freeable_memory_bytes", "Available RAM", LABELS),
                "BinLogDiskUsage"              : Gauge("rds_exporter_maria_binlog_disk_usage_bytes", "The amount of disk space occupied by binary logs on the master", LABELS)
            },

            "aurora": {
                "Queries"                       : Gauge("rds_exporter_aurora_queries_per_second", "The average number of queries executed per second", LABELS),
                "Deadlocks"                     : Gauge("rds_exporter_aurora_deadlock_per_second", "The average number of deadlocks in the database per second", LABELS),
                "DeleteLatency"                 : Gauge("rds_exporter_aurora_delete_latency_milliseconds", "The amount of latency for delete queries", LABELS),
                "DeleteThroughput"              : Gauge("rds_exporter_aurora_delete_throughput_per_second", "The average number of delete queries per second", LABELS),
                "DMLThroughput"                 : Gauge("rds_exporter_aurora_dml_throughput_per_second", "The average number of inserts, updates, and deletes per second", LABELS),
                "CommitLatency"                 : Gauge("rds_exporter_aurora_commit_latency_milliseconds", "The amount of latency for commit queries", LABELS),
                "CommitThroughput"              : Gauge("rds_exporter_aurora_commit_throughput_per_second", "The average number of commit queries per second", LABELS),
                "BlockedTransactions"           : Gauge("rds_exporter_aurora_blocked_transaction_per_second", "The average number of transactions in the database that are blocked per second", LABELS),
                "SelectThroughput"              : Gauge("rds_exporter_aurora_select_throughput_per_second", "The average number of select queries per second", LABELS),
                "SelectLatency"                 : Gauge("rds_exporter_aurora_select_latency_milliseconds", "The amount of latency select requests", LABELS),
                "DDLLatency"                    : Gauge("rds_exporter_aurora_ddl_latency_milliseconds", "The amount of latency for data definition language (DDL) requests", LABELS),
                "NetworkTransmitThroughput"     : Gauge("rds_exporter_aurora_network_transmit_throughput_bytes_per_second", "Network transmission throughput", LABELS),
                "ActiveTransactions"            : Gauge("rds_exporter_aurora_active_transactions_per_second", "The average number of current transactions executing on an Aurora database instance per second", LABELS),
                "EngineUptime"                  : Gauge("rds_exporter_aurora_engine_uptime_seconds", "The amount of time that the instance has been running", LABELS),
                "CPUUtilization"                : Gauge("rds_exporter_aurora_cpu_utilization_percent", "The percentage of CPU utilization", LABELS),
                "DMLLatency"                    : Gauge("rds_exporter_aurora_dml_latency_milliseconds", "The amount of latency for data manipulation language (DDL) requests", LABELS),
                "DatabaseConnections"           : Gauge("rds_exporter_aurora_database_connections_count", "The number of database connections in use", LABELS),
                "FreeableMemory"                : Gauge("rds_exporter_aurora_freeable_memory_bytes", "Available RAM", LABELS),
                "DDLThroughput"                 : Gauge("rds_exporter_aurora_ddl_throughput_per_second", "The average number of inserts, updates, and deletes per second", LABELS),
                "InsertLatency"                 : Gauge("rds_exporter_aurora_insert_latency_milliseconds", "The amount of latency insert requests", LABELS),
                "LoginFailures"                 : Gauge("rds_exporter_aurora_login_failures_per_second", "The average number of failed login attempts per second", LABELS),
                "FreeLocalStorage"              : Gauge("rds_exporter_aurora_free_local_storage_bytes", "The amount of storage available for temporary tables and logs", LABELS),
                "CPUCreditBalance"              : Gauge("rds_exporter_aurora_cpu_credit_count", "CPU credit count", LABELS),
                "NetworkReceiveThroughput"      : Gauge("rds_exporter_aurora_network_receive_throughput_bytes_per_second", "Network receive throughput", LABELS),
                "UpdateLatency"                 : Gauge("rds_exporter_aurora_update_latency_milliseconds", "The amount of latency update requests", LABELS),
                "UpdateThroughput"              : Gauge("rds_exporter_aurora_update_throughput_per_second", "The average number of update queries per second", LABELS),
                "AuroraReplicaLagMinimum"       : Gauge("rds_exporter_aurora_replica_lag_minimum_milliseconds", "The minimum amount of lag between the primary instance and each Aurora DB instance in the DB cluster", LABELS),
                "AuroraReplicaLagMaximum"       : Gauge("rds_exporter_aurora_replica_lag_maximum_milliseconds", "The maximum amount of lag between the primary instance and each Aurora DB instance in the DB cluster", LABELS),
                "AuroraReplicaLag"              : Gauge("rds_exporter_aurora_replica_lag_milliseconds", "The amount of lag when replicating updates from the primary instance", LABELS),
                "AuroraBinlogReplicaLag"        : Gauge("rds_exporter_aurora_bin_log_replica_lag_seconds", "The amount of time a replica DB cluster running on Aurora with MySQL compatibility lags behind the source DB cluster", LABELS)
            }
        }
    }

    def __init__(self, period, db_name, db_engine, availability_zone, monitoring_type, region="us-east-1", access_key=None, secret_access_key=None):
        """

        :param period: Time period of metrics in seconds
        :param db_name: Name of DB instance
        :param db_engine: Name of DB engine
        :param availability_zone: Name of the AZ, For example, us-east-1d
        :param region: Region of the DB instance
        :param access_key:
        :param secret_access_key:
        """
        self.db_name            = db_name
        self.db_engine          = db_engine.lower()
        self.availability_zone  = availability_zone
        self.region             = region
        self.period             = period
        self.monitoring_type    = monitoring_type

        if (access_key is None and secret_access_key is None) or (len(access_key) == 0 and len(secret_access_key) == 0):
            """If access keys are empty or if their length is 0, try loading credentials from instance roles or .aws directory
            """
            self.cloudwatch_client = boto3.client("cloudwatch",
                                                  region_name=region)
        else:
            self.cloudwatch_client = boto3.client("cloudwatch",
                                                  region_name=region,
                                                  aws_access_key_id=access_key,
                                                  aws_secret_access_key=secret_access_key)

    def get_metrics_from_cloud_watch(self):
        """Performs an API call to boto3 to get metrics for cloudwatch

        :return: None or Dict with metrics
        """
        metric_data_queries = []

        if self.db_engine == "maria" or self.db_engine == "aurora":
            db_metrics_dict = self.METRICS.get(self.monitoring_type).get(self.db_engine)

            for metric in db_metrics_dict.keys():
                metric_data_query_dict = {
                    "Id": "{}_{}".format(self.db_name.replace("-", "").lower(), metric.lower()),
                    "MetricStat": {
                        "Metric": {
                            "Namespace": self.NAMESPACE,
                            "MetricName": metric,
                            "Dimensions": [
                                {
                                    "Name": "DBInstanceIdentifier",
                                    "Value": self.db_name
                                }
                            ]
                        },

                        "Period": self.period,
                        "Stat": "Maximum"
                    },
                    "Label": metric,
                    "ReturnData": True
                }

                metric_data_queries.append(metric_data_query_dict)

            response = self.cloudwatch_client.get_metric_data(
                MetricDataQueries=metric_data_queries,
                StartTime=datetime.utcnow() - timedelta(minutes=int(self.period/60)+3),
                EndTime=datetime.utcnow() - timedelta(minutes=int(self.period/60)),
                ScanBy='TimestampDescending'
            )
            return response

        else:
            Logger.publish_log_error("DB engine not specified or not supported, Supported engines are aurora and maria")
            return None
