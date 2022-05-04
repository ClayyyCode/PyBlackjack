import random

random.seed()

Cards = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
Cards_convert = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10}

def cal_sum(hand):
    sum = 0
    for i in hand:
        sum += Cards_convert[i]    
    if ('A' in hand and sum <=11):
            sum +=10
    return sum

#Dealer
class dealer: 
    def __init__(self):
        self.hand = random.choices(Cards,k= 1)
dealer = dealer()
print("Dealer's hand: ", dealer.hand)

#Player
class player:
    def __init__(self):
        self.hand = random.choices(Cards,k= 2)
player = player()
print("Your hand:", player.hand)

decision = input("Player decision(hit/ stand/ split/ double/ surrender)\n")

while (decision != "stand"):
    if decision == "hit":
        player.hand += random.choices(Cards)
    print("Your hand:", player.hand)
    if cal_sum(player.hand) > 21:
        print("BUSTED MOTHER FUCKER!!!")
        break
    decision = input("your decision(hit/ stand/ split/ double/ surrender)\n")

while (cal_sum(dealer.hand) < 17 ):
    dealer.hand += random.choices(Cards)
    print("Dealer's hand: ", dealer.hand)
    if cal_sum(dealer.hand) > 21:
        print("BUSTED MOTHER FUCKER!!!")
        break

print("Dealer's hand: ", dealer.hand,"\nSum:", cal_sum(dealer.hand))
print("Your hand:", player.hand ,"\nSum:", cal_sum(player.hand))

if cal_sum(player.hand) > 21:
    print("Dealer won")
elif cal_sum(dealer.hand) > 21:    
    print("Player won")
elif cal_sum(player.hand)<cal_sum(dealer.hand):
    print("Dealer won")
elif cal_sum(player.hand)>cal_sum(dealer.hand):
    print("Player won")
else: 
    print("Draw")    