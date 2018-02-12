#==========================================================================
# PROGRAM:... ....... Assignment 02 - Classes and Objects
# AUTHOR:............ Phan, Anna
# COURSE:............ CSC 231 001
# TERM:.............. Spring 2018
# COLLABORATION:.....
#==========================================================================

from BankAccount import*
import statistics

input_file = open("accounts-with-types.csv", "r")
lines = input_file.read().splitlines()[1:]

balances =[]
sav_accounts = []
chk_accounts = []
accounts = []

for line in lines:
    part = line.split(",")
    acct_type = part[0]
    acct_num = part[1]
    first_name = part[2]
    last_name = part[3]
    balance = part[4]
    if acct_type == "Savings":
        s_acct = SavingsAccount(acct_num, first_name, last_name, balance)
        sav_accounts.append(s_acct)
    else:
        c_acct = CheckingAccount(acct_num, first_name, last_name, balance)
        chk_accounts.append(c_acct)
    acct = BankAccount(acct_num, first_name, last_name, balance)
    accounts.append(acct)
    balances.append(balance)

tmp = []
for i in accounts:
    if i in tmp:
        print('Warning! Account number already exists:', i.acct_num)
    else:
        tmp.append(i)

print('Number of checking accounts:', len(chk_accounts))
print('Number of savings accounts:', len(sav_accounts))

sum = 0
for b in tmp:
    sum += b.balance
print('Average balance:', sum/len(tmp))

maxBalance = tmp[0]
for b in tmp:
    if b.balance > maxBalance.balance:
        maxBalance = b
print('Biggest balance:', maxBalance)

no_dup_balances = []
for b in tmp:
    no_dup_balances.append(b.balance)

print('Median balance:', statistics.median(map(float, no_dup_balances)))

no_dup_savings = []
for i in sav_accounts:
    if i in no_dup_savings:
        pass
    else:
        no_dup_savings.append(i)

no_dup_checkings = []
for i in chk_accounts:
    if i in no_dup_checkings:
        pass
    else:
        no_dup_checkings.append(i)

for b in no_dup_savings:
    b.balance += b.calculate_interest()

for b in no_dup_checkings:
    b.balance += b.calculate_interest()

sum = 0
for b in no_dup_savings:
    sum += b.balance

for b in no_dup_checkings:
    sum += b.balance

print('Average balance with interest:', sum/len(tmp))