def prices(lines, option):
    counts = {'C': 0, 'S': 0, 'Q': 0}
    sums = {'C': 0, 'S': 0, 'Q': 0}
    max_prices = {'C': 0, 'S': 0, 'Q': 0}
    min_prices = {'C': float('inf'), 'S': float('inf'), 'Q': float('inf')}

    for line in lines:
        data = line.strip().split(',')
        price = float(data[-3])
        port = data[-1]

        if price == 0:
            continue

        if port in counts:
            counts[port] += 1
            sums[port] += price
            if price > max_prices[port]:
                max_prices[port] = price
            if price < min_prices[port]:
                min_prices[port] = price

    if option == 'min':
        return [min_prices['C'], min_prices['S'], min_prices['Q']]
    elif option == 'max':
        return [max_prices['C'], max_prices['S'], max_prices['Q']]
    elif option == 'avg':
        return [
            round(sums['C'] / counts['C'], 2) if counts['C'] != 0 else 0,
            round(sums['S'] / counts['S'], 2) if counts['S'] != 0 else 0,
            round(sums['Q'] / counts['Q'], 2) if counts['Q'] != 0 else 0
        ]
