from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

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
        config = {"user_key": "f4924dc9ad672ee8c4f8c84743301af5"}
        zomato = zomatopy.initialize_app(config)
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        budget = tracker.get_slot('budget_type')
        location_detail = zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        lat = d1["location_suggestions"][0]["latitude"]
        lon = d1["location_suggestions"][0]["longitude"]
        cuisines_dict = {'mexican': 73, 'chinese': 25, 'cafe': 30, 'italian': 55, 'american': 1, 'north indian': 50,
                         'south indian': 85}
        cuisine_code = str(cuisines_dict.get(cuisine.lower()))

        response,avg_cost = zomato.get_restaurants(lat, lon, cuisine_code, budget)

        if "no results" in response:
            response.remove("no results")
            avg_cost.remove("no results")
        if not response:
            dispatcher.utter_message("-----" + "no results")
            return [SlotSet('restaurants', None)]
        else:
            for i in response[:5]:
                dispatcher.utter_message("-----" + i)
            mail_response = [r + " which has average cost for two people as " + str(a) for r,a in zip(response,avg_cost)]
            return [SlotSet('restaurants', mail_response[:10])]


class CheckLocation(Action):
    def name(self):
        return 'action_check_location'

    def run(self, dispatcher, tracker, domain):
        cities = ["agra","ajmer","aligarh","amravati","amritsar","asansol","aurangabad","bareilly","belgaum","bhavnagar","bhiwandi","bhopal","bhubaneswar","bikaner","bilaspur","bokarosteelcity","chandigarh","coimbatore","cuttack","dehradun","dhanbad","bhilai","durgapur","dindigul","erode","faridabad","firozabad","ghaziabad","gorakhpur","gulbarga","guntur","gwalior","gurgaon","guwahati","hamirpur","hubli–dharwad","indore","jabalpur","jaipur","jalandhar","jammu","jamnagar","jamshedpur","jhansi","jodhpur","kakinada","kannur","kanpur","karnal","kochi","kolhapur","kollam","kozhikode","kurnool","ludhiana","lucknow","madurai","malappuram","mathura","mangalore","meerut","moradabad","mysore","nagpur","nanded","nashik","nellore","noida","patna","pondicherry","purulia","prayagraj","raipur","rajkot","rajahmundry","ranchi","rourkela","salem","sangli","shimla","siliguri","solapur","srinagar","surat","thanjavur","thiruvananthapuram","thrissur","tiruchirappalli","tirunelveli","ujjain","bijapur","vadodara","varanasi","vasai-virarcity","vijayawada","visakhapatnam","vellore","warangal","ahmedabad","bengaluru","chennai","delhi","hyderabad","kolkata","mumbai","pune"]
        loc = tracker.get_slot('location')
        if loc.lower() in cities:
            return [SlotSet('location', loc),SlotSet('location_found', "found")]
        else:
            return [SlotSet('location', None),SlotSet('location_found', "not_found")]


class SendMail(Action):
    def name(self):
        return 'action_send_mail'

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        restaurants = tracker.get_slot('restaurants')
        recipient = tracker.get_slot('emailid')

        smtp_obj = smtppy.initialize_app()
        response = smtp_obj.send_mail(recipient,cuisine,loc,restaurants)

        dispatcher.utter_message("----------------"+response)
        return [SlotSet("emailid", recipient)]  # just in my case, u can return ntg
