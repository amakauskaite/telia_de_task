"""
The function computeCheckoutTime takes a list of times/customers and the number of checkout counters and return the total time required to check out all the customers.

Sample input:[2,3,10], 2
Sample output: 12
"""

from typing import List

def computeCheckoutTime(customers: List[int], n: int) -> int:
    if n == 1:
        return sum(customers)
    elif n >= len(customers):
        return max(customers)
    else:
        return counter_simulation(customers, n)


def counter_simulation(customers: List[int], n: int) -> int:
    counters = [0] * n
    max_customer_index = len(customers) - 1
    total_time_spent = 0
    index = 0

    for counter in counters:
        counters[index] = customers[index]
        index += 1

    while index < len(customers):
        minimum_time = min(counters)
        total_time_spent += minimum_time
        counters = [counter - minimum_time for counter in counters]

        for i, counter in enumerate(counters):
            if counter == 0 and index < max_customer_index:
                counters[i] = customers[index]
                index += 1
            elif counter == 0 and index == max_customer_index:
                counters[i] = customers[index]
                if index == max_customer_index:
                    total_time_spent += max(counters)
                    index = max_customer_index + 1
                break

    return total_time_spent
