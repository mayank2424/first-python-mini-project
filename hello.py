# print "Hello"
#
# Spy_length =raw_input("The length of your name")
#
# string_length = len(Spy_length)
# print string_length
# def sub(number1,number2):
#     print number1-number2
# sub(5,7)
# def pow(number1, number2):
#     return number1 ** number2
# a= pow(2,10)
# print a
#
# def Spy_chat():
#     choice = True
#
#     while choice:
#
#          user_input= raw_input("Do you want to update status? Y/N")
#
#          if user_input =="Y":
#             print "your status have been updated"
#          elif user_input == "N":
#             print "Application closed"
#
#             choice = False
#          else:
#             print "Bad request"
#
# Spy_chat()
#
#
# def add(number1,number2,number3):
#    print number1+number2*number3
# add(2,2,4)
#
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

from datetime import datetime
p=datetime.now()

print p.strftime("%d/%m/%y")
