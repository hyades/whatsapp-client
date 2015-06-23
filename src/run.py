import os
import sys
sys.path.insert(0, os.path.abspath('..'))

from layers.receivers.message_receiver import MessageReceiver

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


CREDENTIALS = (
    conf.phone,
    conf.password
)


def main():
    logging.debug("Starting up...")
    layers = (
        MessageReceiver,
        (YowAuthenticationProtocolLayer, YowMessagesProtocolLayer,
         YowReceiptProtocolLayer, YowAckProtocolLayer)
    ) + YOWSUP_CORE_LAYERS

    stack = YowStack(layers)
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
    main()
