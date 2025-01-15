from src.mengine.interfaces.i_connection import Connection


class ConcreteConnection(Connection):

    def __init__(self, requester_ip, payload):
        self.requester_ip = requester_ip
        self.payload = payload
        self.method = None
        self.version = None

    def get_requester_ip(self):
        return self.requester_ip

    def get_payload(self):
        return self.payload

    def set_requester_ip(self, requester_ip):
        self.requester_ip = requester_ip

    def set_payload(self, payload):
        self.payload = payload

    def get_method(self):
        return self.method

    def set_method(self, method_val):
        self.method = method_val

    def get_version(self):
        return self.version

    def set_version(self, version_val):
        self.version = version_val
