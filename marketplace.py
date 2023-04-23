"""
This module represents the Marketplace.

Computer Systems Architecture Course
Assignment 1
March 2021
"""
from logging.handlers import RotatingFileHandler
import threading
import logging
import time

import unittest


class Marketplace:
    """
    # Class that represents the Marketplace. It's the central part of the implementation.
    # The producers and consumers use its methods concurrently.
    """

    def __init__(self, queue_size_per_producer):
        """
        # Constructor

        # :type queue_size_per_producer: Int
        # :param queue_size_per_producer: the maximum size of a queue associated with each producer
        """
        self.queue_size_per_producer = queue_size_per_producer

        # list of lists of products, each list of products belonging to a producer
        self.products = []
        self.all_products = []  # stores all products associated with a producer
        self.products_lock = threading.Lock()  # lock for creating a producer
        self.id_producer = 0  # id of the producer

        self.carts = []  # list of lists of products, each list of products belonging to a cart
        self.carts_lock = threading.Lock()  # lock for creating a cart
        self.id_cart = 0  # id of the cart
        # lock for removing product in cart/products, because remove is not thread safe
        self.lock_remove = threading.Lock()
        self.lock_print = threading.Lock()  # lock for printing, not to interleave prints

        # logging
        self.logger = logging.getLogger('logger_tema1_asc')
        self.logger.setLevel(logging.INFO)
        self.handler = RotatingFileHandler(
            "marketplace.log", maxBytes=1024 * 512, backupCount=50)
        self.formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s')
        self.handler.setFormatter(self.formatter)
        self.formatter.converter = time.gmtime
        self.logger.addHandler(self.handler)

    def register_producer(self):
        """
        # Returns an id for the producer that calls this. Creates a new list of products
                                                    for the producer in products matrix.
        """
        self.logger.info("Registering producer")
        with self.products_lock:
            self.products.append([])
            self.all_products.append([])
            self.id_producer += 1
            self.logger.info("New producer with id: %d", self.id_producer - 1)
            return self.id_producer - 1

    def publish(self, producer_id, product):
        """
        # Adds the product provided by the producer to the marketplace only if the 
        #                                             producer's queue is not full.
        # Append product in products matrix in the row corresponding to the producer id.
        # Also append product in all_products matrix in the row corresponding to the producer id.

        # :type producer_id: String
        # :param producer_id: producer id

        # :type product: Product
        # :param product: the Product that will be published in the Marketplace

        # :returns True or False. If the caller receives False, it should wait and then try again.
        """

        # append is thread safe, and also other thread cannot affect the list,
        # because access is made only by the producer_id

        if len(self.products[producer_id]) >= self.queue_size_per_producer:
            return False
        self.logger.info("Producer %d wants to publish %s",
                         producer_id, product)
        self.products[producer_id].append(product)
        self.all_products[producer_id].append(product)
        self.logger.info("Producer %d published %s", producer_id, product)
        return True

    def new_cart(self):
        """
        # Creates a new cart for the consumer
        # Creates a new list of products for the cart in carts matrix.

        # :returns an int representing the cart_id
        """
        self.logger.info("Creating new cart")
        with self.carts_lock:
            self.carts.append([])
            self.id_cart += 1
            self.logger.info("New cart with id: %d", self.id_cart - 1)
            return self.id_cart - 1

    def add_to_cart(self, cart_id, product):
        """
        # Adds a product to the given cart. 
        # Search for product in matrix products and remove it from the list 
        #                                         of products of the producer.
        # Append the product in the list of products of the cart by cart_id.

        # :type cart_id: Int
        # :param cart_id: id cart

        # :type product: Product
        # :param product: the product to add to cart

        # :returns True or False. If the caller receives False, it should wait and then try again
        """
        self.logger.info("Cart %d wants to add %s", cart_id, product)

        for producer in self.products:
            if product in producer:
                with self.lock_remove:
                    j = self.products.index(producer)
                    self.products[j].remove(product)
                self.carts[cart_id].append(product)
                self.logger.info(
                    "In cart %d was addes %s", cart_id, product)
                return True
        self.logger.error("In cart %d was not added %s", cart_id, product)
        return False

    def remove_from_cart(self, cart_id, product):
        """
        # Removes a product from cart.
        # Find product in matrix carts and remove it. Find product in matrix all_products 
        #                         and append it in the list of products of the producer.

        # :type cart_id: Int
        # :param cart_id: id cart

        # :type product: Product
        # :param product: the product to remove from cart
        """
        self.logger.info("Cart %d wants to remove %s", cart_id, product)
        for prod in self.carts[cart_id]:
            if prod == product:
                with self.lock_remove:
                    self.carts[cart_id].remove(product)
                for prod in self.all_products:
                    if product in prod:
                        self.products[self.all_products.index(
                            prod)].append(product)
                self.logger.info(
                    "From cart %d was removed %s", cart_id, product)
                return True
        self.logger.error("Product %s not found in cart %d", product, cart_id)
        return False

    def place_order(self, cart_id):
        """
        # Return a list with all the products in the cart.
        # Print the products bought by the consumer.

        # :type cart_id: Int
        # :param cart_id: id cart
        """
        self.logger.info(
            "Consumer wants to buy products from cart %d", cart_id)

        products_in_cart = self.carts[cart_id]

        for product in products_in_cart:
            with self.lock_print:
                print(threading.current_thread().name +
                      " bought " + str(product))
                self.logger.info("Consumer %s bought %s",
                                 str(threading.current_thread().name), str(product))

        return products_in_cart


class TestMarketplace(unittest.TestCase):
    """
    # Test class for Marketplace
    """

    def setUp(self):
        self.marketplace = Marketplace(3)

    def test_register_producer(self):
        """
        # Test register_producer method
        """
        producer_id_1 = self.marketplace.register_producer()
        self.assertEqual(producer_id_1, 0)
        producer_id_2 = self.marketplace.register_producer()
        self.assertEqual(producer_id_2, 1)
        producer_id_3 = self.marketplace.register_producer()
        self.assertNotEqual(producer_id_3, 3)

    def test_publish(self):
        """
        # Test publish method
        """
        producer_id = self.marketplace.register_producer()
        product_1 = "product1"
        product_2 = "product2"
        product_3 = "product3"
        product_4 = "product4"
        self.assertTrue(self.marketplace.publish(producer_id, product_1))
        self.assertTrue(self.marketplace.publish(producer_id, product_2))
        self.assertTrue(self.marketplace.publish(producer_id, product_3))
        self.assertFalse(self.marketplace.publish(producer_id, product_4))

    def test_new_cart(self):
        """
        # Test new_cart method
        """
        cart_id_1 = self.marketplace.new_cart()
        self.assertEqual(cart_id_1, 0)
        cart_id_2 = self.marketplace.new_cart()
        self.assertEqual(cart_id_2, 1)
        cart_id_3 = self.marketplace.new_cart()
        self.assertNotEqual(cart_id_3, 3)

    def test_add_to_cart(self):
        """
        # Test add_to_cart method
        """
        producer_id_1 = self.marketplace.register_producer()
        producer_id_2 = self.marketplace.register_producer()
        product_1 = "product1"
        product_2 = "product2"
        product_3 = "product3"
        product_4 = "product4"
        self.marketplace.publish(producer_id_1, product_1)
        self.marketplace.publish(producer_id_1, product_2)
        self.marketplace.publish(producer_id_2, product_3)

        cart_id = self.marketplace.new_cart()
        self.assertTrue(self.marketplace.add_to_cart(cart_id, product_1))
        self.assertTrue(self.marketplace.add_to_cart(cart_id, product_2))
        self.assertTrue(self.marketplace.add_to_cart(cart_id, product_3))
        self.assertFalse(self.marketplace.add_to_cart(cart_id, product_4))

    def test_remove_from_cart(self):
        """
        # Test remove_from_cart method
        """
        producer_id_1 = self.marketplace.register_producer()
        producer_id_2 = self.marketplace.register_producer()
        product_1 = "product1"
        product_2 = "product2"
        product_3 = "product3"
        self.marketplace.publish(producer_id_1, product_1)
        self.marketplace.publish(producer_id_1, product_2)
        self.marketplace.publish(producer_id_2, product_3)

        cart_id = self.marketplace.new_cart()
        self.marketplace.add_to_cart(cart_id, product_1)
        self.marketplace.add_to_cart(cart_id, product_2)
        self.marketplace.add_to_cart(cart_id, product_3)

        self.assertTrue(self.marketplace.remove_from_cart(cart_id, product_1))
        self.assertFalse(self.marketplace.remove_from_cart(cart_id, product_1))
        self.assertTrue(
            self.marketplace.remove_from_cart(cart_id, product_3))

