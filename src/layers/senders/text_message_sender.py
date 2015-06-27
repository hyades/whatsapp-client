import logging
from yowsup.layers.protocol_messages.protocolentities import TextMessageProtocolEntity

from layers.senders.base_sender import BaseSender


class TextMessageSender(BaseSender):
    MESSAGES = ""

    def onSuccess(self, entity):
        logging.info("Successfully connected. Sending messages")
        for message in self.getProp(self.__class__.MESSAGES, []):
            logging.info(message)
            outgoingMessage = TextMessageProtocolEntity(
                message.text,
                to=message.to
            )
            logging.info("Sending Message ID: {0}".format(outgoingMessage.getId()))
            self.toLower(outgoingMessage)
            logging.info("Sent!")
