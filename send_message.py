from twilio.rest import Client 

def sendMsg(message, phoneNumber):
    account_sid = 'AC23eb77b5e31bb7592f946a6016540fdb' 
    auth_token = 'b52e849233c04f977fba76c753128a24' 
    client = Client(account_sid, auth_token) 
    
    message = client.messages.create( 
                                from_='whatsapp:+14155238886',  
                                body=message,      
                                to='whatsapp:{}'.format(phoneNumber) 
                            ) 
    
    print(message.sid)
