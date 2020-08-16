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
        time.sleep(5)
        email = bot.find_element_by_name('session[username_or_email]')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(5)

    def follow_tweet(self, hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typed_query')
        time.sleep(3)

        for i in range(1, 3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(3)
            tweets = bot.find_elements_by_partial_link_text('@')
            links = [elem.get_attribute('href')
                     for elem in tweets]

            for link in links:
                bot.get(link)
                time.sleep(4)
                try:
                    arquivo = open("links.txt", "a")
                    # bot.find_element_by_xpath('//div[@data-testid="placementTracking"]').click()
                    bot.execute_script("""
                                        let nodeElements = document.querySelectorAll("[data-testid]");
                                        let unfollowArray = Array.from(nodeElements)
                                            .filter(btn => btn.getAttribute('data-testid').includes('unfollow'))
                                            .map(ref => ({ ref, type: 'unfollow' }))
                                        let followArray = Array.from(nodeElements)
                                            .filter(btn => btn.getAttribute('data-testid').includes('follow'))
                                            .filter(btn => !btn.getAttribute('data-testid').includes('unfollow'))
                                            .map(ref => ({ ref, type: 'follow' }))

                                        let pageButtons = [].concat(unfollowArray, followArray);
                                        let targetButton = pageButtons[0];

                                        if (targetButton.type === "follow") {
                                            targetButton.ref.click()}
                                        """)

                    time.sleep(5)
                    print(f'follow {link}')
                    arquivo.write(link)
                    arquivo.write("\n")
                    arquivo.close()

                except Exception as ex:
                    print(ex)
                    time.sleep(10)


user = TwitterBot('PauloE010102', 'paulotcc321')
user.login()
user.follow_tweet('follow')
