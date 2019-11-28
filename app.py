URL = 'https://www.bankmandiri.co.id/kurs'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

from bs4 import BeautifulSoup
import requests

r = requests.get(URL, headers=HEADERS)
html = r.text
soup = BeautifulSoup(html, features='lxml')
data = soup.findAll('td')
datas = []
for i in range(len(data)//7):
    sub_data=[]
    #sub_data.append(data[i*7+0].text)
    #sub_data.append((data[i*7+1].text).split(",")[0])
    #sub_data.append((data[i*7+2].text).split(",")[0])
    sub_data.append((data[i*7+3].text).split(",")[0])
    sub_data.append((data[i*7+4].text).split(",")[0])
    sub_data.append((data[i*7+5].text).split(",")[0])
    sub_data.append((data[i*7+6].text).split(",")[0])
    datas.append(sub_data)
###
datas = list(map(list, zip(*datas)))

for i in range(len(datas)):
    for j in range(len(datas[0])):
        datas[i][j] = datas[i][j].replace(".",'')

### 
from flask import Flask, Blueprint, render_template
from werkzeug.contrib.fixers import ProxyFix

web_app = Blueprint('app', __name__)

@web_app.route('/')
def index():
    return render_template('index.html', data=datas)

if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(web_app, url_prefix='/')

    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.run()
