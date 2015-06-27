import logging

from yowsup.layers import YowLayer
from yowsup.layers.protocol_receipts.protocolentities import OutgoingReceiptProtocolEntity
from yowsup.layers.protocol_acks.protocolentities import OutgoingAckProtocolEntity


__all__ = ['BaseReceiver']


class BaseReceiver(YowLayer):

    def receive(self, protocolEntity):
        tag = protocolEntity.getTag()
        logging.debug('Got tag: ' + tag)

        def getReiever(tag):
            handlers = {
                'message': self.onMessage,
                'iq': self.onIq,
                'ib': self.onIb,
                'notification': self.onNotification,
                'presence': self.onPresence,
                'receipt': self.onReceipt,
                'ack': self.onAck
            }
            if tag in handlers:
                return handlers[tag]
            else:
                return lambda x: x

        getReiever(tag)(protocolEntity)

    def onMessage(self, protocolEntity):
        pass

    def onIq(self, protocolEntity):
        pass

    def onIb(self, protocolEntity):
        pass

    def onNotification(self, protocolEntity):
        pass

    def onPresence(self, protocolEntity):
        pass

    def onReceipt(self, protocolEntity):
        pass

    def onAck(self, protocolEntity):
        pass

    @classmethod
    def getReceiptEntity(cls, messageProtocolEntity):
        return OutgoingReceiptProtocolEntity(
            messageProtocolEntity.getId(),
            messageProtocolEntity.getFrom(),
            'read',
            messageProtocolEntity.getParticipant()
        )

    @classmethod
    def getAckEntity(cls, receiptEntity):
        return OutgoingAckProtocolEntity(
            receiptEntity.getId(),
            "receipt",
            "delivery",
            receiptEntity.getFrom()
        )
