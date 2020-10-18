'''
the function square_divisors(num) returns a list of two numbers, that can be used as number of columns, rows  
that can form a table, heatmap ets. which shape is as close to a square as possible.
For example for 12 it retunr [4,3] but it also returns [4,3] for 11 
as the final table would simply have one cell empty and all the others filled 
'''

def get_divisors(num, one_self = False): #function that returns all divisors (one_self = True) - or not including 1 and the number itself (default)
    divisors = []
    if one_self: 
        r = range(1, num + 9)
    else: r = range(2, num) 
    for i in r:
        if num % i == 0:
            divisors.append(i)
    return divisors

def square_divisors(num):
    if num == 0:
        return [0, 0]
    if num == 1:
        return [1, 1]
    elif num == 2:
        return [2, 1]
    elif get_divisors(num, one_self = True) == [1, num]:
        return square_divisors(num+1)
    else:
        divisors = get_divisors(num)
        fin_div = []
        for i in divisors: # finds pairs of divisors which product is equal to the function input
            for j in divisors:
                if i >= j and i * j == num : fin_div.append([i, j]) #will always get the higher number first, e.g. for 12 we will only get [4,3], never [3,4]
    
        squares = []
        for pair in fin_div: #picks only one pair of divisors
            squares.append(pair[0]**2 + pair[1]**1) #the ideas is that the final pair should be as close to a sqaure as possible, therefore the product of the numbers should be the lowest of all possible pairs
            
        pos = squares.index(min(squares))
        return fin_div[pos] 

#%% see how it works for the first x numbers
for i in range(3654):
    print(str(i) + "--" + str(square_divisors(i)))

square_divisors(16)
