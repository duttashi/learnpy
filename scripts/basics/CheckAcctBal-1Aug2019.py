#import the Python packages for Lambda to use
import boto3
from boto3.dynamodb.conditions import Key, Attr
import json
import decimal
import datetime
from datetime import datetime, timedelta

#start our Lambda runtime here 
def lambda_handler(event_data, lambda_config):

    #Retrieve ANI from inbound callerID
    
    # unhide the below code line when using the test script
    callerId = event_data["sessionAttributes"]["CustomerNumber"]
    
    # unhide the below code line when NOT using the test script
    #callerId = "+60176053920"
    
    #Lex Intent name
    intent_name = event_data['currentIntent']['name']
    
    #Lex session attributes
    session_attributes = event_data['sessionAttributes']
    
    #Establish connection to dynamoDB and retrieve table
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('RICHA_ASHISH_DEV')
    client = boto3.client('lex-models')
    
    #Establish connection to dynamoDB and retrieve table
    #sns_client = boto3.client('sns')
    
    #KeyConditionExpression looks for number that equals ANI of inbound call from a dynamoDB table and saves it to response
    response = table.query(
        KeyConditionExpression=Key('phone_number').eq(callerId)
        )
        
    #will always return list
    items = response.get('Items')
    
    # unhide the below code line when using the test script
    cust_acct_type = event_data["currentIntent"]["slots"]["creditCardType"]
    
    # unhide the below code line when NOT using the test script
    #cust_acct_type = event_data["currentIntent"]["slots"]["ccType"]
    
    #print("cust_acct_type # ", cust_acct_type)
    
    cred_1_due_amount = items[0].get('cc_1_due_amount')
    cred_1_due_amount = decimal.Decimal(cred_1_due_amount)
    acct_balance = cred_1_due_amount
    
    cred_1_due_date = items[0].get('cc_1_due_date')
    cred_1_due_date = decimal.Decimal(cred_1_due_date)
    
    cred_2_due_amount = items[0].get('cc_2_due_amount')
    cred_2_due_amount = decimal.Decimal(cred_2_due_amount)
    
    cred_2_due_date = items[0].get('cc_2_due_date')
    cred_2_due_date = decimal.Decimal(cred_2_due_date)
    
    
    # Calculate days left for credit card payment
    paymt_due_date = 8 # to test zero days for payment
    
    cc1_days_left = paymt_due_date - cred_1_due_date 
    cc2_days_left = paymt_due_date - cred_2_due_date 
    
    # Apparently, the datetime module is not present in AWS Lambda. To make it work, you'll need to zip the libraries and upload them to Lambda
    # dt = date.today() - timedelta(days_to_subtract)
    
    if not items:
        return {'acct_balance_1' : 0, "acct_type": "not available"}
    else:
        
        if(intent_name == "checkCreditCardBal"):
            
            if (cust_acct_type in ("platinum")):
                
                # Determine bill payment date overdue or not?
                
                if(cc1_days_left > 0):
                    
                    message = 'You have ' + str(acct_balance) + ' ringgit left on your ' + cust_acct_type + ' account.' + 'And you have ' + str(cc1_days_left) + ' day left to settle the bills.'
                
                elif(cc1_days_left==0):
                    
                    message = 'You have ' + str(acct_balance) + ' ringgit left on your ' + cust_acct_type + ' account.' + "And, today is last day to pay bills!"
                    
                elif(cc1_days_left < 0):
                    temp = cc1_days_left * -1
                    message = 'You have ' + str(acct_balance) + ' ringgit left on your ' + cust_acct_type + ' account.' + 'You are ' + str(temp) + ' day behind credit bill payment!'
                
                else:
                   message = "Invalid!! "
                
                return close(session_attributes, "Fulfilled", '<speak>{}</speak>'.format(message))
                
            elif (cust_acct_type in ("signature")):
                
                # Determine bill payment date overdue or not?
                
                if(cc2_days_left > 0):
                
                    message = 'You have ' + str(acct_balance) + ' ringgit left on your ' + cust_acct_type + ' account.' + 'And you have ' + str(cc2_days_left) + ' day left to settle the bills.'
                
                elif(cc2_days_left == 0):
                
                    message = 'You have ' + str(acct_balance) + ' ringgit left on your ' + cust_acct_type + ' account.' + "And, today is last day to pay bills!"
                    
                elif (cc2_days_left < 0):
                    temp = cc2_days_left * -1 
                    print("cred_2_due_date = ", cred_2_due_date, " cc2_days_left= ", cc2_days_left, " temp= ", temp)
                    message = 'You have ' + str(acct_balance) + ' ringgit left on your ' + cust_acct_type + ' account.' + 'You are ' + str(temp) + ' day behind credit bill payment!'
                
                else:
                   message = "Invalid!! "
                    
                return close(session_attributes, "Fulfilled", '<speak>{}</speak>'.format(message))
            
def close(session_attributes, fulfillment_state, message):
    response = {
    'sessionAttributes': session_attributes,
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled", 
            "message": {
                "contentType": "SSML",
                "content": message
                }
            }
        }
    return response
    
def build_response_message(message_content):
    return {"contentType": "PlainText", "content": message_content}
    
def elicit_slot(session_attributes, intent_name, slots, slot_to_elicit, message):
    return {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'ElicitSlot',
            'intentName': intent_name,
            'slots': slots,
            'slotToElicit': slot_to_elicit,
            'message': {
                "contentType": "SSML",
                "content": message
                }
            }
        }
