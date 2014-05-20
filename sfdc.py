from simple_salesforce import Salesforce, SalesforceLogin, SFType
import pymongo
import json
class sfdcdatafetch():

    def __init__(self, username, password, security_token):
        self.username = username
        self.password = password
        self.security_token = security_token

    def returnsObject(self):
        sf = Salesforce(username=self.username, password=self.password, security_token=self.security_token)
        l1 = [[x['name'],x['custom'],x['label']] for x in sf.describe()['sobjects']]
        return l1

    def runQuery(self,*args):
        sf = Salesforce(username=self.username, password=self.password, security_token=self.security_token)
        session_id = sf.session_id
        instance = sf.sf_instance
        query = "Select "
        #session_id, instance = SalesforceLogin(self.username, self.password, self.security_token, True)
        for sObject in args:
            sObjectName = SFType(sObject,session_id,instance)
            for x in sObjectName.describe()['fields']:
                query = query + x['name'] + ","
            query = query[:-1] + " from " + sObjectName.name
            print query
            res = sf.query(query)
            records = res['records']
            ls = []
            data = {}
            type = {}
            for y in sObjectName.describe()['fields']:
                    type[y['name']] = y['type']
            for x in records:
                for y in sObjectName.describe()['fields']:
                    data[y['name']] = x[y['name']]
                ls.append(data)
        return ls
sfdc = sfdcdatafetch('mudit.somani@salesforce.com','mudit1234$','N0OF2max8RxHHoZkY4AB96uih')
print sfdc.returnsObject()
print sfdc.runQuery('Campaign__c')