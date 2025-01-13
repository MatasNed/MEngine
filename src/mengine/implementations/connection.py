from src.mengine.interfaces.i_connection import Connection


class ConcreteConnection(Connection):
    def __init__(self, requester_ip, payload):
        self.requester_ip = requester_ip
        self.payload = payload

    def get_requester_ip(self):
        return self.requester_ip

    def get_payload(self):
        return self.payload

    def set_requester_ip(self, requester_ip):
        self.requester_ip = requester_ip

    def set_payload(self, payload):
        self.payload = payload
