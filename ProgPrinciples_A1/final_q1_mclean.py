def process_employees(employees, file_name):
    try:
        with open(file_name, 'w') as file:
            for i in range(len(employees)):
                file.write(f'{employees[i]}')
                if ((i + 1) % 3) == 0:
                    file.write('\n')
                else: file.write(',')
    except Exception:
        print('Error')
        return False    

    five = total = count = 0
    higher = []
    lower = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                fields = line.rstrip('\n').split(',')
                if int(fields[1]) > 5:
                    five += 1
                total += float(fields[2])
                count += 1
            
            total = total / count   
            #print(f'Employees of 5+ years: {five}')
            #print(f'Average salaries: {total: .2f}')
                
    except Exception:
        print('Error')
        return False
    
    try:
        with open(file_name, 'r') as file:
            for line in file:
                fields = line.rstrip('\n').split(',')
                if float(fields[2]) > total:
                    higher.append(fields[0])
                else: lower.append(fields[0])
                
            #print(f'High-Pad Employees: {higher}')
            #print(f'Low-Paid Employees: {lower}')
                
    except Exception:
        print('Error')
        return False
    
    return five, total, higher, lower
            
count, average, higher_list, lower_list = (process_employees(['George', 3, 
                                                              3456.78, 'Jack', 8, 5678.91, 'Anna', 4, 3142.65], 'employees.txt'))

print(f'Employees of 5+ years: {count}')
print(f'Average salaries: {average: .2f}')
print(f'High-Pad Employees: {higher_list}')
print(f'Low-Paid Employees: {lower_list}')