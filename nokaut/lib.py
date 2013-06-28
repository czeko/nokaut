import urllib
import urllib2
from lxml import etree


class PusteError(Exception):
    pass


def nokaut__api(arg1, arg2):
    url = 'http://api.nokaut.pl/'
    query = urllib.urlencode(dict(
        format='rest',
        key=arg1,
        method='nokaut.Product.getByKeyword',
        keyword=arg2
    ))
    url = '?'.join([url, query])
    try:
        f = urllib2.urlopen(url)
    except urllib2.URLError, err:
        return 'Sprawdz czy z internetem wszystko ok!', err.reason
    else:
        root = etree.fromstring(f.read())
        if root.find('items') is None or root.find('total').text == '0':
            raise PusteError('Brak produktu')
        else:
            item = root.xpath('/rsp/items/item')[0]
            cena__minimalna = item.find('price_min').text
            adres = item.find('url').text
            return "Cena mini:", cena__minimalna, "Znajdziesz tutaj: ", adres
