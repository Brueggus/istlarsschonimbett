from util import hook
import requests

@hook.regex("n8$")
def tbowach(match, nick=''):
  if nick == "mynick":
    url = 'http://www.mysite.com/bettflag/'
    post_fields = {'bett': 'true'}
    r = requests.post(url, data=post_fields)
