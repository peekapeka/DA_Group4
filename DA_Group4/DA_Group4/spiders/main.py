import scrapy

class WebReference(scrapy.Spider):
    name = "web_reference"

    def start_requests(self):
        urls = ['http://172.18.58.238/index.html']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'web_reference-{page}.css'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
