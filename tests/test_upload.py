from seleniumbase import BaseCase

class UploadTest(BaseCase):
    def test_visible_upload(self):
        # open the page
        self.open("https:/the-internet.herokuapp.com/upload")

        # get file path
        file_path = './data/hp.jpg'

        # upload file
        self.choose_file("#file-upload", file_path)

        # click upload button
        self.click("#file-submit")

        # assert
        self.assert_text("File Uploaded!", "h3")


    def test_hidden_upload(self):
        # open the page
        self.open_new_window()
        self.open("https://practice.automationbro.com/cart/")

        # get the file path
        file_path = './data/hp.jpg'

        # add js code
        remove_hidden_class = "document.getElementById('upfile_1').classList.remove('file_input_hidden')"
        self.add_js_code(remove_hidden_class)

        # upload file
        self.choose_file("#upfile_1", file_path)

        # click upload button
        self.click("#upload_1")

        # assert the upload text
        self.assert_text("uploaded successfully", "#wfu_messageblock_header_1_label_1")