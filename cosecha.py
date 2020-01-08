from tweepy import Stream #tweepy es la libreria que trae tweets desde la API de Twitter (requiere ser instalada primero)
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json #Libreria para manejar archivos JSON

import pymongo
from pymongo import MongoClient


###Credenciales de la cuenta de Twitter########################
ckey = "f0nqxD2gg6SkVfjadkrnXioUo"
csecret = "o8FV2jOs1BKYgoePXN5yTTb0F28ZwTGZYxxKKha2zHeGzXelhY"
atoken = "115946548-hFaQfpQsGtXz5OMd0ts3lJuyOs12wFqsnb4JoYYk"
asecret = "4etAj30jzc6gU5swMlnY6i0dnTKhxoj3G26U0G4MAuIBK"
#####################################

class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            dictTweet["_id"] = str(dictTweet['id'])

            collection.insert_one(dictTweet)

            print ("Guardado " + "=> " + dictTweet["_id"])
        except:
            print ("Documento ya existe")
            pass
        return True
    
    def on_error(self, status):
        print (status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

#Setear la URL del servidor de mongodb atlas
MONGO_URI = 'mongodb+srv://admin:admin12345@cluster0-7dmzz.mongodb.net/test?retryWrites=true&w=majority'

client = MongoClient(MONGO_URI)

db = client['mineria']
collection = db['datos']


#Aqui se define el bounding box con los limites geograficos donde recolectar los tweets
twitterStream.filter(track=["ecuador","quito","epn","ecuador","la zona"])
#twitterStream.filter(locations=[-78.586922,-0.395161,-78.274155,0.021973])