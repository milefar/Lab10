def prices(lines, option):
    c_count = 0
    s_count = 0
    q_count = 0

    c_sum = 0
    s_sum = 0
    q_sum = 0

    c_max = 0
    q_max = 0
    s_max = 0

    c_min = 100000
    s_min = 100000
    q_min = 100000
    for line in lines:
        data = line.strip().split(',')
        if float(data[-3]) == 0:
            continue
        else:
            price = float(data[-3])
        if data[-1] == 'C':
            c_count += 1
            c_sum += price
            if price < c_min:
                c_min = price
            if price > c_max:
                c_max = price
        elif data[-1] == "S":
            s_count += 1
            s_sum += price
            if price < s_min:
                s_min = price
            if price > s_max:
                s_max = price
        elif data[-1] == "Q":
            q_count += 1
            q_sum += price
            if price < q_min:
                q_min = price
            if price > q_max:
                q_max = price
    if option == 0:
        return [c_min, s_min, q_min]
    elif option == 1:
        return [c_max, s_max, q_max]
    else:
        return [round(c_sum/c_count,2) if c_sum != 0 else 0, round(s_sum/s_count,2) if s_sum != 0 else 0, \
                round(q_sum/q_count,2) if q_sum != 0 else 0]