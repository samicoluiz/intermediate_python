import unittest
import surfshop


class TestShop(unittest.TestCase):
    def setUp(self):
        self.cart = surfshop.ShoppingCart()


    def test_add_surfboards(self):
        for i in range(2, 5):
            with self.subTest(i):
                self.assertEqual(self.cart.add_surfboards(i), f'Successfully added {i} surfboards to cart!')
                self.cart = surfshop.ShoppingCart()

    @unittest.skip
    def test_too_many_boards(self):
        self.assertRaises(surfshop.TooManyBoardsError, self.cart.add_surfboards, 5)

    @unittest.expectedFailure
    def test_apply_locals_discount(self):
        self.cart.apply_locals_discount()
        self.assertTrue(self.cart.locals_discount)

unittest.main()
