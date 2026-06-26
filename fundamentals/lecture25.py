from scipy.optimize import root
'''
a client claim that the consignment i ds faulty as the standard ph value of the product is not equal to 7. so prepre inderential stats report  to support
the claim
'''
from scipy.stats import ttest_1samp
import numpy as np
test_report=np.array([7,7.1,7.2,7,7,7,7,7,8,8,9,10,7.2,9,7.2,7,7,7,7])

mean=np.mean(test_report)

t_statistic,p_value=ttest_1samp(test_report,7)
print(f'The p value of test report :{p_value}')



if p_value<0.05:
    print('Reject the null hypothesis')
else:
    print('Accept the null hypothesis')

#calculating standard deviation

std=np.std(test_report)
sqrt_samplesize=std/np.sqrt(len(test_report))

SE=std/sqrt_samplesize
print(f'the standard error of the mean is {SE}')

upper_bound=7+SE
lower_bound=7-SE
print(upper_bound,lower_bound)












