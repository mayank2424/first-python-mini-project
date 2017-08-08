print "Hello" #here we have simply used print function to print this string

Spy =raw_input("what is your name ?") #here we have made a variable in Spy whre we haved stored raw_nput value("raw_input ka yaha matlab hhain agar hum input me kuch bhi de numbers or character ts it will always written output in string
# Spy_rating=0.0
# Spy_is_online = False

string_length = len(Spy) #here also we have made another variable and "len" is for calculating length of string
# print string_length

if string_length > 0: #here if statement has been implemented and"remember not ot use brackets because  python dont understanfd brackets in if statemm
     print "hello" + Spy

else: print "please enter your name"

Spy_age = int(raw_input("what is your age?"))

if Spy_age >=18 and Spy_age <50:
    print "welcome"
else:
    print "you are not eligible"

Spy_rating = 3.5

if Spy_rating >4.5:
    print "yeh its awesome"
elif Spy_rating >=3.5 and Spy_rating <=4.5:
      print "its good spy"
elif Spy_rating >=2.5 and Spy_rating <=3.5:
    print  "Average"
elif Spy_rating <2.5:
    print "so bad"

Spy_online = raw_input("is spy online ?")

print Spy_online , " ,now you can do chat"

# print "Welcome" + Spy + "\nYour age is  " + str(Spy_age) + "\nYour Rating is" + str(Spy_rating)


