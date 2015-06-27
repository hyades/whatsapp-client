
from layers.senders.text_message_sender import TextMessageSender
from layers.receivers.ack_receiver import AckReceiver
from models.sending_message import SendingMessage

from yowsup.layers.auth import YowAuthenticationProtocolLayer
from yowsup.layers.protocol_messages import YowMessagesProtocolLayer
from yowsup.layers.protocol_receipts import YowReceiptProtocolLayer
from yowsup.layers.protocol_acks import YowAckProtocolLayer
from yowsup.layers.network import YowNetworkLayer
from yowsup.layers.coder import YowCoderLayer
from yowsup.common import YowConstants
from yowsup.layers import YowLayerEvent
from yowsup.stacks import YowStack, YOWSUP_CORE_LAYERS
from yowsup import env

import conf
import logging
logging.basicConfig(level=logging.INFO)
import httplib as http_client
http_client.HTTPConnection.debuglevel = 1

CREDENTIALS = (
    conf.phone,
    conf.password
)


def main(messages):
    logging.debug("Starting up...")

    layers = (
        (TextMessageSender, AckReceiver),
        (YowAuthenticationProtocolLayer, YowMessagesProtocolLayer,
         YowReceiptProtocolLayer, YowAckProtocolLayer)
    ) + YOWSUP_CORE_LAYERS

    stack = YowStack(layers)

    stack.setProp(TextMessageSender.MESSAGES, messages)
    # setting credentials
    stack.setProp(YowAuthenticationProtocolLayer.PROP_CREDENTIALS, CREDENTIALS)
    # whatsapp server address
    stack.setProp(YowNetworkLayer.PROP_ENDPOINT, YowConstants.ENDPOINTS[0])
    stack.setProp(YowCoderLayer.PROP_DOMAIN, YowConstants.DOMAIN)
    # info about us as WhatsApp client
    stack.setProp(YowCoderLayer.PROP_RESOURCE, env.CURRENT_ENV.getResource())

    # sending the connect signal
    stack.broadcastEvent(YowLayerEvent(YowNetworkLayer.EVENT_STATE_CONNECT))

    stack.loop()  # this is the program mainloop

if __name__ == '__main__':
    messages = [
        SendingMessage("919003273352@s.whatsapp.net", "hey1"),
        SendingMessage("919003273352@s.whatsapp.net", "hey2")
    ]
    main(messages)
