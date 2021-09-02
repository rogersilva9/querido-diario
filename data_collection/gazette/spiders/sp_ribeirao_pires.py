from datetime import date,datetime
from dateutil import relativedelta
from gazette.spiders.base import BaseGazetteSpider
import scrapy.http.request
from pprint import pprint

class SpRibeiraoPiresSpider(BaseGazetteSpider):
	
	name = "sp_ribeirao_pires"
	allowed_domains = "www.ribeiraopires.sp.gov.br"
	start_date = date(2016,5,25)
	url_base = "https://www.ribeiraopires.sp.gov.br/diario-oficial/26-{}"
	
	
	TERRITORY_ID = "3543303"

	def start_requests(self):		
		current_date = self.start_date
		while current_date <= date.today():
			year_month = current_date.strftime("%m-%Y") #like 05-2016
			current_date = current_date + relativedelta.relativedelta(months=1)
			yield scrapy.Request(
			self.url_base.format(year_month),callback=self.extract_gazette_links
			)
			pprint(self.url_base)

	
	def extract_gazette_links(self,response):
		pprint(response)		
		for a in response.css('div.calendario_TD2 a'):
			url = "https://www.ribeiraopires.sp.gov.br"+(a.attrib["href"])
			yield scrapy.Request(
			url,callback=self.parse
			)
			pprint(url)
			
	def parse(self,response):
		pprint('Não chega aqui')
    
               
		url = "https://www.ribeiraopires.sp.gov.br/" + response.css('.pagina-anexos > a:nth-child(2)::attr(href)').extract()
        
        
		gazette_date = response.css('h1').extract() # ['<h1>Atos Oficiais - 06/08/2021</h1>']
		gazette_date = gazette_date[0][20:30] # '06/08/2021'
		gazette_date = datetime.strptime(gazette_date, "%d/%m/%Y").date()  #formato Python
        
		yield Gazette (
			date = gazette_date,
			file_urls = [url],
			is_extra_edition= False,
			territory_id = self.TERRITORY_ID,
			power="executive",
			scraped_at = datetime.utcnow(),
		)		
            		
	
        
