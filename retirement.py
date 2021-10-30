#investment calculator for retirement

start_invest = float(input("How much do you have invested currently? "))
income = float(input("Enter net income: "))
invest_rate = float(input("What percentage of your income do you invest for retirement?: ") * .01)
int_rate = float(input("What is your expected rate of return? (Hint: average returns adjusted for inflation is around 7%): "))
year_term = int(input("In how many years would you like to retire?: "))

rate_return = 1 + (int_rate/100)

invest_num = (float(start_invest) + float(income * invest_rate) * int_rate) * int(year_term)

#reformat float into money 
format_float = "${:,.2f}".format(invest_num)

print("Congrats! You will retire with about " + format_float)