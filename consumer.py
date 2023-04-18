"""
This module represents the Consumer.

Computer Systems Architecture Course
Assignment 1
March 2021
"""

from threading import Thread
import time

class Consumer(Thread):
    """
    Class that represents a consumer.
    """

    # Class that represents a consumer.

    def __init__(self, carts, marketplace, retry_wait_time, **kwargs):

        # Constructor.

        # :type carts: List
        # :param carts: a list of add and remove operations

        # :type marketplace: Marketplace
        # :param marketplace: a reference to the marketplace

        # :type retry_wait_time: Time
        # :param retry_wait_time: the number of seconds that a producer must wait
        # until the Marketplace becomes available

        # :type kwargs:
        # :param kwargs: other arguments that are passed to the Thread's __init__()

        Thread.__init__(self, **kwargs)

        self.carts = carts
        self.marketplace = marketplace
        self.retry_wait_time = retry_wait_time
        self.kwargs = kwargs

    def run(self):

        # Creates a new cart and performs add/remove operations on this
        # cart. When all operations have been performed, the order for the cart
        # is placed  When a cart operation fails, the consumer sleeps for
        # retry_wait_time seconds.

        for cart in self.carts:
            cart_id = self.marketplace.new_cart()
            for oper in cart:
                number_ops = 0
                while number_ops < oper["quantity"]:
                    if oper["type"] == "add":
                        if self.marketplace.add_to_cart(cart_id, oper["product"]):
                            number_ops += 1
                        else:
                            time.sleep(self.retry_wait_time)
                    elif oper["type"] == "remove":
                        self.marketplace.remove_from_cart(
                            cart_id, oper["product"])
                        number_ops += 1
            self.marketplace.place_order(cart_id)

