from third_party.base_request import BaseRequest


class CreateTicketRequest(BaseRequest):

    def __init__(self, auth, message):
        payload = {
            "helpdesk_ticket": {
                "description": {
                    "body": message.text,
                    "from": message.from_addr,
                    "timestamp": message.timestamp
                },
                "subject": "WhatsApp[{0}]".format(message.whatsapp_msg_id),
                "email": "whatsappbot@randomcompany.com",
                "priority": 1,
                "status": 2
            },
            "cc_emails": "xyz@randomcompany.com,abc@randomcompany.com"
        }
        url = '/helpdesk/tickets.json'
        super(CreateTicketRequest, self).__init__(auth, url, payload)
        self.post()

    def check_valid_response(self):
        if self.response.status_code != 200:
            return False
        return True
