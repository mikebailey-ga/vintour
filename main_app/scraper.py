from requests_html import HTML, HTMLSession
import csv


csv_file = open('winery_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['name', 'address', 'desc', 'price'])

session = HTMLSession()
a = session.get('https://www.sonoma.com/businesses?category=Wineries')
wineries = a.html.find('.article-secondary')
for winery in wineries:
   name = winery.find('.article-body-meta h4')[0].text
   address = winery.find('.article-body-meta>h6')[0].text
   desc = winery.find('.article-body-entry>p')[0].text
   price_find = winery.find('.bizdetail__price>span')
   price = None
   if len(price_find):
      price = f'From {price_find[0].text}'
   else:
      price = 'No price data available'
   csv_writer.writerow([name, address, desc, price])

b = session.get('https://www.sonoma.com/businesses?category=Wineries&page=2')
wineries = b.html.find('.article-secondary')
for winery in wineries:
   name = winery.find('.article-body-meta h4')[0].text
   address = winery.find('.article-body-meta>h6')[0].text
   desc = winery.find('.article-body-entry>p')[0].text
   price_find = winery.find('.bizdetail__price>span')
   price = None
   if len(price_find):
      price = f'From {price_find[0].text}'
   else:
      price = 'No price data available'
   csv_writer.writerow([name, address, desc, price])


c = session.get('https://www.sonoma.com/businesses?category=Wineries&page=3')
wineries = c.html.find('.article-secondary')
for winery in wineries:
   name = winery.find('.article-body-meta h4')[0].text
   address = winery.find('.article-body-meta>h6')[0].text
   desc = winery.find('.article-body-entry>p')[0].text
   price_find = winery.find('.bizdetail__price>span')
   price = None
   if len(price_find):
      price = f'From {price_find[0].text}'
   else:
      price = 'No price data available'
   csv_writer.writerow([name, address, desc, price])


d = session.get('https://www.sonoma.com/dusinesses?category=Wineries&page=4')
wineries = d.html.find('.article-secondary')
for winery in wineries:
   name = winery.find('.article-body-meta h4')[0].text
   address = winery.find('.article-body-meta>h6')[0].text
   desc = winery.find('.article-body-entry>p')[0].text
   price_find = winery.find('.bizdetail__price>span')
   price = None
   if len(price_find):
      price = f'From {price_find[0].text}'
   else:
      price = 'No price data available'
   csv_writer.writerow([name, address, desc, price])



e = session.get('https://www.sonoma.com/businesses?category=Wineries&page=5')
wineries = e.html.find('.article-secondary')
for winery in wineries:
   name = winery.find('.article-body-meta h4')[0].text
   address = winery.find('.article-body-meta>h6')[0].text
   desc = winery.find('.article-body-entry>p')[0].text
   price_find = winery.find('.bizdetail__price>span')
   price = None
   if len(price_find):
      price = f'From {price_find[0].text}'
   else:
      price = 'No price data available'
   csv_writer.writerow([name, address, desc, price])


f = session.get('https://www.sonoma.com/businesses?category=Wineries&page=6')
wineries = f.html.find('.article-secondary')
for winery in wineries:
   name = winery.find('.article-body-meta h4')[0].text
   address = winery.find('.article-body-meta>h6')[0].text
   desc = winery.find('.article-body-entry>p')[0].text
   price_find = winery.find('.bizdetail__price>span')
   price = None
   if len(price_find):
      price = f'From {price_find[0].text}'
   else:
      price = 'No price data available'
   csv_writer.writerow([name, address, desc, price])



g = session.get('https://www.sonoma.com/businesses?category=Wineries&page=7')
wineries = g.html.find('.article-secondary')
for winery in wineries:
   name = winery.find('.article-body-meta h4')[0].text
   address = winery.find('.article-body-meta>h6')[0].text
   desc = winery.find('.article-body-entry>p')[0].text
   price_find = winery.find('.bizdetail__price>span')
   price = None
   if len(price_find):
      price = f'From {price_find[0].text}'
   else:
      price = 'No price data available'
   csv_writer.writerow([name, address, desc, price])


h = session.get('https://www.sonoma.com/businesses?category=Wineries&page=8')
wineries = h.html.find('.article-secondary')
for winery in wineries:
   name = winery.find('.article-body-meta h4')[0].text
   address = winery.find('.article-body-meta>h6')[0].text
   desc = winery.find('.article-body-entry>p')[0].text
   price_find = winery.find('.bizdetail__price>span')
   price = None
   if len(price_find):
      price = f'From {price_find[0].text}'
   else:
      price = 'No price data available'
   csv_writer.writerow([name, address, desc, price])


i = session.get('https://www.sonoma.com/businesses?category=Wineries&page=9')
wineries = i.html.find('.article-secondary')
for winery in wineries:
   name = winery.find('.article-body-meta h4')[0].text
   address = winery.find('.article-body-meta>h6')[0].text
   desc = winery.find('.article-body-entry>p')[0].text
   price_find = winery.find('.bizdetail__price>span')
   price = None
   if len(price_find):
      price = f'From {price_find[0].text}'
   else:
      price = 'No price data available'
   csv_writer.writerow([name, address, desc, price])


j = session.get('https://www.sonoma.com/businesses?category=Wineries&page=10')
wineries = j.html.find('.article-secondary')
for winery in wineries:
   name = winery.find('.article-body-meta h4')[0].text
   address = winery.find('.article-body-meta>h6')[0].text
   desc = winery.find('.article-body-entry>p')[0].text
   price_find = winery.find('.bizdetail__price>span')
   price = None
   if len(price_find):
      price = f'From {price_find[0].text}'
   else:
      price = 'No price data available'
   csv_writer.writerow([name, address, desc, price])


k = session.get('https://www.sonoma.com/businesses?category=Wineries&page=11')
wineries = k.html.find('.article-secondary')
for winery in wineries:
   name = winery.find('.article-body-meta h4')[0].text
   address = winery.find('.article-body-meta>h6')[0].text
   desc = winery.find('.article-body-entry>p')[0].text
   price_find = winery.find('.bizdetail__price>span')
   price = None
   if len(price_find):
      price = f'From {price_find[0].text}'
   else:
      price = 'No price data available'
   csv_writer.writerow([name, address, desc, price])



csv_file.close() 

