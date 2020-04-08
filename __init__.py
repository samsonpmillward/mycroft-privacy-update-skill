from mycroft import MycroftSkill, intent_file_handler


class PrivacyUpdate(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('update.privacy.intent')
    def handle_update_privacy(self, message):
        self.speak_dialog('update.privacy')


def create_skill():
    return PrivacyUpdate()
