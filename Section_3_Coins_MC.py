#!/usr/bin/env python
# coding: utf-8


#Libraries
import numpy as np
import random
import copy as cp
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import time


# For the first coin, you are paid the value of the coin. For subsequent coins, you are paid the absolute 
# difference between the drawn coin and the previously drawn coin. For example, if you drew 5,3,2,4,1, your
# payments would be 5,2,1,2,3 for a total payment of 13.
def getPayment(pouch,n):
    
    pouch_l=pouch.copy()
    prev=0
    payment=0
    for i in range(n):
        coin=random.choice(pouch_l)
        payment=payment+abs(prev-coin)
        prev=coin
        pouch_l.remove(coin)
    return payment


#Estimate the expected payment based on x simulations
def paymentSim(n_sims=10000): #by default run 10000 simulations
    total=0
    #Coins in bag
    nc=int(input())
    bag=list(np.arange(1,nc+1))
    start=time.time()
    payment=np.empty((n_sims,))
    for i in range(n_sims):
        payment[i]=getPayment(bag,nc)
    
    end=time.time()
    print(end-start) #to measure the time taken
    return payment



# 10 million simulations gave the most accurate results

payment_10=paymentSim(100000000)

print(payment_10.mean(), payment_10.std())
len(payment_10[payment_10>=45])/len(payment_10)


payment_20=paymentSim(100000000)

print(payment_20.mean(), payment_20.std())
len(payment_20[payment_20>=160])/len(payment_20)

