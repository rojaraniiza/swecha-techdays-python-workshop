#Usage: scrapy runspider 1_quotes_scraper.py 
import scrapy
import csv
class QuotesExtracterItem(scrapy.Spider):
  name = "quotes_extracter"
  allowed_domains = "quotes.toscrape.com"
  start_urls = ["http://quotes.toscrape.com/page/1/","http://quotes.toscrape.com/page/2/"]

  def parse(self, response):
    csv_file = open("quotes.csv", 'a')
    with csv_file:
      writer = csv.writer(csv_file)
      for element in response.xpath('//div[@class="col-md-8"]/div[@class="quote"]'):
        quote = element.xpath('.//span[@class="text"]/text()').extract_first()
        author = element.xpath('.//small[@class="author"]/text()').extract_first()
        tags = element.xpath('.//div[@class="tags"]/a/text()').extract()
        tags = ', '.join(tags) # converting list to string (comma seperated)
        writer.writerow([quote,author,tags])
