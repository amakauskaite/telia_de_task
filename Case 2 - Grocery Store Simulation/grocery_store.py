def computeCheckoutTime(customers, n):
    counters = [0] * n
    total_time_spent = 0

    if n == 1:
        return sum(customers)
    elif n == len(customers):
        return max(customers)
    else:
        return total_time_spent

#computeCheckoutTime([1, 2], 2)