
def cls():
    
    print('\n'*30)

	

print("WELCOME TO THE GAME OF STONE, PAPER AND SCISSORS")
print(" ")        #For Spaceing
print(" ")
print(" ")



def loop():
        print(" ")
        print(" ")
        print("Ok, Now the FUN part, Naming :P")
        print(" ")
        print(" ")
        print(" ")

       
        Player1=input("Enter the First player's name \n")
        print(" ")
        print(" ")
        print(" ")
       
       
        Player2=input("Enter the Seccond player's name \n")
        print(" ")
        print(" ")
        print(" ")

        print("WELCOME",Player1,"and",Player2)
        print(" ")
        print(" ")
        print(" ")


        print("LET'S START")
        print(" ")
        print(" ")
        print(" ")
        
       
        x = input("{} please choose b/w 'Stone','Paper',Scissors'\n".format(Player1))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
        cls()
        y = input("{} please choose b/w 'Stone','Paper',Scissors'\n".format(Player2))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
        cls()
        print(" ")
        print(Player1," Chooses ",x)
        print(" ")
        print(Player2," Chooses ",y)
        print(" ")
        if x==y:
            print("Draw")
        elif x== "Stone" :
            if y=="Paper":
                print(Player2,"Wins")
            else:
                print(Player1,"Wins")
        elif x== "Paper":
            if y=="Stone":
                print(Player1,"Wins")
            else:
                print(Player2,"Wins")
        elif x== "Scissors":
            if y== "Stone":
                print(Player2,"Wins")
            else:
                print(Player1,"Wins")


    


while True:
    ans=input("Do you Want to play ? \n Y = 'YES' N = 'NO' \n ")
    if ans=="Y":
        loop()
        
    else:
        print("THANK YOU FOR PLAYING")
        break
