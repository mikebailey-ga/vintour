from requests_html import HTML, HTMLSession
import json


data = []

session = HTMLSession()
pk = 1
a = session.get('https://www.napavalley.com/businesses/?category=Wineries')
wineries = a.html.find('.article-secondary')
for winery in wineries:
   price_find = winery.find('.bizdetail__price>span')
   price = None
   if len(price_find):
      price = f'From {price_find[0].text}'
   else:
      price = 'No price data available'
   item = {}
   item['pk'] = pk
   item['model'] = 'main_app.Winery'
   item['fields'] = {
      'name': winery.find('.article-body-meta h4')[0].text,
      'address': winery.find('.article-body-meta>h6')[0].text,
      'desc': winery.find('.article-body-entry>p')[0].text,
      'price': price
   }
   data.append(item)
   pk += 1

b = session.get('https://www.napavalley.com/businesses/?category=Wineries&page=2')
wineries = b.html.find('.article-secondary')
for winery in wineries:
   price_find = winery.find('.bizdetail__price>span')
   price = None
   if len(price_find):
      price = f'From {price_find[0].text}'
   else:
      price = 'No price data available'
   item = {}
   item['pk'] = pk
   item['model'] = 'main_app.Winery'
   item['fields'] = {
      'name': winery.find('.article-body-meta h4')[0].text,
      'address': winery.find('.article-body-meta>h6')[0].text,
      'desc': winery.find('.article-body-entry>p')[0].text,
      'price': price
   }
   data.append(item)
   pk += 1


c = session.get('https://www.napavalley.com/businesses/?category=Wineries&page=3')
wineries = c.html.find('.article-secondary')
for winery in wineries:
   price_find = winery.find('.bizdetail__price>span')
   price = None
   if len(price_find):
      price = f'From {price_find[0].text}'
   else:
      price = 'No price data available'
   item = {}
   item['pk'] = pk
   item['model'] = 'main_app.Winery'
   item['fields'] = {
      'name': winery.find('.article-body-meta h4')[0].text,
      'address': winery.find('.article-body-meta>h6')[0].text,
      'desc': winery.find('.article-body-entry>p')[0].text,
      'price': price
   }
   data.append(item)
   pk += 1


d = session.get('https://www.napavalley.com/businesses/?category=Wineries&page=4')
wineries = d.html.find('.article-secondary')
for winery in wineries:
   price_find = winery.find('.bizdetail__price>span')
   price = None
   if len(price_find):
      price = f'From {price_find[0].text}'
   else:
      price = 'No price data available'
   item = {}
   item['pk'] = pk
   item['model'] = 'main_app.Winery'
   item['fields'] = {
      'name': winery.find('.article-body-meta h4')[0].text,
      'address': winery.find('.article-body-meta>h6')[0].text,
      'desc': winery.find('.article-body-entry>p')[0].text,
      'price': price
   }
   data.append(item)
   pk += 1



e = session.get('https://www.napavalley.com/businesses/?category=Wineries&page=5')
wineries = e.html.find('.article-secondary')
for winery in wineries:
   price_find = winery.find('.bizdetail__price>span')
   price = None
   if len(price_find):
      price = f'From {price_find[0].text}'
   else:
      price = 'No price data available'
   item = {}
   item['pk'] = pk
   item['model'] = 'main_app.Winery'
   item['fields'] = {
      'name': winery.find('.article-body-meta h4')[0].text,
      'address': winery.find('.article-body-meta>h6')[0].text,
      'desc': winery.find('.article-body-entry>p')[0].text,
      'price': price
   }
   data.append(item)
   pk += 1


f = session.get('https://www.napavalley.com/businesses/?category=Wineries&page=6')
wineries = f.html.find('.article-secondary')
for winery in wineries:
   price_find = winery.find('.bizdetail__price>span')
   price = None
   if len(price_find):
      price = f'From {price_find[0].text}'
   else:
      price = 'No price data available'
   item = {}
   item['pk'] = pk
   item['model'] = 'main_app.Winery'
   item['fields'] = {
      'name': winery.find('.article-body-meta h4')[0].text,
      'address': winery.find('.article-body-meta>h6')[0].text,
      'desc': winery.find('.article-body-entry>p')[0].text,
      'price': price
   }
   data.append(item)
   pk += 1



g = session.get('https://www.napavalley.com/businesses/?category=Wineries&page=7')
wineries = g.html.find('.article-secondary')
for winery in wineries:
   price_find = winery.find('.bizdetail__price>span')
   price = None
   if len(price_find):
      price = f'From {price_find[0].text}'
   else:
      price = 'No price data available'
   item = {}
   item['pk'] = pk
   item['model'] = 'main_app.Winery'
   item['fields'] = {
      'name': winery.find('.article-body-meta h4')[0].text,
      'address': winery.find('.article-body-meta>h6')[0].text,
      'desc': winery.find('.article-body-entry>p')[0].text,
      'price': price
   }
   data.append(item)
   pk += 1


h = session.get('https://www.napavalley.com/businesses/?category=Wineries&page=8')
wineries = h.html.find('.article-secondary')
for winery in wineries:
   price_find = winery.find('.bizdetail__price>span')
   price = None
   if len(price_find):
      price = f'From {price_find[0].text}'
   else:
      price = 'No price data available'
   item = {}
   item['pk'] = pk
   item['model'] = 'main_app.Winery'
   item['fields'] = {
      'name': winery.find('.article-body-meta h4')[0].text,
      'address': winery.find('.article-body-meta>h6')[0].text,
      'desc': winery.find('.article-body-entry>p')[0].text,
      'price': price
   }
   data.append(item)
   pk += 1


i = session.get('https://www.napavalley.com/businesses/?category=Wineries&page=9')
wineries = i.html.find('.article-secondary')
for winery in wineries:
   price_find = winery.find('.bizdetail__price>span')
   price = None
   if len(price_find):
      price = f'From {price_find[0].text}'
   else:
      price = 'No price data available'
   item = {}
   item['pk'] = pk
   item['model'] = 'main_app.Winery'
   item['fields'] = {
      'name': winery.find('.article-body-meta h4')[0].text,
      'address': winery.find('.article-body-meta>h6')[0].text,
      'desc': winery.find('.article-body-entry>p')[0].text,
      'price': price
   }
   data.append(item)
   pk += 1


j = session.get('https://www.napavalley.com/businesses/?category=Wineries&page=10')
wineries = j.html.find('.article-secondary')
for winery in wineries:
   price_find = winery.find('.bizdetail__price>span')
   price = None
   if len(price_find):
      price = f'From {price_find[0].text}'
   else:
      price = 'No price data available'
   item = {}
   item['pk'] = pk
   item['model'] = 'main_app.Winery'
   item['fields'] = {
      'name': winery.find('.article-body-meta h4')[0].text,
      'address': winery.find('.article-body-meta>h6')[0].text,
      'desc': winery.find('.article-body-entry>p')[0].text,
      'price': price
   }
   data.append(item)
   pk += 1


k = session.get('https://www.napavalley.com/businesses/?category=Wineries&page=11')
wineries = k.html.find('.article-secondary')
for winery in wineries:
   price_find = winery.find('.bizdetail__price>span')
   price = None
   if len(price_find):
      price = f'From {price_find[0].text}'
   else:
      price = 'No price data available'
   item = {}
   item['model'] = 'main_app.winery'
   item['pk'] = pk
   item['fields'] = {
      'name': winery.find('.article-body-meta h4')[0].text,
      'address': winery.find('.article-body-meta>h6')[0].text,
      'desc': winery.find('.article-body-entry>p')[0].text,
      'price': price
   }
   data.append(item)
   pk += 1

l = session.get('https://www.napavalley.com/businesses/?category=Wineries&page=12')
wineries = l.html.find('.article-secondary')
for winery in wineries:
   price_find = winery.find('.bizdetail__price>span')
   price = None
   if len(price_find):
      price = f'From {price_find[0].text}'
   else:
      price = 'No price data available'
   item = {}
   item['model'] = 'main_app.winery'
   item['pk'] = pk
   item['fields'] = {
      'name': winery.find('.article-body-meta h4')[0].text,
      'address': winery.find('.article-body-meta>h6')[0].text,
      'desc': winery.find('.article-body-entry>p')[0].text,
      'price': price
   }
   data.append(item)
   pk += 1

m = session.get('https://www.napavalley.com/businesses/?category=Wineries&page=13')
wineries = m.html.find('.article-secondary')
for winery in wineries:
   price_find = winery.find('.bizdetail__price>span')
   price = None
   if len(price_find):
      price = f'From {price_find[0].text}'
   else:
      price = 'No price data available'
   item = {}
   item['model'] = 'main_app.winery'
   item['pk'] = pk
   item['fields'] = {
      'name': winery.find('.article-body-meta h4')[0].text,
      'address': winery.find('.article-body-meta>h6')[0].text,
      'desc': winery.find('.article-body-entry>p')[0].text,
      'price': price
   }
   data.append(item)
   pk += 1

n = session.get('https://www.sonoma.com/businesses?category=Wineries')
wineries = n.html.find('.article-secondary')
for winery in wineries:
   price_find = winery.find('.bizdetail__price>span')
   price = None
   if len(price_find):
      price = f'From {price_find[0].text}'
   else:
      price = 'No price data available'
   item = {}
   item['pk'] = pk
   item['model'] = 'main_app.Winery'
   item['fields'] = {
      'name': winery.find('.article-body-meta h4')[0].text,
      'address': winery.find('.article-body-meta>h6')[0].text,
      'desc': winery.find('.article-body-entry>p')[0].text,
      'price': price
   }
   data.append(item)
   pk += 1

o = session.get('https://www.sonoma.com/businesses?category=Wineries&page=2')
wineries = o.html.find('.article-secondary')
for winery in wineries:
   price_find = winery.find('.bizdetail__price>span')
   price = None
   if len(price_find):
      price = f'From {price_find[0].text}'
   else:
      price = 'No price data available'
   item = {}
   item['pk'] = pk
   item['model'] = 'main_app.Winery'
   item['fields'] = {
      'name': winery.find('.article-body-meta h4')[0].text,
      'address': winery.find('.article-body-meta>h6')[0].text,
      'desc': winery.find('.article-body-entry>p')[0].text,
      'price': price
   }
   data.append(item)
   pk += 1

p = session.get('https://www.sonoma.com/businesses?category=Wineries&page=3')
wineries = p.html.find('.article-secondary')
for winery in wineries:
   price_find = winery.find('.bizdetail__price>span')
   price = None
   if len(price_find):
      price = f'From {price_find[0].text}'
   else:
      price = 'No price data available'
   item = {}
   item['pk'] = pk
   item['model'] = 'main_app.Winery'
   item['fields'] = {
      'name': winery.find('.article-body-meta h4')[0].text,
      'address': winery.find('.article-body-meta>h6')[0].text,
      'desc': winery.find('.article-body-entry>p')[0].text,
      'price': price
   }
   data.append(item)
   pk += 1

q = session.get('https://www.sonoma.com/businesses?category=Wineries&page=4')
wineries = q.html.find('.article-secondary')
for winery in wineries:
   price_find = winery.find('.bizdetail__price>span')
   price = None
   if len(price_find):
      price = f'From {price_find[0].text}'
   else:
      price = 'No price data available'
   item = {}
   item['pk'] = pk
   item['model'] = 'main_app.Winery'
   item['fields'] = {
      'name': winery.find('.article-body-meta h4')[0].text,
      'address': winery.find('.article-body-meta>h6')[0].text,
      'desc': winery.find('.article-body-entry>p')[0].text,
      'price': price
   }
   data.append(item)
   pk += 1

r = session.get('https://www.sonoma.com/businesses?category=Wineries&page=5')
wineries = r.html.find('.article-secondary')
for winery in wineries:
   price_find = winery.find('.bizdetail__price>span')
   price = None
   if len(price_find):
      price = f'From {price_find[0].text}'
   else:
      price = 'No price data available'
   item = {}
   item['pk'] = pk
   item['model'] = 'main_app.Winery'
   item['fields'] = {
      'name': winery.find('.article-body-meta h4')[0].text,
      'address': winery.find('.article-body-meta>h6')[0].text,
      'desc': winery.find('.article-body-entry>p')[0].text,
      'price': price
   }
   data.append(item)
   pk += 1

s = session.get('https://www.sonoma.com/businesses?category=Wineries&page=6')
wineries = s.html.find('.article-secondary')
for winery in wineries:
   price_find = winery.find('.bizdetail__price>span')
   price = None
   if len(price_find):
      price = f'From {price_find[0].text}'
   else:
      price = 'No price data available'
   item = {}
   item['pk'] = pk
   item['model'] = 'main_app.Winery'
   item['fields'] = {
      'name': winery.find('.article-body-meta h4')[0].text,
      'address': winery.find('.article-body-meta>h6')[0].text,
      'desc': winery.find('.article-body-entry>p')[0].text,
      'price': price
   }
   data.append(item)
   pk += 1

t = session.get('https://www.sonoma.com/businesses?category=Wineries&page=7')
wineries = t.html.find('.article-secondary')
for winery in wineries:
   price_find = winery.find('.bizdetail__price>span')
   price = None
   if len(price_find):
      price = f'From {price_find[0].text}'
   else:
      price = 'No price data available'
   item = {}
   item['pk'] = pk
   item['model'] = 'main_app.Winery'
   item['fields'] = {
      'name': winery.find('.article-body-meta h4')[0].text,
      'address': winery.find('.article-body-meta>h6')[0].text,
      'desc': winery.find('.article-body-entry>p')[0].text,
      'price': price
   }
   data.append(item)
   pk += 1

u = session.get('https://www.sonoma.com/businesses?category=Wineries&page=8')
wineries = u.html.find('.article-secondary')
for winery in wineries:
   price_find = winery.find('.bizdetail__price>span')
   price = None
   if len(price_find):
      price = f'From {price_find[0].text}'
   else:
      price = 'No price data available'
   item = {}
   item['pk'] = pk
   item['model'] = 'main_app.Winery'
   item['fields'] = {
      'name': winery.find('.article-body-meta h4')[0].text,
      'address': winery.find('.article-body-meta>h6')[0].text,
      'desc': winery.find('.article-body-entry>p')[0].text,
      'price': price
   }
   data.append(item)
   pk += 1

v = session.get('https://www.sonoma.com/businesses?category=Wineries&page=9')
wineries = v.html.find('.article-secondary')
for winery in wineries:
   price_find = winery.find('.bizdetail__price>span')
   price = None
   if len(price_find):
      price = f'From {price_find[0].text}'
   else:
      price = 'No price data available'
   item = {}
   item['pk'] = pk
   item['model'] = 'main_app.Winery'
   item['fields'] = {
      'name': winery.find('.article-body-meta h4')[0].text,
      'address': winery.find('.article-body-meta>h6')[0].text,
      'desc': winery.find('.article-body-entry>p')[0].text,
      'price': price
   }
   data.append(item)
   pk += 1

w = session.get('https://www.sonoma.com/businesses?category=Wineries&page=10')
wineries = w.html.find('.article-secondary')
for winery in wineries:
   price_find = winery.find('.bizdetail__price>span')
   price = None
   if len(price_find):
      price = f'From {price_find[0].text}'
   else:
      price = 'No price data available'
   item = {}
   item['pk'] = pk
   item['model'] = 'main_app.Winery'
   item['fields'] = {
      'name': winery.find('.article-body-meta h4')[0].text,
      'address': winery.find('.article-body-meta>h6')[0].text,
      'desc': winery.find('.article-body-entry>p')[0].text,
      'price': price
   }
   data.append(item)
   pk += 1

x = session.get('https://www.sonoma.com/businesses?category=Wineries&page=11')
wineries = x.html.find('.article-secondary')
for winery in wineries:
   price_find = winery.find('.bizdetail__price>span')
   price = None
   if len(price_find):
      price = f'From {price_find[0].text}'
   else:
      price = 'No price data available'
   item = {}
   item['pk'] = pk
   item['model'] = 'main_app.Winery'
   item['fields'] = {
      'name': winery.find('.article-body-meta h4')[0].text,
      'address': winery.find('.article-body-meta>h6')[0].text,
      'desc': winery.find('.article-body-entry>p')[0].text,
      'price': price
   }
   data.append(item)
   pk += 1



with open('winery_scrape.json', 'w') as writeJSON:
   json.dump(data, writeJSON, ensure_ascii=False) 

