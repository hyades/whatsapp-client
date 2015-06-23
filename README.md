# WhatsApp Client

### Project Aim - 

* Recieve messages from WhatsApp network
* Send messages to WhatsApp network

### Project Dependencies

* [Youwsup 2.0](https://github.com/tgalal/yowsup)
* Uses GPLv3 Licence, so have to include it.


### Steps Followed

***As a general note, all personal information is kept in the app.conf file which is not shared here. Generating a app.conf file is pretty simple***
`$ yowsup-cli registration --help-config > app.conf `

##### Step 1 - Register a Mobile number on whatsapp.

* When a mobile is registered, whatsapp generates a numerical code and send it as SMS/Call to the user
* Generating the code 
```
$ yowsup-cli registration -d -r sms -c app.conf 
DEBUG:yowsup.common.http.warequest:{'Accept': 'text/json', 'User-Agent': 'WhatsApp/2.12.82 S40Version/14.26 Device/Nokia302'}
DEBUG:yowsup.common.http.warequest:cc=91&in=<mobile_number>&lc=GB&lg=en&sim_mcc=000&sim_mnc=000&method=sms&token=e4e31aa936c3e660d2b3e0d599199c55&id=%E0%90Ji9%EF%A1A%BDgX%D0YO%FFb%8A%14Fk
DEBUG:yowsup.common.http.warequest:Opening connection to v.whatsapp.net
DEBUG:yowsup.common.http.warequest:Sending GET request to /v2/code?cc=91&in=<mobile_number>&lc=GB&lg=en&sim_mcc=000&sim_mnc=000&method=sms&token=e4e31aa936c3e660d2b3e0d599199c55&id=%E0%90Ji9%EF%A1A%BDgX%D0YO%FFb%8A%14Fk
INFO:yowsup.common.http.warequest:{"status":"sent","length":6,"method":"sms","retry_after":1805}

status: sent
retry_after: 1805
length: 6
method: sms

```
* You will recieve an SMS on the number. Now next step is to pass this on another request. This should give you the `Password` in the `pw` field. You may save this password in the `app.conf` file.

```
$ yowsup-cli registration -d -R <secret_code>  -c app.conf                                                                                                                                    rvm: 
DEBUG:yowsup.common.http.warequest:{'Accept': 'text/json', 'User-Agent': 'WhatsApp/2.12.82 S40Version/14.26 Device/Nokia302'}
DEBUG:yowsup.common.http.warequest:cc=91&in=7299066108&id=%E0%90Ji9%EF%A1A%BDgX%D0YO%FFb%8A%14Fk&code=<secret_code>
DEBUG:yowsup.common.http.warequest:Opening connection to v.whatsapp.net
DEBUG:yowsup.common.http.warequest:Sending GET request to /v2/register?cc=91&in=7299066108&id=%E0%90Ji9%EF%A1A%BDgX%D0YO%FFb%8A%14Fk&code=<secret_code>
INFO:yowsup.common.http.warequest:{"status":"ok","login":"<mobile_number>","pw":"<secret_password>","type":"new","expiration":1466615185,"kind":"free","price":"\u20b9 55","cost":"55.00","currency":"INR","price_expiration":1437974308}

status: ok
kind: free
pw: <secret_password>
price: ₹ 55
price_expiration: 1437974308
currency: INR
cost: 55.00
expiration: 1466615185
login: <mobile_number>
type: new

```


##### Step 2 - Running the listener

* Provide configuration details in `conf.py`
* `cd src`
* `python run.py`