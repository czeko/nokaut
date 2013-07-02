import urllib
import urllib2
from lxml import etree


class NokautError(Exception):
    pass


def nokaut__api(n_key, n_keyword):
    url = 'http://api.nokaut.pl/'
    query = urllib.urlencode(dict(
        format='rest',
        key=n_key,
        method='nokaut.Product.getByKeyword',
        keyword=n_keyword
    ))
    url = '?'.join([url, query])
    f = urllib2.urlopen(url)
    root = etree.fromstring(f.read())
    if root.find('items') is None or root.find('total').text == '0':
        raise NokautError('Brak produktu')
    else:
        item = root.xpath('/rsp/items/item')[0]
        price = item.find('price_min').text
        price = price.replace(',', '.')
        price = float(price)
        url = item.find('url').text
        return price, url

