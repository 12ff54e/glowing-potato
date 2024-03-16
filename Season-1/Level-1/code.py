'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

def add(xh, xl, yh, yl):
    rh = xh + yh
    if abs(xh) > abs(yh):
        rl = xh - rh + yh + xl + yl
    else:
        rl = yh - rh + xh + xl + yl

    zh = rh + rl
    zl = rh - zh + rl

    return zh, zl

def sub(xh, xl, yh, yl):
    rh = xh - yh
    if abs(xh) > abs(yh):
        rl = xh - rh - yh + xl - yl
    else:
        rl = -yh - rh + xh + xl - yl

    zh = rh + rl
    zl = rh - zh + rl

    return zh, zl

def validorder(order: Order):
    net_high = 1e20
    net_low = 0
    total_amount = 0

    for item in order.items:
        if item.type == 'payment':
            # r = net_low + item.amount
            # rr = net_high
            # net_high = rr + r
            # net_low = rr - net_high + r
            net_high, net_low = add(net_high, net_low, item.amount, 0)
        elif item.type == 'product':
            # r = net_low - item.amount * item.quantity
            # rr = net_high
            # net_high = rr + r
            # net_low = rr - net_high + r
            net_high, net_low = sub(net_high, net_low, item.amount * item.quantity, 0)
            total_amount += item.amount * item.quantity
        else:
            return "Invalid item type: %s" % item.type


    if total_amount >= 12*99999:
        return 'Total amount payable for an order exceeded'

    net = net_high - 1e20 + net_low
    if abs(net) >= 0.01:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net)
    else:
        return "Order ID: %s - Full payment received!" % order.id