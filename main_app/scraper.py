from requests_html import HTML, HTMLSession
import csv


# csv_file = open('winery_scrape.csv', 'w')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['name', 'address', 'desc', 'price'])

session = HTMLSession()
s = session.get('https://www.sonoma.com/businesses/?category=Wineries')
wineries = s.html.find('.article-secondary')
for winery in wineries:
   name = winery.find('.article-body-meta h4')
   address = winery.find('.article-body-meta>h6')
   desc = winery.find('.article-body-entry>p')
   price = winery.find('.bizdetail__price>span')
   print(name[0].text)
   print(address[0].text)
   print(desc[0].text)
   if len(price) > 0: 
      print(price[0].text)
   else:
      print('No price data available')
   # print(price)



# tastings = s.html.find('.article-body-actions li:has(h3)')


# for name in names:
#    print(name.text)

# for address in addresses:
#    print(address.text)

# for des in desc:
#    print(des.text)

# for tasting in tastings:
#    print(tasting.text)

# for price in prices:
#    if price:
#       # print(f'From {price.text}')
#       print(price)
#    else:
#       print('No Price data available')
