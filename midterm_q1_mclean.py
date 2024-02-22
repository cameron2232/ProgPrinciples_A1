#calculate total cost for a number of movie tickets
#5% discount if tickets is 10 or more
#round result to 2 decimal places

tickets_cost = int(input('Price for one ticket: '))

tickets_count = int(input('Number of tickets: '))

tickets_total = tickets_cost * tickets_count

if tickets_count < 10:
    print('Less than 10 tickets, no discount')
elif tickets_count >= 10:
    tickets_total *= 0.95