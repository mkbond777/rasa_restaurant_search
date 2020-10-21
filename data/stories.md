## complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget_type": "high"}
    - slot{"budget_type": "high"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_mail_send
* affirm
    - utter_ask_mailid
* mailid{"emailid":"abc@yahoo.com"}
    - slot{"emailid": "abc@yahoo.com"}
    - action_send_mail
    - slot{"emailid": "abc@yahoo.com"}
    - utter_mail_sent
* affirm
    - utter_goodbye

## location specified
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget_type": "medium"}
    - slot{"budget_type": "medium"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_mail_send
* affirm
    - utter_ask_mailid
* mailid{"emailid":"abc@yahoo.com"}
    - slot{"emailid": "abc@yahoo.com"}
    - action_send_mail
    - slot{"emailid": "abc@yahoo.com"}
    - utter_mail_sent
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
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search{"budget_type": "low"}
    - slot{"budget_type": "low"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_mail_send
* negate
    - utter_goodbye
    - export

## complete path 3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Patna"}
    - slot{"location": "Patna"}
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
    - utter_mail_sent
* goodbye
    - utter_goodbye

## complete path 4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget_type": "high"}
    - slot{"budget_type": "high"}
    - action_search_restaurants
    - slot{"location": "bangalore"}

    
    
## happy_path
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai","budget_type": "high"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - slot{"budget_type": "high"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_ask_mail_send
* affirm
    - utter_ask_mailid
* mailid{"emailid":"abc@yahoo.com"}
    - slot{"emailid": "abc@yahoo.com"}
    - action_send_mail
    - slot{"emailid": "abc@yahoo.com"}
    - utter_mail_sent
* affirm
    - utter_goodbye


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_search_restaurants
    - slot{"location": "delhi"}
* affirm
    - utter_goodbye
