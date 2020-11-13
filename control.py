import requests
response=request.get("https://www.usom.gov.tr/url-list.txt", verify=False)
myFolder=open("usom.txt","w")
myFolder.write(str(response.content))
myFolder.close()