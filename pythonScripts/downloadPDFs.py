import path+urllib
path = '/usr/local/lib/python3.10/'

url = input("Enter Link to Download PDF : ")
Name = input("Enter a Name for the PFD file : ")
FileName = Name+".pdf"
urllib.request.urlretrieve(url, FileName)
