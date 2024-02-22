#calculate total cost for a number of movie tickets
#5% discount if tickets is 10 or more
#round result to 2 decimal places

tickets_cost = float(input('Price for one ticket: '))

tickets_count = float(input('Number of tickets: '))

tickets_total = tickets_cost * tickets_count

if tickets_count < 10:
    print('Less than 10 tickets, no discount')
elif tickets_count >= 10:
    print('10 or more tickets, 5% discount')
    tickets_total *= 0.95
    
print(f'Total cost: {tickets_total: .2f}')