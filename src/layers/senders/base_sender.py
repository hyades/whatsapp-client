import logging

from yowsup.layers import YowLayer


class BaseSender(YowLayer):

    def receive(self, protocolEntity):
        tag = protocolEntity.getTag()
        logging.debug('Got tag: ' + tag)

        def getReiever(tag):
            handlers = {
                'success': self.onSuccess,
            }
            if tag in handlers:
                return handlers[tag]
            else:
                return lambda x: x

        getReiever(tag)(protocolEntity)

    def onSuccess(self, protocolEntity):
        pass

