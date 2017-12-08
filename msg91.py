import http.client

def check_balance():
	conn = http.client.HTTPConnection("control.msg91.com")
	conn.request("GET", "/api/balance.php?authkey=184608AXJHchldS5a12eeb2&type=4")
	res = conn.getresponse()
	data = res.read()
	return data.decode("utf-8")

#print(check_balance())

def send_SMS(mobile, message):
	conn = http.client.HTTPConnection("api.msg91.com")
	url  = "/api/sendhttp.php?sender=EQRATC&route=4&mobiles="+mobile+"&authkey=184608AXJHchldS5a12eeb2&country=91&message="+message
	conn.request("GET", url)
	res = conn.getresponse()
	data = res.read()
	return data.decode("utf-8")
	
#print(send_SMS('9488631135', 'EQRA Test Message'))


# def send_SMS_POST():
# 	conn = http.client.HTTPConnection("api.msg91.com")
# 	payload = "{ \"sender\": \"SOCKET\", \"route\": \"4\", \"country\": \"91\", \"sms\": [ { \"message\": \"Message1\", \"to\": [ \"98260XXXXX\", \"98261XXXXX\" ] }, { \"message\": \"Message2\", \"to\": [ \"98260XXXXX\", \"98261XXXXX\" ] } ] }"
# 	headers = {
#     'content-type': "application/json",
#     'authkey': "184608AXJHchldS5a12eeb2"
#     }
#     conn.request("POST", "/api/v2/sendsms", payload, headers)
#     res = conn.getresponse()
# 	data = res.read()
# 	return data.decode("utf-8")