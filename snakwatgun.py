import random

'''
press 1 for snake 
preass 2 for water
press 3 for gun'''
d={1:'sanke',2:'water',3:'gun'}
you,com=0,0
print(''' enter 1 for snake 
    enter 2 for water
    enter 3 for gun
      ''')
while(True):
    computer=random.randint(1,3)
    yourguess=int(input("Your choice :"))
    if(yourguess<1 or yourguess>3):
        print("invalid choice!! try again ")
    else:
        print(f" your choice is {d[yourguess]} and computer choice is {d[computer]} and",end="\n     ")
        if(computer==yourguess):
            print("draw!!!")
        else:
            if yourguess==1:
                if computer==2:
                    print(" you won !! snake drinks water ")
                    you=you+1
                else:
                    print("You lost snake killed by gun ")
                    com=com+1
            else:
                if yourguess==2:
                    if computer==1:
                        com=com+1
                        print(' you lost snake drinks water ')
                    else:
                        you=you+1
                        print("you won  water damages gun")
                else:
                    if computer==1:
                        print('you win gun kills sanke')
                        you=you+1
                    else:
                        print('you lost water damges gun')
                        you=you+1
        if com==3 or you==3:
            if com==3:
                print(f' \n\nsorry computer wins\n')
            else:
                print(f' \n\n finally you win \n your point is {you}\n')
            break

            
        


        
