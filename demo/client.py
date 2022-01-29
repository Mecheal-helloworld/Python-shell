import urllib.request
def url_scraper():
  str='http://122.152.210.191:6681'#'http://wdpersonal.xyz:1234/'
  request = urllib.request.Request(str)
  print(request)
  response = urllib.request.urlopen(request)
  print(response)
url_scraper()