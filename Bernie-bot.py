##
# This is a module comment.
##
print('Welcome to the Bernie chatbot.')

##
# This comment provides documentation for the following
# variable.
def bernie_bot():
    policy_question="y"
      
    while policy_question=="y":
        bernie_policies()
        while True:
            policy_question=input('Is there another policy you want to know about? \n[a] y \n[b] n \n>')
            if policy_question in ["y", "n"]:
                break
    
    bernie_election()
            
    print("Thanks for using the Bernie chatbot!")
    
def bernie_policies():    
    userinput=input('What policy do you want to know about? \n>')
    if userinput.lower()== "climate":
        print("Climate change is real! I plan to transform our energy system to 100 percent renewable energy and create 20 million jobs needed to solve the climate crisis.")
    elif userinput.lower()=="taxes":
        print("This is my stance on taxes: Eat the rich. Establish an annual tax on the extreme wealth of the top 0.1 percent of U.S. households.")
    elif userinput.lower()=="healthcare":
        print("I am very passionate about my healthcare policies: Create a Medicare for All, single-payer, national health insurance program to provide everyone in America with comprehensive health care coverage, free at the point of service.")
    else:
        print("Please try a different keyword, such as climate, taxes, or healthcare.")
        return bernie_policies()
    
def bernie_election():
    electioninput=input("Do you want to know about how Bernie is doing in the campaign? \n[a] y \n[b] n \n>")
    if electioninput.lower()=="y":
        print("Unfortunately, Bernie just dropped out of the race.")
    else: 
        print("Okay!")
    
bernie_bot()
#jared
#cool
#Amelia
#lorena
