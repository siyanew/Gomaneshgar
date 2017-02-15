class Message:
    def __init__(self, chat_id=""):
        self.chat_id = chat_id

    def set_text(self, text, parse_mode=None, disable_web_page_preview=None, disable_notification=None,
                 reply_to_message_id=None, reply_markup=None):
        self.text = text
        self.parse_mode = parse_mode
        self.disable_web_page_preview = disable_web_page_preview
        self.disable_notification = disable_notification
        self.reply_to_message_id = reply_to_message_id
        self.reply_markup = reply_markup
        return self
