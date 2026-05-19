#concept of pass continue and break

for i in range(1,5):
  print(i, end=" ")


for i in range(2,5):
  print(i, end=" ")
  break


for i in range(1,5):
  print(i, end=" ")
  continue

for i in range(1,5):
  continue
  print(i, end=" ")

  
  
for i in range(1,5):
  pass
#   pass # it ensures there is no input error



for i in range(1,5):
  if i%2==0:
    print(i)
    pass
    
  continue


i=0
while i<=5:
  for i in range(1,5):
    pass
    print(i)
    i=i+1
  break


i=0
while i<=5:
  for i in range(1,5):
    print(i)
    i=i+1
  continue


# logic:

# 1. ask user to enter name,passcode,acct_no,withdraw_amt,acct_type
# 2. defined variables: saving_acct = 10000 and current_acct = 2000
# 3. condition: type == 1 for saving_acct and type == 2 for current_acct
# 4. if withdraw_amt <= saving_acct : balance  = saving_acct - withdraw_amt
# 5. if withdraw_amt <= current_acct : balance  = current_acct - withdraw_amt
# 6. print(balance)


#Define User Variables

name = input("Enter the Name :")
passcode = int(input("Enter the Passcode : "))
withdraw_amt = int(input("Enter the Withdraw Amount : "))
acct_no = int(input("Enter the Account Number : "))
acct_type = int(input("Enter the Account Type : "))

#Define Variables

saving_acct = 10000
current_acct = 2000

# Condition: ask user to enter the type of account
# '''
# 1: Saving Account
# 2: Current Account
# '''


account = input("Enter the type of account (1 and 2): ")

if account == "1":
  if withdraw_amt <= saving_acct:
    balance = saving_acct - withdraw_amt
    print(balance)
  else:
    print("Insufficient Balance")

if account == "2":
  if withdraw_amt <= current_acct:
    balance = current_acct - withdraw_amt
    print(balance)
  else:
    print("Insufficient Balance")