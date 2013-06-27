#-*- coding: utf-8 -*-

import mock
import unittest
import sys
from nokaut.lib import nokaut_api
import urlparse
from nokaut.lib import urllib

EXAMPLE_RESPONSE = """\
<?xml version="1.0" encoding="UTF-8"?>
<rsp stat="ok">
    <items>
        <item>
            <id>5519095632551337932</id>
            <name>EasyCover na aparat Canon 450/500D</name>
            <shop_count>1</shop_count>
            <offer_count>1</offer_count>
            <price_min>139,00</price_min>
            <price_max>139,00</price_max>
            <price_avg>139,00</price_avg>
            <url>http://www.nokaut.pl/futeraly-fotograficzne/easycover-na-aparat-canon-450-500d.html</url>
            <image_mini>http://nokautimg4.pl/p-cb-eb-cbeba28bb6ba027093e79d196c51b09d90x90/easycover-na-aparat-canon-450-500d.jpg</image_mini>
            <image_medium>http://nokautimg4.pl/p-cb-eb-cbeba28bb6ba027093e79d196c51b09d130x130/easycover-na-aparat-canon-450-500d.jpg</image_medium>
            <image_large>http://nokautimg4.pl/p-cb-eb-cbeba28bb6ba027093e79d196c51b09d500x500/easycover-na-aparat-canon-450-500d.jpg</image_large>
            <rate>0.00</rate>
            <thumbnail>http://nokautimg4.pl/p-cb-eb-cbeba28bb6ba027093e79d196c51b09d90x90/easycover-na-aparat-canon-450-500d.jpg</thumbnail>
            <image>http://nokautimg4.pl/p-cb-eb-cbeba28bb6ba027093e79d196c51b09d130x130/easycover-na-aparat-canon-450-500d.jpg</image>
        </item>
        <item>
            <id>7705481406037386865</id>
            <name>Pilot radiowy Canon 450D 400D 350D 300D FreePower</name>
            <shop_count>1</shop_count>
            <offer_count>1</offer_count>
            <price_min>105,00</price_min>
            <price_max>105,00</price_max>
            <price_avg>105,00</price_avg>
            <url>http://www.nokaut.pl/piloty-i-wezyki-spustowe/pilot-radiowy-canon-450d-400d-350d-300d-freepower.html</url>
            <image_mini>http://nokautimg3.pl/p-64-16-64160ca5522c8095de9f3813299d847390x90/pilot-radiowy-canon-450d-400d-350d-300d-freepower.jpg</image_mini>
            <image_medium>http://nokautimg3.pl/p-64-16-64160ca5522c8095de9f3813299d8473130x130/pilot-radiowy-canon-450d-400d-350d-300d-freepower.jpg</image_medium>
            <image_large>http://nokautimg3.pl/p-64-16-64160ca5522c8095de9f3813299d8473500x500/pilot-radiowy-canon-450d-400d-350d-300d-freepower.jpg</image_large>
            <rate>0.00</rate>
            <thumbnail>http://nokautimg3.pl/p-64-16-64160ca5522c8095de9f3813299d847390x90/pilot-radiowy-canon-450d-400d-350d-300d-freepower.jpg</thumbnail>
            <image>http://nokautimg3.pl/p-64-16-64160ca5522c8095de9f3813299d8473130x130/pilot-radiowy-canon-450d-400d-350d-300d-freepower.jpg</image>
        </item>
        <item>
            <id>214835676480362228</id>
            <name>ALPHA Digital BG-E5</name>
            <shop_count>1</shop_count>
            <offer_count>1</offer_count>
            <price_min>138,00</price_min>
            <price_max>138,00</price_max>
            <price_avg>138,00</price_avg>
            <url>http://www.nokaut.pl/akumulatory-fotograficzne/alpha-digital-bg-e5.html</url>
            <image_mini>http://nokautimg2.pl/p-56-08-560834b6210b901c3de88477266afbd290x90/alpha-digital-bg-e5.jpg</image_mini>
            <image_medium>http://nokautimg2.pl/p-56-08-560834b6210b901c3de88477266afbd2130x130/alpha-digital-bg-e5.jpg</image_medium>
            <image_large>http://nokautimg2.pl/p-56-08-560834b6210b901c3de88477266afbd2500x500/alpha-digital-bg-e5.jpg</image_large>
            <rate>0.00</rate>
            <thumbnail>http://nokautimg2.pl/p-56-08-560834b6210b901c3de88477266afbd290x90/alpha-digital-bg-e5.jpg</thumbnail>
            <image>http://nokautimg2.pl/p-56-08-560834b6210b901c3de88477266afbd2130x130/alpha-digital-bg-e5.jpg</image>
        </item>
        <item>
            <id>5352107065365888798</id>
            <name>- Canon 4508B010AA</name>
            <shop_count>1</shop_count>
            <offer_count>1</offer_count>
            <price_min>313,00</price_min>
            <price_max>313,00</price_max>
            <price_avg>313,00</price_avg>
            <url>http://www.nokaut.pl/pozostale-akcesoria-do-drukarek/canon-4508b010aa.html</url>
            <image_mini>http://nokautimg2.pl/p-1a-31-1a31f38588dfed58d25e1596ff72f08890x90/canon-4508b010aa.jpg</image_mini>
            <image_medium>http://nokautimg2.pl/p-1a-31-1a31f38588dfed58d25e1596ff72f088130x130/canon-4508b010aa.jpg</image_medium>
            <image_large>http://nokautimg2.pl/p-1a-31-1a31f38588dfed58d25e1596ff72f088500x500/canon-4508b010aa.jpg</image_large>
            <rate>0.00</rate>
            <thumbnail>http://nokautimg2.pl/p-1a-31-1a31f38588dfed58d25e1596ff72f08890x90/canon-4508b010aa.jpg</thumbnail>
            <image>http://nokautimg2.pl/p-1a-31-1a31f38588dfed58d25e1596ff72f088130x130/canon-4508b010aa.jpg</image>
        </item>
        <item>
            <id>5883965206927818031</id>
            <name>Discovered easyCover do Canon 450D/500D</name>
            <shop_count>1</shop_count>
            <offer_count>1</offer_count>
            <price_min>89,00</price_min>
            <price_max>89,00</price_max>
            <price_avg>89,00</price_avg>
            <url>http://www.nokaut.pl/pozostale-akcesoria-fotograficzne/discovered-easycover-do-canon-450d-500d.html</url>
            <image_mini>http://nokautimg2.pl/p-94-5b-945b3466779a517538e31912255ac5d990x90/discovered-easycover-do-canon-450d-500d.jpg</image_mini>
            <image_medium>http://nokautimg2.pl/p-94-5b-945b3466779a517538e31912255ac5d9130x130/discovered-easycover-do-canon-450d-500d.jpg</image_medium>
            <image_large>http://nokautimg2.pl/p-94-5b-945b3466779a517538e31912255ac5d9500x500/discovered-easycover-do-canon-450d-500d.jpg</image_large>
            <rate>0.00</rate>
            <thumbnail>http://nokautimg2.pl/p-94-5b-945b3466779a517538e31912255ac5d990x90/discovered-easycover-do-canon-450d-500d.jpg</thumbnail>
            <image>http://nokautimg2.pl/p-94-5b-945b3466779a517538e31912255ac5d9130x130/discovered-easycover-do-canon-450d-500d.jpg</image>
        </item>
        <item>
            <id>6899684875502046996</id>
            <name>Osłona LCD Canon 450D 500D GGS III generacji</name>
            <shop_count>1</shop_count>
            <offer_count>1</offer_count>
            <price_min>45,00</price_min>
            <price_max>45,00</price_max>
            <price_avg>45,00</price_avg>
            <url>http://www.nokaut.pl/ochrona-wyswietlacza-aparatu/oslona-lcd-canon-450d-500d-ggs-iii-generacji.html</url>
            <image_mini>http://nokautimg4.pl/p-75-f8-75f88115b67b3ded5980c3582ee72d0190x90/oslona-lcd-canon-450d-500d-ggs-iii-generacji.jpg</image_mini>
            <image_medium>http://nokautimg4.pl/p-75-f8-75f88115b67b3ded5980c3582ee72d01130x130/oslona-lcd-canon-450d-500d-ggs-iii-generacji.jpg</image_medium>
            <image_large>http://nokautimg4.pl/p-75-f8-75f88115b67b3ded5980c3582ee72d01500x500/oslona-lcd-canon-450d-500d-ggs-iii-generacji.jpg</image_large>
            <rate>0.00</rate>
            <thumbnail>http://nokautimg4.pl/p-75-f8-75f88115b67b3ded5980c3582ee72d0190x90/oslona-lcd-canon-450d-500d-ggs-iii-generacji.jpg</thumbnail>
            <image>http://nokautimg4.pl/p-75-f8-75f88115b67b3ded5980c3582ee72d01130x130/oslona-lcd-canon-450d-500d-ggs-iii-generacji.jpg</image>
        </item>
        <item>
            <id>757101521335487259</id>
            <name>Ładowarka  LP-E5 12/230V CANON 450D 500D 1000D</name>
            <shop_count>1</shop_count>
            <offer_count>1</offer_count>
            <price_min>23,00</price_min>
            <price_max>23,00</price_max>
            <price_avg>23,00</price_avg>
            <url>http://www.nokaut.pl/ladowarki-do-akumulatorkow/ladowarka-lp-e5-12-230v-canon-450d-500d-1000d.html</url>
            <image_mini>http://nokautimg3.pl/p-bd-1a-bd1a899cfe35ef558f0a479803623eeb90x90/ladowarka-lp-e5-12-230v-canon-450d-500d-1000d.jpg</image_mini>
            <image_medium>http://nokautimg3.pl/p-bd-1a-bd1a899cfe35ef558f0a479803623eeb130x130/ladowarka-lp-e5-12-230v-canon-450d-500d-1000d.jpg</image_medium>
            <image_large>http://nokautimg3.pl/p-bd-1a-bd1a899cfe35ef558f0a479803623eeb500x500/ladowarka-lp-e5-12-230v-canon-450d-500d-1000d.jpg</image_large>
            <rate>0.00</rate>
            <thumbnail>http://nokautimg3.pl/p-bd-1a-bd1a899cfe35ef558f0a479803623eeb90x90/ladowarka-lp-e5-12-230v-canon-450d-500d-1000d.jpg</thumbnail>
            <image>http://nokautimg3.pl/p-bd-1a-bd1a899cfe35ef558f0a479803623eeb130x130/ladowarka-lp-e5-12-230v-canon-450d-500d-1000d.jpg</image>
        </item>
        <item>
            <id>1779987317393138409</id>
            <name>Walimex pro Battery Grip Canon 450D/500D/1000D</name>
            <shop_count>1</shop_count>
            <offer_count>1</offer_count>
            <price_min>199,99</price_min>
            <price_max>199,99</price_max>
            <price_avg>199,99</price_avg>
            <url>http://www.nokaut.pl/baterie-elektryczne/walimex-pro-battery-grip-canon-450d-500d-1000d.html</url>
            <image_mini>http://nokautimg4.pl/p-c3-fc-c3fc0f17d84db770aaa239f543e3a96590x90/walimex-pro-battery-grip-canon-450d-500d-1000d.jpg</image_mini>
            <image_medium>http://nokautimg4.pl/p-c3-fc-c3fc0f17d84db770aaa239f543e3a965130x130/walimex-pro-battery-grip-canon-450d-500d-1000d.jpg</image_medium>
            <image_large>http://nokautimg4.pl/p-c3-fc-c3fc0f17d84db770aaa239f543e3a965500x500/walimex-pro-battery-grip-canon-450d-500d-1000d.jpg</image_large>
            <rate>0.00</rate>
            <thumbnail>http://nokautimg4.pl/p-c3-fc-c3fc0f17d84db770aaa239f543e3a96590x90/walimex-pro-battery-grip-canon-450d-500d-1000d.jpg</thumbnail>
            <image>http://nokautimg4.pl/p-c3-fc-c3fc0f17d84db770aaa239f543e3a965130x130/walimex-pro-battery-grip-canon-450d-500d-1000d.jpg</image>
        </item>
        <item>
            <id>3798810434223671323</id>
            <name>Discovered easyCover do Canon 450D/500D - Gratis Transport-Raty w 15 minut-Punkty Odbioru-Tel  571-51-55</name>
            <shop_count>1</shop_count>
            <offer_count>1</offer_count>
            <price_min>89,00</price_min>
            <price_max>89,00</price_max>
            <price_avg>89,00</price_avg>
            <url>http://www.nokaut.pl/pozostale-akcesoria-fotograficzne/discovered-easycover-do-canon-450d-500d-gratis-transport-raty-w-15-minut-punkty-odbioru-tel-571-51-55.html</url>
            <image_mini>http://nokautimg1.pl/p-dd-70-dd708ae190df787c5cab1db87c1e8e8f90x90/discovered-easycover-do-canon-450d-500d-gratis-transport-raty-w-15-minut-punkty-odbioru-tel-571-51-55.jpg</image_mini>
            <image_medium>http://nokautimg1.pl/p-dd-70-dd708ae190df787c5cab1db87c1e8e8f130x130/discovered-easycover-do-canon-450d-500d-gratis-transport-raty-w-15-minut-punkty-odbioru-tel-571-51-55.jpg</image_medium>
            <image_large>http://nokautimg1.pl/p-dd-70-dd708ae190df787c5cab1db87c1e8e8f500x500/discovered-easycover-do-canon-450d-500d-gratis-transport-raty-w-15-minut-punkty-odbioru-tel-571-51-55.jpg</image_large>
            <rate>0.00</rate>
            <thumbnail>http://nokautimg1.pl/p-dd-70-dd708ae190df787c5cab1db87c1e8e8f90x90/discovered-easycover-do-canon-450d-500d-gratis-transport-raty-w-15-minut-punkty-odbioru-tel-571-51-55.jpg</thumbnail>
            <image>http://nokautimg1.pl/p-dd-70-dd708ae190df787c5cab1db87c1e8e8f130x130/discovered-easycover-do-canon-450d-500d-gratis-transport-raty-w-15-minut-punkty-odbioru-tel-571-51-55.jpg</image>
        </item>
    </items>
    <total>9</total>
</rsp>"""
class MyTest(unittest.TestCase):

	@mock.patch('nokaut.lib.urllib.urlopen')
	def test_czy_wyjscie(self, mmock):
	    NOKAUT_KEY='a8839b1180ea00fa1cf7c6b74ca01bb5'
	    NOKAUT_KEY_WORD='canon450d'
	    #import ipdb; ipdb.set_trace()
	    stream = mock.MagicMock()
	    mmock.return_value = stream
	    stream.read.return_value = EXAMPLE_RESPONSE
	    nokaut_api(NOKAUT_KEY, NOKAUT_KEY_WORD) 
	    do_parsowania = mmock.call_args[0]
	    do_parsowania = urlparse.urlparse((str(do_parsowania))[2:-3])
	    query_parse = urlparse.parse_qs(do_parsowania.query)
	    self.assertEqual(query_parse['key'][0], NOKAUT_KEY)
	    self.assertEqual(query_parse['keyword'][0],NOKAUT_KEY_WORD)
	    self.assertEqual(query_parse['format'][0],'rest')
	    self.assertEqual(query_parse['method'][0],'nokaut.Product.getByKeyword')
	    self.assertEqual(do_parsowania.scheme,'http')
	    self.assertEqual(do_parsowania.netloc,'api.nokaut.pl')
	    self.assertEqual(do_parsowania.path,'/')

if __name__=="__main__":
 	unittest.main()