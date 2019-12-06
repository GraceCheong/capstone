import boto3
import configparser
import os
import sys
import dbInfo

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

CONFIG_DIR = os.path.join(BASE_DIR, 'config.ini')

print(CONFIG_DIR)

config = configparser.ConfigParser()
#config = configparser.ConfigParser()
config.read(CONFIG_DIR)


def initDB():

    dblist = list()
    client = boto3.client(
        'rds',
        aws_access_key_id=config['aws']['aws_access_key_id'],
        aws_secret_access_key=config['aws']['aws_secret_access_key'],
        aws_session_token=config['aws']['aws_session_token'],
        region_name = config['db']['REGION']
    )

    try:
        dbs = client.describe_db_instances()
        count = 0
        for db in dbs['DBInstances']:
            count += 1
            dbinfo = dbInfo.dbInfo().infoInit(name="capstonedb",
                                       host=db['Endpoint']['Address'],
                                       user=db['MasterUsername'],
                                       port=db['Endpoint']['Port'],
                                       pw="khu-ce2015")
            dblist.append(dbinfo)
            print(dbinfo.name,":", dbinfo.user, "@" ,dbinfo.host, " working")
        print("you've got {} of DB working".format(count))

    except Exception as e :
        print("error occured", e)

    return dblist

#initDB()