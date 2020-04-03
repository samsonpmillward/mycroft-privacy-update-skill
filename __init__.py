from mycroft import MycroftSkill, intent_file_handler
import feedparser

class PrivacyUpdate(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('update.privacy.intent')
    def handle_update_privacy(self, message):
        self.speak_dialog('update.privacy')
    def readFeed():
        
        url= "http://fetchrss.com/rss/5e8742188a93f83f138b45675e8741f48a93f8cc108b4567.xml"
        feed = feedparser.parse(url)

        for post in feed.entries:
        date = "(%d/%02d/%02d)" % (post.published_parsed.tm_year,\
        post.published_parsed.tm_mon, \
        post.published_parsed.tm_mday)
        print("post date: " + date)
        print("post title: " + post.title)
        print("post link: " + post.link)

def create_skill():
    return PrivacyUpdate()

