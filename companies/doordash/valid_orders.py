
"""
Given a set list of pickups and deliveries for order, figure out if the given list is valid or not.

A delivery cannot happen for an order before pickup.
The same order cannot be delivered or picked up twice
The car must be empty at the end of the drive.
Examples below:
[P1, P2, D1, D2]==>valid
[P1, D1, P2, D2]==>valid
[P1, D2, D1, P2]==>invalid
[P1, D2]==>invalid
[P1, P2]==>invalid
[P1, D1, D1]==>invalid
[]==>valid
[P1, P1, D1]==>invalid
[P1, P1, D1, D1]==>invalid
[P1, D1, P1]==>invalid
[P1, D1, P1, D1]==>invalid
"""

def is_valid_order(orders):
    p_set = set()
    d_set = set()

    for o in orders:
        o_type = o[0]
        o_id   = o[1]

        if o_type == 'P':
            if o_id in p_set:
                return False
            else:
                p_set.add(o_id)
        elif o_type == 'D':
            if o_id in d_set or o_id not in p_set:
                return False
            else:
                d_set.add(o_id)
                
    return len(p_set) == len(d_set)

orders = ['P1', 'P2', 'D1', 'D2']

print(is_valid_order(orders))

"""
Follow up: Find longest valid subarray

Ex 1: orders = ['P1', 'P1', 'D1'], return ['P1', 'D1']
Ex 2: orders = ['P1', 'P1', 'D1', 'D1'], return ['P1', 'D1']
"""

def longest_valid_orders(orders):
    p_set = set()
    d_set = set()
    result = []

    for o in orders:
        o_type = o[0]
        o_id   = o[1]

        if o_type == 'P':
            if o_id in p_set:
                continue
            else:
                p_set.add(o_id)
                result.append(o)
        elif o_type == 'D':
            if o_id in d_set or o_id not in p_set:
                continue
            else:
                d_set.add(o_id)
                result.append(o)
                
    return result

orders = ['P1', 'P1', 'D1', 'D1']
print(longest_valid_orders(orders)) # ['P1', 'D1']

