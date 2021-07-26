from pyshorteners import Shortener
import bitly_api

API_KEY = input('Enter Vaild bitly api_key:')


#Shorten long URL
def one():
    long_url = input('Enter the long URL:')
    url_shortener = Shortener(api_key = API_KEY)
    print("Short URL is {}".format(url_shortener.bitly.short(long_url)))
    Shortener()

#Expand short URL
def two():
    short_url = input('Enter the short URL:')
    url_expander = Shortener(api_key = API_KEY)
    print("Long URL is {}".format(url_expander.bitly.expand(short_url)))



access =input("1.Shorten long URL or 2.Expand short URL\n(use 1 and 2 command to access)\naccess = ")

if access == '1':
    one()
elif access == '2':
    two()
else:
    print("Please Enter valid input")