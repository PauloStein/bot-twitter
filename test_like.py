# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# import time
#
#
# class TwitterBot:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
#         self.bot = webdriver.Firefox()
#
#     def login(self):
#         bot = self.bot
#         bot.get('https://twitter.com')
#         time.sleep(3)
#         email = bot.find_element_by_name('session[username_or_email]')
#         password = bot.find_element_by_name("session[password]")
#         email.clear()
#         password.clear()
#         email.send_keys(str(self.username))
#         password.send_keys(str(self.password))
#         password.send_keys(str(password.submit()))
#         time.sleep(3)
#
#     def like_tweet(self, hashtag):
#         bot = self.bot
#         # Serch browser
#         bot.get('https://twitter.com/search?q=' + hashtag + '&src=typed')
#         time.sleep(3)
#         # Scroll down
#         for i in range(1, 9):
#             bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
#             time.sleep(2)
#             # Search for each tweets
#             tweets = bot.find_elements_by_xpath('//*[@data-testid="tweet"]//a[@dir="auto"]')
#             # Link to each tweete and get data
#             links = [elem.get_attribute('href') for elem in tweets]
#             for link in links:
#                 bot.get(link)
#                 time.sleep(5)
#                 try:
#                     test = bot.find_element_by_xpath('//*[@aria-label="Curtir"]')
#                     time.sleep(3)
#                     print(test)
#                 except Exception as ex:
#                     time.sleep(5)
#                     print(ex)
#
#
# ed = TwitterBot('', '')
# ed.login()
# ed.like_tweet('test')