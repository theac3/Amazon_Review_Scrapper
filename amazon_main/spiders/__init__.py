# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy

class Amazon_Main(scrapy.Spider):
    name = 'Amazon_Main'
    myBaseUrl = "https://www.amazon.com/Gotham-Greens-Butterhead-Lettuce-Clamshell/product-reviews/B00KAR6ERQ/ref=cm_cr_getr_d_paging_btm_prev_1?ie=UTF8&reviewerType=all_reviews&pageNumber="
    start_urls = []

    for i in range(1,3):
        start_urls.append(myBaseUrl+str(i))

    def parse(self, response):
        data = response.css('#cm_cr-review_list')
        
        # collecting name of reviewer
        name = data.css('.a-profile-name')

        #collecting date and country
        date = data.css('.review-date')
 
        # Collecting product star ratings
        star_rating = data.css('.review-rating')
 
        # Collecting user reviews
        comments=response.xpath('//span[@class="a-size-base review-text review-text-content"]/span/text()').extract()

        #verified
        verified=response.xpath('//span[@class="a-size-mini a-color-state a-text-bold"]/text()').extract()
        count = 0
 
        # Combining the results
        for review in star_rating:
            yield{'name': ''.join(name[count].xpath(".//text()").extract()),
            'stars': ''.join(review.xpath('.//text()').extract()),
            'comment': comments[count],
            'date': ''.join(date[count].xpath(".//text()").extract()),
            'verified': verified[count]

            }
            count=count+1