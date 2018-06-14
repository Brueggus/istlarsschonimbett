from util import hook
import requests

@hook.regex("^moin$")
def tbowach(match, nick=''):
  if nick == "mynick":
    url = 'http://www.mysite.com/bettflag/'
    post_fields = {'bett': 'false'}
    r = requests.post(url, data=post_fields)
