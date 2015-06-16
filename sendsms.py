import unirest


#site2sms.com account credential.
#userid is your registered phone number on the site.
#password is account password on site.
#phone is the phone number of person whome you want to send sms.



userid = raw_input("Enter site2sms userid :")
password = raw_input("Enter password :")
phone = raw_input("Enter sender phone number :")
message = raw_input("Enter message :")

message = message.replace(" ", "+")   # only single space is allowed

response = unirest.get("https://sphirelabs-site2sms.p.mashape.com/msg/v1/get/index.php?msg="+message+"&pass="+password+"&phone="+phone+"&uid="+userid+"",
  headers={
    "X-Mashape-Key": "qHic5Uw9EBmshCE9J2DFKw4lRsvgp1s2Qzsjsnv8JLvrDWttBm",
    "Accept": "application/json"
  }
)
print "Message sent successfully!"