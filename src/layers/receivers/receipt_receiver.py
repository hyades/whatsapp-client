from layers.receivers.base_receiever import BaseReceiver


class ReceiptReceiver(BaseReceiver):

    def onReceipt(self, receiptEntity):
        ack = ReceiptReceiver.getAckEntity(receiptEntity)
        self.toLower(ack)
