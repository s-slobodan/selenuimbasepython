from selenium.common.exceptions import NoSuchElementException
from page_objects.shop_page import ShopPage

class ShopTest(ShopPage):
    def test_search_products(self):
        # open page
        self.open_page()

        # search for products
        self.send_keys(self.search_input, "Toys")
        self.click(self.search_btn)

        # assert product image
        try:
            print("in try block")
            self.assert_element(self.product_img)
        except NoSuchElementException:
            print("in exception block")
            self.assert_text("No products were found matching your selection.", self.no_product_txt)