from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json
import smtppy

from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk import Action, Tracker
from typing import Text, Dict, Any, List

import smtplib

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'
		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		budget = tracker.get_slot('budget_type')
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}
		cuisine_code = str(cuisines_dict.get(cuisine.lower()))

		response = zomato.get_restaurants(lat,lon,cuisine_code,budget)

		if "no results" in response:
			response.remove("no results")
		print("responses----------------------------->",response)
		if not response:
			dispatcher.utter_message("-----"+"no results")
		else:
			for i in response[:5]:
				dispatcher.utter_message("-----"+i)
		return [SlotSet('location',loc)]


# class CheckLocation(Action):
# 	def name(self):
# 		return 'action_check_location'
		
# 	def run(self, dispatcher, tracker, domain):
		
# 		loc = tracker.get_slot('location')
# 		if valid_location(loc):
# 			SlotSet('check_op',True)
# 		else:
# 			SlotSet('check_op',False)
# 		return [SlotSet('location',loc)]

class SendMail(Action):
	def name(self):
		return 'action_send_mail'
		
	# def run(self, dispatcher, tracker, domain):
	# 	loc = tracker.get_slot('location')
	# 	cuisine = tracker.get_slot('cuisine')
	# 	sender_id = tracker.get_slot('emailid')
	# 	send_m = smtppy.initialize_app()
	# 	reponse = send_m.send_mail("mkbond777@gmail.com","chiness","delhi")
	# 	dispatcher.utter_message("-----"+response)
	# 	return [SlotSet('emailid',sender_id)]


	def run(self, dispatcher: CollectingDispatcher,
          tracker: Tracker,
         domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
         Subject = "Testing mail"
         Body = "Testing Body"
         Recipient = tracker.get_slot('emailid')


         server = smtplib.SMTP_SSL('smtp.gmail.com', 465) #connect to smtp server
         server.login("upgrad.rasa.chat@gmail.com", "manish@1992")  
         # you can write your mail and or get it from the slots with tracker.get_slot
         # if you are using your email is better that you dont pass it through the code for security u can 
         # set path variables with email and password and use them instead

       
         msg ="Subject: {} \n\n {} " .format(Subject,Body) #creating the message

         server.sendmail(                     #send the email 
         "upgrad.rasa.chat@gmail.com", 
         Recipient, 
         msg)                         
         server.quit()  

         dispatcher.utter_message(" Email sended ! ")
         return [SlotSet("emailid",Recipient)] #just in my case, u can return ntg
