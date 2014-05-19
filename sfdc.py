from simple_salesforce import Salesforce
import json
from collections import OrderedDict

class sfdcdatafetch():
    def __init__(self, username, password, security_token):
        sf = Salesforce(username=username, password=password, security_token=security_token)
        query = "Select "
        for x in sf.Campaign__c.describe()['fields']:
          query = query + x['name'] + ","
        query = query[:-1] + " from Campaign__c"
        print query
        res = sf.query(query)
        records = res['records']
        for x in records:
            for y in sf.Campaign__c.describe()['fields']:
                print x[y['name']]

data = sfdcdatafetch('mudit.somani@salesforce.com','mudit1234$','N0OF2max8RxHHoZkY4AB96uih')