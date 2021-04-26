
import requests
import json
import urllib
import tensorflow as tf 


#free API code = G5POEK75Q6FFQT9N
url= "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=15min&apikey=G5POEK75Q6FFQT9N"

msft_requests = requests.get(url)

hello = tf.constant("Helloworld2")
sess = tf.Session()
print(sess.run(hello))

#print (msft_requests.json())
print ("Hello World")
print ("testing 2")
