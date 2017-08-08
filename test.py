# def hello(name="mayank"):
#      print "hello %s" % (name)
# hello()
# hello( "Amayank")

STATUS_MESSAGE=["Test1", "Test2" ,"TEST3", "test4", "test5"]
def add_status(Current_status_message):
    choice= raw_input("Would you like to add new message (y/n) ??")

    if choice == "y":
        new_message= raw_input("whats on your mind??")

        if len(new_message)>0:
                STATUS_MESSAGE.append(new_message)
                print STATUS_MESSAGE

    else:
         for status in STATUS_MESSAGE:
               print status
         index = int(raw_input("wouls you like to choose to add status"))

         print STATUS_MESSAGE[index-1]



add_status("test")






