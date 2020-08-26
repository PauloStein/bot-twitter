import time


class Twitter:

    def find_users(self, hashtag, bot):
        bot = bot
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typed_query')
        time.sleep(3)
        follow_bot = Twitter()

        for i in range(1, 3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(3)
            tweets = bot.find_elements_by_partial_link_text('@')
            links = [elem.get_attribute('href')
                     for elem in tweets]
            for link in links:
                follow_bot.follow_tweet(link, bot)

    def follow_tweet(self, link, bot):
        follow_bot = Twitter()
        link_twitter = link
        bot = bot
        bot.get(link_twitter)
        time.sleep(4)
        try:
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
            follow_bot.save_file(link_twitter)
            time.sleep(5)

        except Exception as ex:
            print(ex)
            time.sleep(5)

    def save_file(self, link):
        link_twitter = link
        try:
            file = open("links.txt", "a")
            file.write(link_twitter)
            file.write("\n")
            file.close()
        except Exception as ex:
            print(ex)
