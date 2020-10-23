## complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "gaya"}
    - slot{"location": "gaya"}
    - action_check_location
    - slot{"location":null}
    - slot{"location_found":"not_found"}
    - utter_location_notfound
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget_type": "high"}
    - slot{"budget_type": "high"}
    - action_search_restaurants
    - slot{"restaurants": ["Coppetto Artisan Gelato in Shop 3, Plot 117, Muzzafar Manor, Waterfield Road, Linking Road, Bandra West, delhi has been rated 4.6","Firangi Bake in Nalasopara, delhi has been rated 4.6","Theobroma in Shop 8, Ground Floor, City Park Building, Central Avenue, Hiranandani Business Park, Phase 2 Dmart, Powai, delhi has been rated 4.5","Theobroma in 24, Cusrow Baug, Shahid Bhagat Singh Road, Colaba Causeway, Colaba, delhi has been rated 4.5","Food And Taste Theory in Shop 25, 2nd Floor, Phoenix Market City, LBS Marg, Kurla, delhi has been rated 4.5"]}
    - utter_ask_mail_send
* affirm
    - utter_ask_mailid
* mailid{"emailid":"abc@yahoo.com"}
    - slot{"emailid": "abc@yahoo.com"}
    - action_send_mail
    - slot{"emailid": "abc@yahoo.com"}
* affirm
    - utter_goodbye

## location specified
* greet
    - utter_greet
* restaurant_search{"location": "diliya"}
    - slot{"location": "diliya"}
    - action_check_location
    - slot{"location":null}
    - slot{"location_found":"not_found"}
    - utter_location_notfound
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget_type": "medium"}
    - slot{"budget_type": "medium"}
    - action_search_restaurants
    - slot{"restaurants": ["Coppetto Artisan Gelato in Shop 3, Plot 117, Muzzafar Manor, Waterfield Road, Linking Road, Bandra West, delhi has been rated 4.6","Firangi Bake in Nalasopara, delhi has been rated 4.6","Theobroma in Shop 8, Ground Floor, City Park Building, Central Avenue, Hiranandani Business Park, Phase 2 Dmart, Powai, delhi has been rated 4.5","Theobroma in 24, Cusrow Baug, Shahid Bhagat Singh Road, Colaba Causeway, Colaba, delhi has been rated 4.5","Food And Taste Theory in Shop 25, 2nd Floor, Phoenix Market City, LBS Marg, Kurla, delhi has been rated 4.5"]}
    - utter_ask_mail_send
* affirm
    - utter_ask_mailid
* mailid{"emailid":"abc@yahoo.com"}
    - slot{"emailid": "abc@yahoo.com"}
    - action_send_mail
    - slot{"emailid": "abc@yahoo.com"}
* affirm
    - utter_goodbye
    - export

## complete path 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location":"delhi"}
    - slot{"location_found":"found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search{"budget_type": "low"}
    - slot{"budget_type": "low"}
    - action_search_restaurants
    - slot{"restaurants": null}
* affirm
    - utter_goodbye
    - export

## complete path 3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "patna"}
    - slot{"location": "patna"}
    - action_check_location
    - slot{"location":"patna"}
    - slot{"location_found":"found"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget_type": "medium"}
    - slot{"budget_type": "medium"}
    - action_search_restaurants
    - utter_ask_mail_send
* affirm
    - utter_ask_mailid
* mailid{"emailid":"abc@yahoo.com"}
    - slot{"emailid": "abc@yahoo.com"}
    - action_send_mail
    - slot{"emailid": "abc@yahoo.com"}
* goodbye
    - utter_goodbye

## happy_path
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai","budget_type": "high"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - slot{"budget_type": "high"}
    - action_check_location
    - slot{"location":"mumbai"}
    - slot{"location_found":"found"}
    - action_search_restaurants
    - slot{"restaurants": ["Coppetto Artisan Gelato in Shop 3, Plot 117, Muzzafar Manor, Waterfield Road, Linking Road, Bandra West, Mumbai has been rated 4.6","Firangi Bake in Nalasopara, Mumbai has been rated 4.6","Theobroma in Shop 8, Ground Floor, City Park Building, Central Avenue, Hiranandani Business Park, Phase 2 Dmart, Powai, Mumbai has been rated 4.5","Theobroma in 24, Cusrow Baug, Shahid Bhagat Singh Road, Colaba Causeway, Colaba, Mumbai has been rated 4.5","Food And Taste Theory in Shop 25, 2nd Floor, Phoenix Market City, LBS Marg, Kurla, Mumbai has been rated 4.5"]}
    - utter_ask_mail_send
* affirm
    - utter_ask_mailid
* mailid{"emailid":"abc@yahoo.com"}
    - slot{"emailid": "abc@yahoo.com"}
    - action_send_mail
    - slot{"emailid": "abc@yahoo.com"}
* affirm
    - utter_goodbye
