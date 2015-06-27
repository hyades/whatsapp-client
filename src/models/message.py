class Message(object):

    """docstring for Message"""

    def __init__(self, from_addr, text, whatsapp_msg_id=None, timestamp=None):
        super(Message, self).__init__()
        self.whatsapp_msg_id = whatsapp_msg_id
        self.from_addr = from_addr
        self.text = text
        self.timestamp = timestamp

    def __str__(self):
        return "<WhatsApp Message :: From: {1}, Body: {2}>".format(
            self.from_addr,
            self.text
        )

    def __repr__(self):
        return self.__str__()
