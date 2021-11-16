import random

#hadse addade 2

karan_bala = 100
karan_paiin = 1
number = random.randint(karan_paiin,karan_bala)
print(number)
no_find = True
tedade_hads = 0


while no_find:
    client_number = (input("please say your number is biger(b) or is smaller(s) or equal(e)>>[b,s,e] :"))
    tedade_hads = tedade_hads + 1
    if client_number == "b":
        karan_paiin = number
        number = random.randint(karan_paiin,karan_bala)
        print(number)

    elif client_number == "s":
        karan_bala = number
        number = random.randint(karan_paiin,karan_bala)
        print(number)

    else :
        print("you won computer")
        no_find = False


print("successfully!!!","you do this game computer in ",tedade_hads-1," steps")



























