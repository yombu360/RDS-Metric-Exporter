# https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MonitoringOverview.html#monitoring-cloudwatch
# https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Monitoring.html

from prometheus_client import Gauge

LABELS = [
    "db_name",
    "db_engine",
    "az_name"
]


Metrics = {
    "maria": {
        "write_latency"                 : Gauge("rds_exporter_write_latency_seconds", "The average amount of time taken per disk I/O operation", LABELS),
        "read_latency"                  : Gauge("rds_exporter_read_latency_seconds", "The average amount of time taken per disk I/O operation", LABELS),
        "write_iops"                    : Gauge("rds_exporter_write_IOPS_per_second", "The average number of disk write I/O operations per second", LABELS),
        "read_iops"                     : Gauge("rds_exporter_read_IOPS_per_second", "The average number of disk read I/O operations per second", LABELS),
        "read_throughput"               : Gauge("rds_exporter_read_throughput_bytes_per_second", "The average number of bytes read from disk per second", LABELS),
        "write_throughput"              : Gauge("rds_exporter_read_throughput_bytes_per_second", "The average number of bytes written to disk per second", LABELS),
        "cpu_credit_balance"            : Gauge("rds_exporter_cpu_credit_count", "CPU credit count", LABELS),
        "burst_balance"                 : Gauge("rds_exporter_cpu_burst_balance_percent", "The percent of General Purpose SSD (gp2) burst-bucket I/O credits available", LABELS),
        "network_transmit_throughput"   : Gauge("rds_exporter_network_transmit_throughput_bytes_per_second", "Network transmission throughput", LABELS),
        "network_receive_throughput"    : Gauge("rds_exporter_network_receive_throughput_bytes_per_second", "Network receive throughput", LABELS),
        "free_storage_space"            : Gauge("rds_exporter_free_space_bytes", "The amount of available storage space", LABELS),
        "disk_queue_depth"              : Gauge("rds_exporter_disk_queue_depth_count", "The number of outstanding IOs (read/write requests) waiting to access the disk.", LABELS),
        "cpu_utilization"               : Gauge("rds_exporter_cpu_utilization_percent", "The percentage of CPU utilization", LABELS),
        "database_connections"          : Gauge("rds_exporter_database_connections_count", "The number of database connections in use", LABELS),
        "swap_usage"                    : Gauge("rds_exporter_swap_usage_bytes", "The amount of swap space used on the DB instance", LABELS),
        "freeable_memory"               : Gauge("rds_exporter_freeable_memory_bytes", "Available RAM", LABELS),
        "binlog_disk_usage"             : Gauge("rds_exporter_binlog_disk_usage_bytes", "The amount of disk space occupied by binary logs on the master", LABELS)
    },

    "aurora": {
        "queries"                       : Gauge("rds_exporter_queries_per_second", "The average number of queries executed per second", LABELS),
        "deadlocks"                     : Gauge("rds_exporter_deadlock_per_second", "The average number of deadlocks in the database per second", LABELS),
        "delete_latency"                : Gauge("rds_exporter_delete_latency_milliseconds", "The amount of latency for delete queries", LABELS),
        "dml_throughput"                : Gauge("rds_exporter_dml_throughput_per_second", "The average number of inserts, updates, and deletes per second", LABELS),
        "commit_latency"                : Gauge("rds_exporter_commit_latency_milliseconds", "The amount of latency for commit queries", LABELS),
        "commit_throughput"             : Gauge("rds_exporter_commit_throughput_per_second", "The average number of commit queries per second", LABELS),
        "blocked_transaction"           : Gauge("rds_exporter_blocked_transaction_per_second", "The average number of transactions in the database that are blocked per second", LABELS),
        "select_throughput"             : Gauge("rds_exporter_select_throughput_per_second", "The average number of select queries per second", LABELS),
        "select_latency"                : Gauge("rds_exporter_select_latency_milliseconds", "The amount of latency select requests", LABELS),
        "ddl_latency"                   : Gauge("rds_exporter_ddl_latency_milliseconds", "The amount of latency for data definition language (DDL) requests", LABELS),
        "network_transmit_throughput"   : Gauge("rds_exporter_network_transmit_throughput_bytes_per_second", "Network transmission throughput", LABELS),
        "active_transactions"           : Gauge("rds_exporter_active_transactions_per_second", "The average number of current transactions executing on an Aurora database instance per second", LABELS),
        "engine_uptime"                 : Gauge("rds_exporter_engine_uptime_seconds", "The amount of time that the instance has been running", LABELS),
        "cpu_utilization"               : Gauge("rds_exporter_cpu_utilization_percent", "The percentage of CPU utilization", LABELS),
        "dml_latency"                   : Gauge("rds_exporter_dml_latency_milliseconds", "The amount of latency for data manipulation language (DDL) requests", LABELS),
        "delete_throughput"             : Gauge("rds_exporter_delete_throughput_per_second", "The average number of delete queries per second", LABELS),
        "database_connections"          : Gauge("rds_exporter_database_connections_count", "The number of database connections in use", LABELS),
        "freeable_memory"               : Gauge("rds_exporter_freeable_memory_bytes", "Available RAM", LABELS),
        "ddl_throughput"                : Gauge("rds_exporter_ddl_throughput_per_second", "The average number of inserts, updates, and deletes per second", LABELS),
        "insert_latency"                : Gauge("rds_exporter_insert_latency_milliseconds", "The amount of latency insert requests", LABELS),
        "login_failures"                : Gauge("rds_exporter_login_failures_per_second", "The average number of failed login attempts per second", LABELS),
        "free_local_storage"            : Gauge("rds_exporter_free_local_storage_bytes", "The amount of storage available for temporary tables and logs", LABELS),
        "cpu_credit_balance"            : Gauge("rds_exporter_cpu_credit_count", "CPU credit count", LABELS),
        "network_receive_throughput"    : Gauge("rds_exporter_network_receive_throughput_bytes_per_second", "Network receive throughput", LABELS),
        "update_latency"                : Gauge("rds_exporter_update_latency_milliseconds", "The amount of latency update requests", LABELS),
        "update_throughput"             : Gauge("rds_exporter_update_throughput_per_second", "The average number of update queries per second", LABELS),
        "aurora_replica_lag_minimum"    : Gauge("rds_exporter_aurora_replica_lag_minimum_milliseconds", "The minimum amount of lag between the primary instance and each Aurora DB instance in the DB cluster", LABELS),
        "aurora_replica_lag_maximum"    : Gauge("rds_exporter_aurora_replica_lag_maximum_milliseconds", "The maximum amount of lag between the primary instance and each Aurora DB instance in the DB cluster", LABELS),
        "aurora_replica_lag"            : Gauge("rds_exporter_aurora_replica_lag_milliseconds", "The amount of lag when replicating updates from the primary instance", LABELS),
        "aurora_bin_log_replica_lag"    : Gauge("rds_exporter_aurora_bin_log_replica_lag_seconds", "The amount of time a replica DB cluster running on Aurora with MySQL compatibility lags behind the source DB cluster", LABELS)
    }
}
