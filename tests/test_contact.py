from seleniumbase import BaseCase

class ContactTest(BaseCase):
    def test_contact_page(self):
        # open the page
        self.open("https://practice.automationbro.com/contact")

        # scroll to form
        self.scroll_to("#evf-form-277")
        self.save_screenshot("empty_contact_form", "custom_screenshots")

        # fill all the fields
        self.send_keys('.contact-name input', 'Test Name')
        self.send_keys('.contact-email input', 'test_name@mail.com')
        self.send_keys('.contact-phone input', '123456789')
        self.send_keys('.contact-message textarea', 'Test message')

        # filled form screenshot
        self.scroll_to("#evf-form-277")
        self.save_screenshot("filled_contact_formp", "custom_screenshots")

        # click submit
        self.click("#evf-submit-277")

        # verify submit msg
        self.assert_text('Thanks for contacting us We will be in touch with you shortly', 'div[role=alert]')