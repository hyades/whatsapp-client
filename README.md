# WhatsApp Client

### Project Aim - 

* Recieve messages from WhatsApp network
* Send messages to WhatsApp network

### Project Dependencies

* [Youwsup 2.0](https://github.com/tgalal/yowsup)
* Uses GPLv3 Licence, so have to include it.


### Steps Followed

##### Step 1 - Register a Mobile number on whatsapp.

* When a mobile is registered, whatsapp generates a numerical code and send it as SMS/Call to the user
* Generating the code
```
$ yowsup-cli registration -d -r sms -c app.conf 
DEBUG:yowsup.common.http.warequest:{'Accept': 'text/json', 'User-Agent': 'WhatsApp/2.12.82 S40Version/14.26 Device/Nokia302'}
DEBUG:yowsup.common.http.warequest:cc=91&in=7299066108&lc=GB&lg=en&sim_mcc=000&sim_mnc=000&method=sms&token=e4e31aa936c3e660d2b3e0d599199c55&id=%E0%90Ji9%EF%A1A%BDgX%D0YO%FFb%8A%14Fk
DEBUG:yowsup.common.http.warequest:Opening connection to v.whatsapp.net
DEBUG:yowsup.common.http.warequest:Sending GET request to /v2/code?cc=91&in=7299066108&lc=GB&lg=en&sim_mcc=000&sim_mnc=000&method=sms&token=e4e31aa936c3e660d2b3e0d599199c55&id=%E0%90Ji9%EF%A1A%BDgX%D0YO%FFb%8A%14Fk
INFO:yowsup.common.http.warequest:{"status":"sent","length":6,"method":"sms","retry_after":1805}

status: sent
retry_after: 1805
length: 6
method: sms

```

