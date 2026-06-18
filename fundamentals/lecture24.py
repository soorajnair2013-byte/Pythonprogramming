'''
random forest algorithm
100 trees 

binoamial distribution
binomial distribution is the probbaility distribution for the number of success in a sequence of bernoulli trails

eg. person tossing a coin
the event to occur head p=0.5 i.e success
                        q=0.5 ie failure
                        note: p+q=1

'''

from scipy.stats import binom

n,p=10,0.5 
mean,var,skew,kurt=binom.stats(n, p ,moments='mvsk')
print(mean,var,kurt,skew)


#binom.pmf(r,n,p)
'''
r: a list of integers from 0 to n,inclusive
n:the total nummber of trails or times the experiment will beb carried out
p:the propbability that the outcome of a single experiment will be a success
the value of p must be between 0 and 1, inclusive
'''




binom.pmf(1,2,0.5)



'''
note
if p<0.5
distribution is right skewed

if p=0.5
distribution is symmetric

if p>0.5
distribution is left skewed


'''