from page_objects.cart_page import CartPage
from selenium.webdriver.common.keys import Keys

class CartTest(CartPage):

    def setUp(self):
        super().setUp()
        self.open("https://practice.automationbro.com/shop")

    def test_add_to_cart(self):
        # add item
        self.click(self.converse_add_to_cart_btn)

        # assert product
        self.assert_text("1", self.cart_count_text)

        # open cart
        self.open_page()

        # get subtotal
        text = self.get_text(self.subtotal_text)
        print(text)

        # change quantity
        self.set_value(self.product_quantity_input, "2")
        self.send_keys(self.product_quantity_input, Keys.RETURN)
        self.click(self.update_cart_btn)

        # wait
        self.wait_for_element_visible(self.loading_overlay)
        self.wait_for_element_not_visible(self.loading_overlay)

        # assert updatd subtotal
        updated_text = self.get_text(self.subtotal_text)
        print(updated_text)

        # assert subtotal
        self.assert_not_equal(text, updated_text)