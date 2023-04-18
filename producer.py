"""
This module represents the Producer.

Computer Systems Architecture Course
Assignment 1
March 2021
"""

from threading import Thread
import time


class Producer(Thread):
    """
    Class that represents a producer.
    """

    def __init__(self, products, marketplace, republish_wait_time, **kwargs):
        # Constructor.

        # @type products: List()
        # @param products: a list of products that the producer will produce

        # @type marketplace: Marketplace
        # @param marketplace: a reference to the marketplace

        # @type republish_wait_time: Time
        # @param republish_wait_time: the number of seconds that a producer must
        # wait until the marketplace becomes available

        # @type kwargs:
        # @param kwargs: other arguments that are passed to the Thread's __init__()

        Thread.__init__(self, **kwargs)

        self.products = products
        self.marketplace = marketplace
        self.republish_wait_time = republish_wait_time
        self.kwargs = kwargs

        self.producer_id = marketplace.register_producer()

    def run(self):
        # Adds products stored in the current producer to the Marketplace
        # When all products have been published, the product list is iterated again.
        # If the publish operation succeeds, the producer sleeps for the time
        # associated with the current poduct.
        # Otherwise, it sleeps for republish_wait_time
        while True:
            for (prod, nr_prod, wait_time) in self.products:
                index = 0
                while index < nr_prod:
                    if self.marketplace.publish(self.producer_id, prod):
                        # produce item
                        index += 1
                        time.sleep(wait_time)
                    else:
                        # publish failed, retry after a timeout
                        time.sleep(self.republish_wait_time)

