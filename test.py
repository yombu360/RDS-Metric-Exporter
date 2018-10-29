# import boto3
# from datetime import datetime, timedelta
#
# client = boto3.client('cloudwatch')
#
# response = client.get_metric_data(
#     MetricDataQueries=[
#         {
#             'Id': 'test',
#             'MetricStat':
#                 {
#                     'Metric': {
#                         'Namespace': 'AWS/RDS',
#                         'MetricName': 'BinLogDiskUsage'
#                     },
#                     'Period': 300,
#                     'Stat': 'SampleCount',
#                     'Unit': 'Bytes'
#                 },
#             'Label': 'test',
#             'ReturnData': True
#         },
#     ],
#     StartTime=datetime.now() - timedelta(days=7),
#     EndTime=datetime.now()
# )
#
# print(response)
#
from prometheus_client import make_wsgi_app, Counter, Gauge
from wsgiref.simple_server import make_server
from prometheus_client import multiprocess, make_wsgi_app, CollectorRegistry

REQUESTS = Counter("http_requests_total", "HTTP requests")
IN_PROGRESS = Gauge("http_requests_inprogress", "Inprogress HTTP requests",
        multiprocess_mode='livesum')

@IN_PROGRESS.track_inprogress()
def app(environ, start_fn):
    REQUESTS.inc()
    if environ['PATH_INFO'] == '/metrics':
        registry = CollectorRegistry()
        multiprocess.MultiProcessCollector(registry)
        metrics_app = make_wsgi_app(registry)
        return metrics_app(environ, start_fn)
    start_fn('200 OK', [])
    return [b'Hello World']

if __name__ == '__main__':
    make
    httpd = make_server('', 8000)
    httpd.serve_forever()
