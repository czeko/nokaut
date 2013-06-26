import urllib
import urllib2

from lxml import etree
def nokaut_api(arg1, arg2):
	#import ipdb; ipdb.set_trace()
	#argv1=sys.argv[1]
	#argv2=sys.argv[2]
	opener = urllib.FancyURLopener({})

	f = opener.open("http://api.nokaut.pl/?format=rest&key=%s&method=nokaut.Product.getByKeyword&keyword=%s" %(arg1,arg2))

	wynik= etree.parse(f)
	root=wynik.getroot()   
	for child in root.iter('item'):
	  	cena_minimalna=child.find('price_min').text
	  	adres=child.find('url').text
	return cena_minimalna, adres

#nokaut_api('a8839b1180ea00fa1cf7c6b74ca01bb5', 'canon450d')