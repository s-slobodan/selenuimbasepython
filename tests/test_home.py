from page_objects.home_page import HomePage

class HomeTest(HomePage):
    def setUp(self):
        super().setUp()
        print("RUNNING BEFORE EACH TEST")
        # Login
        # self.open("https://practice.automationbro.com/my-account")
        # self.add_text("#username", "testuser")
        # self.add_text("#password", "testuser123")
        # self.click("button[name=login]")
        # self.assert_text("Log out", ".woocommerce-MyAccount-content")

        # open home page
        self.open_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")

        # Logout
        # self.open("https://practice.automationbro.com/my-account")
        # self.click("woocommerce-MyAccount-content a[href*=logout]")
        # self.assert_text_visible("button[name=login]")

        super().tearDown()

    def test_home_page(self ):
        # assert title
        self.assert_title("Practice E-Commerce Site – Automation Bro")

        # assert logo
        self.assert_element(HomePage.logo_icon)

        # click on the get started button and assert the url
        self.click(HomePage.get_started_btn)
        get_started_url=self.get_current_url()
        self.assert_equal(get_started_url, "https://practice.automationbro.com/#get-started")
        self.assert_true("get-started" in get_started_url)

        # get the text of the header and assert the value
        self.assert_text("Think different. Make different.", HomePage.heading_text)

        # exercise scroll to bottom and assert copyright text
        self.scroll_to_bottom()
        self.assert_text("Copyright © 2020 Automation Bro", HomePage.copyright_text)

    def test_menu_links(self):
        expected_links = ['Home','About','Shop','Blog','Contact','My account','Home','About','Blog','Contact','Support Form']

        # find elements
        menu_links_el = self.find_elements(HomePage.menu_links)

        # loop through links
        for idx, link_el in enumerate(menu_links_el):
            # print(idx, link_el.text)
            self.assert_equal(expected_links[idx], link_el.text)