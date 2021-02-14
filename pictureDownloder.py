import urllib.request


url1="https://assets.nflxext.com/ffe/siteui/acquisition/ourStory/fuji/desktop/device-pile.png"
url2="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSL4nNIXrHVdF1AGOxP6yqgL0Tn6flyxbkeqQ&usqp=CAU"
url3="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSVo288LlUo2jAlMj6g1CwKb0FxTj7nQECyHw&usqp=CAU"

urlLists =[url1,url2,url3]
count=1
for url in  urlLists:
    urllib.request.urlretrieve(url,"pictue"+str(count)+"jpg")
    count +=1
