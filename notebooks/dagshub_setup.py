import mlflow
import dagshub

mlflow.set_tracking_uri('https://dagshub.com/rishavkumar1951/mlops-mini-project.mlflow')
mlflow.set_experiment('mlops-mini-project')

dagshub.init(repo_owner='rishavkumar1951', repo_name='mlops-mini-project', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)