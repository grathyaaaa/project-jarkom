from flask import Flask, Blueprint, render_template
from werkzeug.contrib.fixers import ProxyFix

hello = Blueprint('hello', __name__)

@hello.route('/')
def hello_world():
    return 'Hello, World!'
#############flask


#not flask
import bs4
from requests_html import HTMLSession

def strike(text):
    result = ''
    for c in text:
        result = result + c + '\u0336'
    return result

session = HTMLSession()
r = session.get('https://shopee.co.id/flash_sale?categoryId=41')

r.html.render(scrolldown=500)

page_html = r.html.html

soup = bs4.BeautifulSoup(page_html, features='lxml')

import io
with io.open("text.txt", "w", encoding="utf-8") as f:
    f.write(soup.prettify())

names = soup.findAll("div", {"class": "flash-sale-item-card__item-name"})
prices = soup.findAll("span", {"class": "item-price-number"})

sl = []
for i in range(len(names)):
    sll = []
    sll.append(names[i].text)
    sll.append(strike(prices[i*2].text))
    sll.append(prices[(i*2) +1].text)
    sl.append(sll)
#################not flask


#flask
@hello.route('/test')
def testing():
    return render_template('index.html', data=sl)

if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(hello, url_prefix='/')

    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.run()
