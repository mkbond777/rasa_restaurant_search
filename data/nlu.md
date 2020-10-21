## intent:affirm
- yes
- yep
- yeah
- indeed
- that's right
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks
- thanks

## intent:goodbye
- bye
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye
- have a good one

## intent:greet
- hey
- howdy
- hey there
- hello
- hi
- good morning
- good evening
- dear sir
- hi
- hi
- hello

## intent:negate
- no
- not required
- no Thanks
- nope
- negative

## intent:mailid
- here you go [abc@gmail.com](emailid)
- my email address is [new@abc.co.in](emailid)
- [test@gmail.com](emailid)
- [hello@test.co.in](emailid)

## intent:restaurant_search
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- show me [chinese](cuisine) restaurants
- show me [chines](cuisine:chinese) restaurants in the [New Delhi](location:Delhi)
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- search for restaurants
- anywhere in the [west](location)
- I am looking for [asian fusion](cuisine) food
- I am looking a restaurant in [294328](location)
- in [Gurgaon](location)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [Chinese](cuisine:chinese)
- [chinese](cuisine)
- [Lithuania](location)
- Oh, sorry, in [Italy](location)
- in [delhi](location)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican indian fusion](cuisine)
<!-- - can you book a table in [rome](location) in a [moderate](price:mid) price range with [british](cuisine) food for [four](people:4) people -->
- [central](location) [indian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurantin [bangalore](location)
- [mumbai](location)
- [Chinese](cuisine:chinese)
- show me restaurants
- [Italian](cuisine)
- [<300](budget_type:low)
- [Rs. 300 to 700](budget_type:medium)
- [More than 700](budget_type:high)
- please fine me some [chnese](cuisine:chinese) restaurart in [delhi](location:Delhi) having [average price for two people as 1000](budget_type:high)
- look for some restaurants [under 500](budget_type:medium)
- look for some [cheap](budget_type:low) restaurnats 
- I am looking for some restaurnats in [Mumbai](location) with [average price not more than 700](budget_type:medium)
- I am looking for some [high budget_type](budget_type:high) [Italian](cuisine) restaurants 
- please find me [chinese](cuisine) restaurant in [delhi](location)
- can you find me a [chinese](cuisine) restaurant
- [delhi](location)
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- show me restaurants in [Dilli](location:Delhi)


## synonym:Delhi
- dilli
- New Delhi

## synonym:bangalore
- Bengaluru
- Banglore

## synonym:chinese
- chines
- Chinese
- Chines

## synonym:mid
- moderate

## lookup:location
- Agra
- Ajmer
- Aligarh
- Amravati
- Amritsar
- Asansol
- Aurangabad
- Bareilly
- Belgaum
- Bhavnagar
- Bhiwandi
- Bhopal
- Bhubaneswar
- Bikaner
- Bilaspur
- BokaroSteelCity
- Chandigarh
- Coimbatore
- Cuttack
- Dehradun
- Dhanbad
- Bhilai
- Durgapur
- Dindigul
- Erode
- Faridabad
- Firozabad
- Ghaziabad
- Gorakhpur
- Gulbarga
- Guntur
- Gwalior
- Gurgaon
- Guwahati
- Hamirpur
- Hubli–Dharwad
- Indore
- Jabalpur
- Jaipur
- Jalandhar
- Jammu
- Jamnagar
- Jamshedpur
- Jhansi
- Jodhpur
- Kakinada
- Kannur
- Kanpur
- Karnal
- Kochi
- Kolhapur
- Kollam
- Kozhikode
- Kurnool
- Ludhiana
- Lucknow
- Madurai
- Malappuram
- Mathura
- Mangalore
- Meerut
- Moradabad
- Mysore
- Nagpur
- Nanded
- Nashik
- Nellore
- Noida
- Patna
- Pondicherry
- Purulia
- Prayagraj
- Raipur
- Rajkot
- Rajahmundry
- Ranchi
- Rourkela
- Salem
- Sangli
- Shimla
- Siliguri
- Solapur
- Srinagar
- Surat
- Thanjavur
- Thiruvananthapuram
- Thrissur
- Tiruchirappalli
- Tirunelveli
- Ujjain
- Bijapur
- Vadodara
- Varanasi
- Vasai-VirarCity
- Vijayawada
- Visakhapatnam
- Vellore
- Warangal
- Ahmedabad
- Bengaluru
- Chennai
- Delhi
- Hyderabad
- Kolkata
- Mumbai
- Pune
    
## synonym:vegetarian
- veggie
- vegg

## regex:greet
- hey[^\s]*

## regex:pincode
- [0-9]{6}

## regex:mailid
- [^@]+@[^@]+\.[^@]+
