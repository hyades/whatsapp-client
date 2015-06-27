class SendingMessage(object):

    def __init__(self, to, text):
        self.to = to
        self.text = text

    def __str__(self):
        return "<Sending WhatsApp Message :: To: {0}, Body: {1}>".format(
            self.to,
            self.text
        )

    def __repr__(self):
        return self.__str__()
