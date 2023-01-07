from django.shortcuts import render
from django.http import HttpResponse
import json
import urllib.request
# Create your views here.

def index(req):
    if req.method =='POST':
        city = req.POST['city']
        # res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=8a44a88c92ae1574111499a95b7ca282').read()
        res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=8a44a88c92ae1574111499a95b7ca282').read()
        json_data = json.loads(res)
        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate" : str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            "temp":str(int(json_data['main']['temp'])-273) + ' C',
            "pressure" : str(json_data['main']['pressure']),
            "humidity" : str(json_data['main']['humidity'])
        }
    else:
        data={}
        city=''
    return render(req,'index.html',{'city':city,'data':data})
