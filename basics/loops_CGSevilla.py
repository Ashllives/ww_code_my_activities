"""
During closing, Aling Nena counts from her vault the day's total income and
also the total amount of all her paper bills.
Help Aling Nena count her total income and total amount of her paper bills
from a list of cash money and using a loop!
"""


def is_coins(money):
    """ Determine if the money is a coin
    :param money: (Integer)
    :return: (Boolean)
    Examples:
        >>>  print(is_coins(20))
        False
        >>>  print(is_coins(1))
        True
    """
    if money > 10:
        return True
    return False


cash_on_vault = [1, 5, 100, 10, 50, 50, 20, 5, 1, 1000, 1000, 500, 5, 200]

# solution

# to count Aling Nena's total income for the day:

total_income = sum(cash_on_vault)
print ('Total income for the day is ' + str(total_income) + '.')

# to count the total amount of her paper bills:

paper_bills = []
for cash in cash_on_vault:
    # print (cash)
    if is_coins(cash) == True:
        # print (cash)
        paper_bills.append(cash)
        # print(paper_bills)

total_paper_bills = sum(paper_bills)
print ('The total amount of all bills earned for the day is ' + str(total_paper_bills) + '.')
