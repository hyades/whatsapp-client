import logging

from base_receiever import BaseReceiver

__all__ = ['MessageReceiver']


class MessageReceiver(BaseReceiver):

    def onMessage(self, messageProtocolEntity):
        logging.info('Got Message: {0}'.format(messageProtocolEntity))
        try:
            logging.info("Sending message to application")
            logging.info("Sent data to application")
            receipt = MessageReceiver.getReceiptEntity(messageProtocolEntity)
            logging.info("Sent receipt of message to WhatsApp server")
            self.toLower(receipt)
        except Exception as e:
            logging.error(e)
            logging.error("Error communicating with the application")
