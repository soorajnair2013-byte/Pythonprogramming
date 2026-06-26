# smot- data should be fairly balanced (sample)

# p-probabilty value  succes+fail=1

# z=(x-u)/(std variation/sqrt(n)

# when std deviation is unknow go with t test


from scipy.optimize import root
from scipy.stats import ttest_1samp
import numpy as np
test_report=np.array([500,500,501,502,500,503,510,522,530,540,501,500,500,501,502,503,504])

mean=np.mean(test_report)

t_statistic,p_value=ttest_1samp(test_report,500)
print(f'The p value of test report :{p_value}')



if p_value<0.05:
    print('Reject the null hypothesis')
else:
    print('Accept the null hypothesis')




import numpy as np
suraj=[500,501,500,500,500,501,502,506,501,500,500,500,501,500,500]
suresh=[500,501,500,500,500,501,500,500,501,500,500,500,500,500,500]

suraj_sampletest=np.array(suraj)
suresh_sampletest=np.array(suresh)

from scipy.stats import ttest_ind
t_statistic,p_value=ttest_ind(suraj_sampletest,suresh_sampletest)
print(f'The p value of test report :{p_value}')

if p_value<0.05:
    print('Reject the null hypothesis')
else:
    print('Accept the null hypothesis')


