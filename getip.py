import requests, json
url = r'https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list'
r = requests.get(url)
with open('proxy.json', 'wb') as f:  
    f.write(r.content)
data = []
with open('proxy.json') as fi:
    for line in fi:
        data.append(json.loads(line))
		
with open('listall.txt','a') as fa:
 i=0
 while i < len(data):
  fa.write (str(data[i]['type'])+"://"+str(data[i]['host'])+":"+str(data[i]['port'])+'\n')
  i+=1

with open('listipport.txt','a') as fip:
 j=0
 while j < len(data):
  fip.write (str(data[j]['host'])+":"+str(data[j]['port'])+'\n')
  j+=1

with open('list.csv','a') as fcsv:
 k=0
 fcsv.write("host,port,country,type,response_time\n")
 while k < len(data):
  fcsv.write (str(data[k]['host'])+","+str(data[k]['port'])+","+str(data[k]['country'])+","+str(data[k]['type'])+","+str(data[k]['response_time'])+'\n')
  k+=1
