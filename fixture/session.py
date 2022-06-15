# -*- coding: utf-8 -*-
class SessionHelper:

    def __init__(self, app, base_url):
        self.app = app
        self.base_url = base_url

    def open_home_page(self):
        wd = self.app.wd
        # open home page
        wd.get(self.base_url)

    def login(self, username, passw):
        wd = self.app.wd
        # open home page
        self.open_home_page()
        # login
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys(username)
        wd.find_element_by_css_selector("input[type='submit']").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(passw)
        wd.find_element_by_css_selector("input[type='submit']").click()


    def logout(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("user-info'").click()
        wd.find_element_by_css_selector("link='/mantisbt-2.25.4/logout_page.php'").click()

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_css_selector("a[href='/mantisbt-2.25.4/account_page.php']").text

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return self.get_logged_user() == username

    def ensure_login(self, username, passw):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, passw)
