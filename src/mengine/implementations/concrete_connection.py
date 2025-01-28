from src.mengine.interfaces.i_connection import IConnection


class ConcreteConnection(IConnection):

    def __init__(self, requester_ip, payload, method="GET", version="HTTP/1.1"):
        self.requester_ip_and_port = tuple(requester_ip)
        self.payload = payload
        self.method = method
        self.version = version

    def get_requester_ip(self):
        return self.requester_ip_and_port

    def get_payload(self):
        return self.payload

    def set_requester_ip(self, requester_ip):
        self.requester_ip_and_port = requester_ip

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
