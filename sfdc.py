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
        res = sf.query("select clicks__c from Campaign__c")
        print res["records"]
        records = res['records']
        for x in  OrderedDict(records):
            print x
        
data = sfdcdatafetch('mudit.somani@salesforce.com','mudit1234$','N0OF2max8RxHHoZkY4AB96uih')