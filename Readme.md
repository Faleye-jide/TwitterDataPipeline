## This is a an ETL pipeline where I utilized Python to interact and communicate with twitter api. In this basic task, I was able to ingest data from twitter and then stored into csv file. In the next future, I plan to deploy the code on Airflow and save the extracted data on Amazon S3 as opposed to saving it on my local pc.

 ### _Before you get started, you need to have some prerequistes to use the simple app._

---
- Create an accounton twitter developer 
- Create the following
    - Consumer secret key
    - Access token
    - Access token secret
- install the required dependencies using the command below
```python
pip install requirements.txt
```

- Finally, for entry into this application, run below commands

```python
python main.py -fn --file_name -f --folder_name -fe file_ext 
```