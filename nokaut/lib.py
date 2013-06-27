import urllib
import urllib2
from lxml import etree


class PusteError(Exception):
      pass

def nokaut_api(arg1, arg2):
	
	f = urllib.urlopen("http://api.nokaut.pl/?format=rest&key=%s&method=nokaut.Product.getByKeyword&keyword=%s" %(arg1,arg2))
	root = etree.fromstring(f.read())


	if root.find('items') is None or root.find('total').text == '0':
		raise PusteError('Brak produktu')
	for item in root.iter('item'):
		cena_minimalna = item.find('price_min').text
		adres = item.find('url').text
		return 'Cena mini:',cena_minimalna, 'Znajdziesz tutaj: ',adres
