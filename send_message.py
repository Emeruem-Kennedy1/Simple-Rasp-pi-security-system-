from twilio.rest import Client 

def sendMsg(message, phoneNumber):
    account_sid = 'Enter key here' 
    auth_token = 'Enter Key here' 
    client = Client(account_sid, auth_token) 
    
    message = client.messages.create( 
                                from_='whatsapp:+14155238886',  
                                body=message,      
                                to='whatsapp:{}'.format(phoneNumber) 
                            ) 
    
    print(message.sid)
