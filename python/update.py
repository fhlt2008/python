import requests
import json
import sys

reload(sys)
sys.setdefaultencoding('utf-8')











aheaders = {'Content-Type': 'application/json','Referer':'http://59.231.11.90/'}
phone = [{"phone":13467996789},{"phone":13487416023}]
url = "http://59.231.11.90/info/insertNetInfo"
url1= "http://59.231.11.90/info/checkPhone"
num = range(0,10)
"""
for i in num:
    response = requests.post(url, headers=aheaders, data = json.dumps(adata[i]))
 
    print response.text
"""
response = requests.post(url1, headers=aheaders, data = json.dumps(adata[0]))

print json.dumps(response.text)

