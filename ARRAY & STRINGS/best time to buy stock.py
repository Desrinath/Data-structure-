""" find Max profit you can achieve 
    you may sell once and buy once 
    if you cant make profit return 0
     
    Ex = 
        price=[7,1,5,3,6,4]
         output=5
          
    How ? 
     buy on day 1 (price=1) and 
    sell on 4th day (price=6) 6-1=5
     
      
    Brute Force!!!

def maxi(prices):
    maximum = 0
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            profit = prices[j] - prices[i]
            maximum = max(maximum, profit)
    return maximum

prices = [7, 1, 5, 3, 6, 4]
a = maxi(prices)
print(a)  # Output: 5

 """
#OPTIMAL 
''' 🧠 Key Intuition:
We want to buy at the lowest price so far.

At each step, compute:

Current profit = current price − min price seen so far

Max profit = max of all those profits

🧪 Walkthrough Example
python
Copy
Edit
prices = [7, 1, 5, 3, 6, 4]

Day	    Price	min_price	    profit (price - min)	max_profit
0	    7	        7               -                       0
1	    1	        1 (update)	    -	                    0
2	    5   	    1	            5 - 1 = 4	            4
3	    3	        1	            3 - 1 = 2	            4
4	    6	        1	            6 - 1 = 5	            5 (update)
5	    4	        1	            4 - 1 = 3	            5
Return 5


'''

def maxi(prices):
    min=float('inf')
    maximum=0

    for price in prices:
        if price<min:
            min=price
        else:
            profit=price-min
            maximum=max(maximum,profit)
    return maximum
prices = [7, 1, 5, 3, 6, 4]
a = maxi(prices)
print(a) 