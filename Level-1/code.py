'''
////////////////////////////////////////////////////////////
///                                                      ///
///   0. tests.py is passing but the code is vulnerable  /// 
///   1. Review the code. Can you spot the bug?          ///
///   2. Fix the code but ensure that tests.py passes    ///
///   3. Run hack.py and if passing then CONGRATS!       ///
///   4. If stuck then read the hint                     ///
///   5. Compare your solution with solution.py          ///
///                                                      ///
////////////////////////////////////////////////////////////
'''

from collections import namedtuple
from decimal import Decimal

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

MAX_QUANTITY = 1_000 # Why would you buy more than a thousand of anything?
MAX_ITEM_VALUE = 1_000_000 # Why would you spend more than a million on an item?
MAX_TOTAL = 1_000_000_000 # Why would you spend more than a billion?

def validorder(order: Order):
    # This is an alternative to use 'common arithmetic' without the fuss of floating point conversion imprecisions
    net = Decimal('0')
    
    for item in order.items:
        if item.type == 'payment':
            # Payment should be reasonable in value
            if item.amount >= (-1 * MAX_TOTAL) and item.amount <= MAX_TOTAL:
                net += Decimal(str(item.amount))
        elif item.type == 'product':
            # Product should be reasonable in quantity and value
            if item.quantity > 0 and item.quantity <= MAX_QUANTITY and item.amount > 0 and item.amount <= MAX_ITEM_VALUE:
                net -= Decimal(str(item.amount * item.quantity))
        elif net <= (-1 * MAX_TOTAL) or net >= MAX_TOTAL:
            return("Total amount exceeded: $%0.2f" % net)
        else:
            return("Invalid item type: %s" % item.type)
    
    if net != 0:
        # Printing only 2 digits hide the leftovers of a sum that doesn't convert as expected
        return("Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net))
    else:
        return("Order ID: %s - Full payment received!" % order.id)
