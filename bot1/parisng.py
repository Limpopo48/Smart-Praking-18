import requests

link = "http://icanhazip.com/"
responce = requests.get(link).text
print(responce)


a,b = map(int,input().split())
print (b,a)

