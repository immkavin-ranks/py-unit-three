def main():
    total = 0.0
    try:
        infile = open('sales_data.txt', 'r')
        for line in infile:
            amount = float(line)
            total += amount
        infile.close()
        print(format(total, ',.2f'))
    except:
        print('An error occurred.')

main()