print ("**************************************")
print ("**    Welcome  to the Snakes Cafe!  **")
print ("**    Please see our menu below.    **")
print ("**")
print ('** to quiet at any time,type "quit" **')
print ("**************************************")
print ("Appetizers")
print ("----------")
print ("Wings")
print ("Cookies")
print ("Spring Rools")
print ("            ")
print ("            ")
print ("Entrees")
print ("-------")
print ("Salmon")
print ("Steak")
print ("Meat Tornado")
print ("A literal Garden")
print ("            ")
print ("            ")
print ("Desserts")
print ("--------")
print ("Ice Cream")
print ("Cake")
print ("Pie")
print ("            ")
print ("            ")
print ("Drinks")
print ("-------")
print ("Coffee")
print ("Tea")
print ("Unicorn Tears")
print ("            ")
print ("            ")
print ("**************************************")
print ("**   what would you like to order?  **")
print ("**************************************")
count_wings=0
count_cookies=0
count_springRolls=0
count_salmon=0
count_steak=0
count_meatTornado=0
count_literal=0
count_ice=0
count_cake=0
count_pie=0
count_coffee=0
count_tea=0
count_unicorn=0
menu =True

summary_order={"Wings":count_wings, "Cookies":count_cookies , "Spring Rolls":count_springRolls, "Salmon":count_salmon ,
              "Steak":count_steak,"Meat Tornado":count_meatTornado,"A literal Garden":count_literal , "Ice Cream":count_ice 
               ,"Cake":count_cake,"Pie":count_pie,"Coffee":count_coffee,"Tea":count_tea,"Unicorn Tears":count_unicorn}
def the_order(order):
        global count_wings
        global count_cookies
        global count_springRolls
        global count_salmon
        global count_steak
        global count_meatTornado
        global count_literal
        global count_ice
        global count_cake
        global count_pie
        global count_coffee
        global count_tea
        global count_unicorn
        
        
        if order=="Wings":
            count_wings+=1
            print ("**" +str(count_wings)+ " order of "+ order + " have been added to your meal **")
            summary_order['Wings']=count_wings
        elif order=="Cookies":
            count_cookies+=1
            print ("**" +str(count_cookies)+ " order of "+ order + " have been added to your meal **")
            summary_order['Cookies']=count_cookies
        elif order=="Spring Rolls":
            count_springRolls+=1
            print ("**" +str(count_springRolls)+ " order of "+ order + " have been added to your meal **")
            summary_order['Spring Rolls']=count_springRolls
        elif order=="Salmon":
            count_salmon+=1
            print ("**" +str(count_salmon)+ " order of "+ order + " have been added to your meal **")
            summary_order['Salmon']=count_salmon
        elif order=="Steak":
            count_steak+=1
            print ("**" +str(count_steak)+ " order of "+ order + " have been added to your meal **")
            summary_order['Steak']=count_steak
        elif order=="Meat Tornado":
            count_meatTornado+=1
            print ("**" +str(count_meatTornado)+ " order of "+ order + " have been added to your meal **")
            summary_order['Meat Tornado']=count_meatTornado
        elif order=="A literal Garden":
            count_literal+=1
            print ("**" +str(count_literal)+ " order of "+ order + " have been added to your meal **")
            summary_order['A literal Garden']=count_literal
        elif order=="Ice Cream":
            count_ice+=1
            print ("**" +str(count_ice)+ " order of "+ order + " have been added to your meal **")
            summary_order['Ice Cream']=count_ice
        elif order=="Cake":
            count_cake+=1
            print ("**" +str(count_cake)+ " order of "+ order + " have been added to your meal **")
            summary_order['Cake']=count_cake
        elif order=="Pie":
            count_pie+=1
            print ("**" +str(count_pie)+ " order of "+ order + " have been added to your meal **")
            summary_order['Pie']=count_pie
        elif order=="Coffee":
            count_coffee+=1
            print ("**" +str(count_coffee)+ " order of "+ order + " have been added to your meal **")
            summary_order['Coffee']=count_coffee
        elif order=="Tea":
            count_tea+=1
            print ("**" +str(count_tea)+ " order of "+ order + " have been added to your meal **")
            summary_order['Tea']=count_tea
        elif order=="Unicorn Tears":
            count_unicorn+=1
            print ("**" +str(count_unicorn)+ " order of "+ order + " have been added to your meal **")
            summary_order['Unicorn Tears']=count_unicorn
        else:
            print("your order not found in the menu, try to choice other thing")
            new_order=input("> ")
            the_order(new_order)
while (menu):
    O=input("> ")
    if O =="quit":
        menu=False
    else:
        the_order(O)
        
            
def summary(S):
    for Key in S.keys():
        if S[Key]>=1:
            print (str(S[Key]) +" " +Key )
print("Your orders:")            
summary(summary_order)

        

        
    
