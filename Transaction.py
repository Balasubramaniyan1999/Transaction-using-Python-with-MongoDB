from pymongo import MongoClient
import datetime

MONGODB_URI = 'mongodb://localhost:27017'  # Client id

client = MongoClient(MONGODB_URI)  # connecting with mongoclient

db = client.Transaction  # database name

accounts_collection = db.Account_Details  # collection name


def transaction(from_account,to_account,amount_transfered):
    try:
        initial_sender_balance = accounts_collection.find_one({"Account_No":from_account})  # Getting the sender account detail
        sender_dict = initial_sender_balance["Balance"]                             # Getting the initial sender balance before transaction
        sender_updated_balance = sender_dict - amount_transfered                    # Debitted amount
        updated_sender_balance = accounts_collection.update_one({"Account_No":from_account},{"$set":{"Balance":sender_updated_balance}}) # Update Query for Senders account   
    except Exception as e:
        print(e + "Error occured in Sender account code")
    
    try:
        initial_receiver_balance = accounts_collection.find_one({"Account_No":to_account})    # getting the Receivers  account balance
        receiver_dict = initial_receiver_balance["Balance"]                   # Getting the initial Recviers balance before transaction
        receiver_updated_balance = receiver_dict + amount_transfered     # Credited amount
        updated_receiver_balance = accounts_collection.update_one({"Account_No":to_account},{"$set":{"Balance":receiver_updated_balance}})    # Update Query for Senders account   
    except Exception as e:
        print(e + " Error occured in Receiver account code")


# Paramters
from_account = 9102
to_account = 5102
amount_transfered = 2000

obj1 = transaction(from_account,to_account,amount_transfered)
obj1