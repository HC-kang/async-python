def cpu_bound_func(number):
    total = 1
    arrange = range(1, number+1)
    for i in arrange:
        for j in arrange:
            for k in arrange:
                total *= i * j * k
    
    return total

if __name__ == '__main__':
    result = cpu_bound_func(100)
    print(result)