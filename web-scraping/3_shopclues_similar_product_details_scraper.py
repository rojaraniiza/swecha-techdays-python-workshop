#Usage: scrapy runspider 2_shopclues_product_details_scraper.py -o output.csv
#script to extract the similar product details
import scrapy
import csv
from scrapy.http import Request
class ProductDetailsExtracter(scrapy.Spider):
  name = "product_details_extracter"
  allowed_domains = ["www.shopclues.com", "shopclues.com"]
  start_urls = ["https://www.shopclues.com/29k-mens-black-round-neck-t-shirt-140403237.html?ref=bs_2"]
  #,"https://www.shopclues.com/stylogue-colour-block-half-sleeves-round-neck-t-shirt-pack-of-2-135137895.html?ref=t_0",
  # "https://www.shopclues.com/toyouth-solid-mens-hooded-black-t-shirt-pack-of-1-142856726.html?ref=vv_3"]

  def parse(self, response):
    product_title = response.xpath('//h1/text()').extract_first().strip()
    price = response.xpath('//div[@class="price"]/span[@class="f_price"]/@data-attr').extract_first()
    shipping_charges = response.xpath('//span[@id="shipcharge"]/text()').extract_first()
    image = response.xpath('//img[@id="zoom_picture_gall"]/@src').extract_first()
    print("main product_title", product_title)
    print("main product price", price)
    print("main product shipping charges", shipping_charges)
    print("main product image", image)
    print("\n")
    similar_products_links = response.xpath('//div[@class="tabbing_products"]//a/@href').extract()
    for product_link in similar_products_links:
      print("link \n", "http:"+product_link)
      yield Request("http:"+product_link,callback = self.item_details_request)

  def item_details_request(self,response):
    yield{
    "product_title" : response.xpath('//h1/text()').extract_first().strip(),
    "price" : response.xpath('//div[@class="price"]/span[@class="f_price"]/@data-attr').extract_first(),
    "shipping_charges" : response.xpath('//span[@id="shipcharge"]/text()').extract_first(),
    "image" : response.xpath('//img[@id="zoom_picture_gall"]/@src').extract_first()

    }
