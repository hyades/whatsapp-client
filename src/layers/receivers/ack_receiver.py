import logging
from layers.receivers.base_receiever import BaseReceiver


class AckReceiver(BaseReceiver):

    def onAck(self, ackEntity):
        logging.info("Got Ack! {0}".format(ackEntity.getId()))
