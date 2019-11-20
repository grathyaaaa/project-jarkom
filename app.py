URL = 'https://www.bankmandiri.co.id/kurs'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

from bs4 import BeautifulSoup
import requests

r = requests.get(URL, headers=HEADERS)
html = r.text
soup = BeautifulSoup(html, features='lxml')
data = soup.find('table')
###



### 
from flask import Flask, Blueprint, render_template
from werkzeug.contrib.fixers import ProxyFix

web_app = Blueprint('app', __name__)

@web_app.route('/')
def index():
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(web_app, url_prefix='/')

    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.run()
