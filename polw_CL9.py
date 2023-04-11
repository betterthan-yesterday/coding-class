#!/usr/bin/env python
# coding: utf-8

# # Computing Cumulative Assessment Practice Version
# Please refer to the handout for coding instructions.
# 
# ***

# ## Part A 
# ### Student Code - Implementation Section

# In[8]:


def factorial(num:int) -> int:
    if num-1 < 1:
        return 1
    return num * factorial(num-1)

def calc_money(coins:list[int], targets:list[float]) -> list[list]:
    total = (coins[0]*200 + coins[1]*100 + coins[2]*25 + coins[3]*10 + coins[4]*5)/100
    target_difference = []
    target_status = []
    
    for x in targets:
        target_difference.append(round(total-x,2))
        if total-x > 0: target_status.append("above")
        elif total-x < 0: target_status.append("below")
        else: target_status.append("equal")
    
    return [total, target_difference, target_status]


# ### Testing Cell
# Run this cell to test your functions

# In[9]:


num = 4
result = factorial(4)

print("The factorial of", num, "is", result)
print("")

coins = [1,2,3,6,7]
targets = [5.25,5.7,2.25,6.60]

money = calc_money(coins,targets)

print("You have a total of", money[0], "dollars")

for i in range(len(money[1])):
    print("The difference between the target", targets[i], "is", money[1][i])
    print("Your amount of",money[0], "is", money[2][i], "the target")




# ## Part B ##
# 
# 
# ### Deck Class ###
# ##### Do Not Edit Below Cell! #####
# ***

# In[12]:


#Do not edit this cell! 
#Make sure to run the cell!

import itertools as itt
import random

class Deck:

    def __init__(self):

        self.card_list = []
        for i in range(0,4):
            for j in range (1, 14):
                card = j
                self.card_list.append(card)
                
        self.points = 0

    def pick_card(self):

        card_return = self.card_list[0]
        self.card_list.remove(card_return)

        return card_return

    def return_card(self, returned_card):

        self.card_list.append(returned_card)

    def shuffle_deck(self):

        temp_list = []
        while len(self.card_list) != 0:
            card_index = random.randint(0, len(self.card_list)-1)
            temp_list.append(self.card_list[card_index])
            self.card_list.pop(card_index)

        self.card_list = temp_list
        
    # Takes in a hand of cards, and number:
    # Returns: list of combinations (tuples) of #num, for the hand given
    def hand_combinations(self,hand,num):
        combos = list(itt.combinations(hand, num))
        return combos
        
        
    # Examples: hand_combinations([1,2,3,4],2) --> [(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)]
    # hand_combinations([1,2,3,4],3) --> [(1,2,3),(1,2,4),(1,3,4),(2,3,4)]

    def adjust_points(self,points):
        self.points = points

    


# ### Student Code - Implimentation Section ###

# In[81]:


# Student Code
def check_fifteens(deck, current_hand:list[int]):
    fifteen_points = 0
    twos = deck.hand_combinations(current_hand, 2)
    threes = deck.hand_combinations(current_hand, 3)
    fours = deck.hand_combinations(current_hand, 4)
    for x in twos:
        if sum(x) == 15:
            fifteen_points += 2
    for x in threes:
        if sum(x) == 15:
            fifteen_points += 2
    for x in fours:
        if sum(x) == 15:
            fifteen_points += 2
    if sum(current_hand) == 15: fifteen_points += 2
    
    return fifteen_points

def check_runs(current_hand):
    hand = []
    run_points = 0
    for n in current_hand:
        hand.append(n)
    
    hand.sort()
    for x in range(0,4):
        print(hand)
        if current_hand[0]+1 != current_hand[1] :
            hand.pop(0)
    
    if len(hand)>1:
        if hand[-1] != hand[-2]+1:
            hand.pop()
    
    if len(hand) > 2:
        run_points += len(hand)
    return run_points
            
def evaluate_hand(deck, current_hand):
    total = check_fifteens(deck, current_hand) + check_runs(current_hand)
    return total


# ### Testing Cell
# Run this cell to test your functions

# In[87]:


# Testing Cell #
def main():
    card_deck = Deck()
    player_hand = []
    card_deck.shuffle_deck()
    
    for counter in range(0,5):
        card = card_deck.pick_card()
        player_hand.append(card)
        
        
    print("Your hand is: ", player_hand)
    print("Counting cards!")
    print("Run points are:", check_runs(player_hand))
    print("Fifteen points are:", check_fifteens(card_deck,player_hand))
    print("Total points are: ", evaluate_hand(card_deck,player_hand))
    for item in player_hand:
        card_deck.return_card(item)
    print("Game over!")
main()


# In[ ]:





# In[ ]:





# In[ ]:




