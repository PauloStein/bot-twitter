from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(3)
        email = bot.find_element_by_name('session[username_or_email]')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    def follow_tweet(self, hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typed_query')
        time.sleep(3)
        for i in range(1,3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(3)
            tweets = bot.find_elements_by_partial_link_text('@')
            links = [elem.get_attribute('href')
                     for elem in tweets]
            for link in links:
                bot.get(link)
                test = bot.find_elements_by_tag_name('span')
                test2 = [testt.get_property('Follow')
                         for testt in test]

                try:
                    # bot.find_element_by_partial_link_text('Follow').click()
                    # bot.find_element_by_link_text('Follow').click()
                    time.sleep(10)
                    print('foi')
                except Exception as ex:
                    time.sleep(10)
                    print('erro')


user = TwitterBot('', '')
user.login()
user.follow_tweet('python')
