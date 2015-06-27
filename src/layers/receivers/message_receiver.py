import logging

from layers.receivers.base_receiever import BaseReceiver
from models.message import Message
from third_party.create_ticket import CreateTicketRequest
from conf import API_KEY, API_PASSWORD

__all__ = ['MessageReceiver']


class MessageReceiver(BaseReceiver):

    def onMessage(self, messageProtocolEntity):
        logging.info('Got Message: {0}'.format(messageProtocolEntity))
        message = Message(
            whatsapp_msg_id=messageProtocolEntity.getId(),
            from_addr=messageProtocolEntity.getFrom(),
            text=messageProtocolEntity.getBody(),
            timestamp=messageProtocolEntity.getTimestamp()
        )
        try:
            logging.info("Sending message to application")
            auth = (API_KEY, API_PASSWORD)
            request = CreateTicketRequest(auth, message)
            if not request.check_valid_response:
                logging.info("Error in request")
                raise Exception("Error sending data to remote server")
            logging.info(request.response.json())
            logging.info("Sent data to application")
            receipt = MessageReceiver.getReceiptEntity(messageProtocolEntity)
            logging.info("Sent receipt of message to WhatsApp server")
            self.toLower(receipt)
        except Exception:
            import traceback
            logging.error(traceback.format_exc())
            logging.error("Error communicating with the application")
