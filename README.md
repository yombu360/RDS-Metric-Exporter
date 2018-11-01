# RDS Metric Exporter

Prometheus exporter written in python that will export metrics for AWS RDS by querying cloudwatch metrics.


## Policy / Permissions required

Only **cloudwatch:GetMetricData** permission is required to receive the metrics

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "cloudwatch:GetMetricData",
            "Resource": "*"
        }
    ]
}
```

## Requirements to run the exporter
 - Make sure you have the permission / roles attached to the server that you are running this exporter from.
 - If you are running from local, there are 2 ways to access the metrics. One is to have aws credentials configured using 
 the **awscli** (recommended) or You can pass access key and secret access key to in the config file
 - Fill the config.yaml file with your configurations.
 - Run the following command to install the dependencies
 ```bash
  pip install -r requirements.txt
 ```
 - To run the exporter, run the following command:
 ```bash
  python rds_exporter.py -config <path to config.yaml>
 ```
 
 
# TODOS
 - Support for postgres, mysql
 - Support to add enhanced monitoring
 