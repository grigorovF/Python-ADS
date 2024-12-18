"""
At the bus stop in FinTown, there were N adults and M children who wanted to travel together to the neighboring city of MinTown. 
The price of one ticket is 100 euros. If an adult wants to travel with k children, he needs to pay one ticket for him
and k-1 tickets for the children (he does not have to pay a ticket for one child). Also, an adult can ride alone,
in which case he will pay one ticket for himself. Additionally, we know that children cannot ride without being 
accompanied by an adult. The first row of the entry is given the number N. 
The second row is given the number M. You need to calculate the minimum and maximum number of euros that passengers can pay
for tickets and print them in two lines.
There will be at least one adult on the bus.
"""

import math
import os
import random
import re
import sys

def bus(M,N):
   if (M == 0):
       return "Musst have an adult!"
   maxcost = 100*(N+M)
   mincost = 100*N + 100*(max(0, M-N))

   return (mincost, maxcost)


M = int(input("Enter a number of adults: "))
N = int(input("Enter a number of children: "))
result = bus(M, N)

print(result)