def greet(name):
    if name == "Alice":
        print("I'm sorry, Alice. I can't do that")
        return 
#return is for functions the way continue and break is for loops
#it prevents the following code from running
    print ("hey there")
    print ("welcome, " + name)

#you can also do it like thisss
#def greet(name):
#    if name == "Alice":
#        print:("I'm sorry, Alice.")
#   else:
#       print("Heya there " + name)
    
greet("monty") 
#greet is the argument
#monty is the parameter
greet("Alice") 