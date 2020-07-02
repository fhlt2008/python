import requests
import json
import sys
aheaders = {'Content-Type': 'application/json','Referer':'http://59.231.11.90/'}
phone = [{"phone":13467996789},{"phone":13487416023}]
url = "http://59.231.11.90/info/insertNetInfo"
url1= "http://59.231.11.90/info/checkPhone"
url2 = "http://59.231.11.90/info/selectNetInfo"
url3 = "http://59.231.11.90/info/updateNetInfo"
"""num = range(0,10)
for i in num:
    response = requests.post(url, headers=aheaders, data = json.dumps(adata[i]))
 
    print response.text
{"str":"location_id='31311',c_name='大数据中心',contact='龙寒斯',phone='13467996789',join_up='裸光纤-50M'","phone":"13467996789"}

"""
f = open("idlist.json","r",encoding='utf-8')
json_data = json.load(f)
for i in range(20,len(json_data["data"])):
	try:
		response = requests.post(url2, headers=aheaders, data = json.dumps(json_data["data"][i]))
		data = json.loads(response.text)
		str1 = '{"str":"'
		str1=str1+"location_id='"+str(data[0]["location_id"])+"',c_name='"
		str1 = str1+data[0]["c_name"]+"',contact='"

		str1 = str1 + data[0]["contact"]+"',phone='"
		str1 =str1 + str(data[0]["phone"])+"',join_up='裸光纤-50M'"
		str1 = str1 + '","phone":"'+data[0]["phone"]+'"}'
		data =json.loads(str1)
		response1 = requests.post(url3, headers=aheaders, data = json.dumps(data))
		print (response1.text)
	except:
		print ("error:",i)




