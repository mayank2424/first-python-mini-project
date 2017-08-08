from Spydetails import Spy_name , Spy_age, Spy_salutation , Spy_online , Spy_rating

from  steganography.steganography import Steganography
# print Spy_name
# print Spy_age
friend_name=[]
friend_age=[]
friend_rating=[]
friend_is_online=[]


STATUS_MESSAGE=["Test1", "Test2" ,"TEST3", "test4", "test5"] # yaha humne STATUA_MESSAGE naam ki list bana di
def add_status(Current_status_message):  # here we have made function and remember always to call function
    choice= raw_input("Would you like to add new message (y/n) ??")

    if choice == "y":  # here ew have used if statement based on user choice
        new_message= raw_input("whats on your mind??")

        if len(new_message)>0:  #len is for calaculating length of string
                STATUS_MESSAGE.append(new_message)
                print STATUS_MESSAGE

    else:
         for status in STATUS_MESSAGE:  # here we have usef for loop in different way ki matlab (ki ye each value ko lega STATUA_MESSAGE wali list me se
               print status
         index = int(raw_input("which status you like to add "))

         print STATUS_MESSAGE[index-1]  # index-1 used beacuase user will not choose message in form of array

add_status("test")  #"HERE WE HAVE CALLED FUNCTION"

def addfriend():
    new_name= raw_input("Please add your friends name")
    new_salutation= raw_input("Shouls i call Mr. or Ms. ??")
    new_age = int(raw_input("whats the age"))
    new_rating = float(raw_input("whats the rating"))

    if len(new_name)> 0 and new_age> 14 and new_rating>=Spy_rating:
             friend_name.append(new_name)  # append function kuch add karne ke liye hota hain (jaise ki koi message enter karna hain humne list mein koi detail update hone kebaad
             friend_age.append(new_age)
             friend_rating.append(new_rating)
             print "friend added"
    else:
        print "sorry invalid details try another details"

    print  "your friends details added  " , "Name =",friend_name , "Age=" ,friend_age , "rating= " ,friend_rating
addfriend()

from  steganography.steganography import Steganography   #yaha humne steganography wali library install kari hain from pip command. Steganography is basically for encoding and decoding message
def send_message():   # def function ke liye use hota hain first we had made send_message function and then defines the variable and steganography class in it
    original_image= 'input.jpg'
    output_path="output.jpg"
    text= raw_input("what you want to enter in this image ")
    Steganography.encode(original_image, output_path, text)  # here we have used steganography class to encode  the message
def read_message():   # this function we made for decoding basically for reading message
    output_path= 'output.jpg'
    secret_text= Steganography.decode(output_path)
    return secret_text

# send_message() ye function pehle call kiya encode karne ke liye
#
send_message()


