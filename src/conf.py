
############# Yowsup Configuration Sample ###########
#
# ====================
# The file contains info about your WhatsApp account. This is used during registration and login.
# You can define or override all fields in the command line args as well.
#
# Country code. See http://www.ipipi.com/help/telephone-country-codes.htm. This is now required.
cc="91"
#
# Your full phone number including the country code you defined in 'cc', without preceding '+' or '00'
phone="91999999999"
#
# You obtain this password when you register using Yowsup.
password="fhkdshfkhdskhfdskhsdk"


API_KEY="abcdefghij1234567890"
API_PASSWORD="password"
SERVER_ADDR="http://domain.freshdesk.com"
#######################################################

# yowsup-cli registration -d -R 515196  -c app.conf                                                                                                                                    rvm: 
# DEBUG:yowsup.common.http.warequest:{'Accept': 'text/json', 'User-Agent': 'WhatsApp/2.12.82 S40Version/14.26 Device/Nokia302'}
# DEBUG:yowsup.common.http.warequest:cc=91&in=7299066108&id=%E0%90Ji9%EF%A1A%BDgX%D0YO%FFb%8A%14Fk&code=515196
# DEBUG:yowsup.common.http.warequest:Opening connection to v.whatsapp.net
# DEBUG:yowsup.common.http.warequest:Sending GET request to /v2/register?cc=91&in=7299066108&id=%E0%90Ji9%EF%A1A%BDgX%D0YO%FFb%8A%14Fk&code=515196
# INFO:yowsup.common.http.warequest:{"status":"ok","login":"917299066108","pw":"rn2VTbVCFkx+47M5r/zS9VI1f18=","type":"new","expiration":1466615185,"kind":"free","price":"\u20b9 55","cost":"55.00","currency":"INR","price_expiration":1437974308}

# status: ok
# kind: free
# pw: rn2VTbVCFkx+47M5r/zS9VI1f18=
# price:  55
# price_expiration: 1437974308
# currency: INR
# cost: 55.00
# expiration: 1466615185
# login: 917299066108
# type: new
