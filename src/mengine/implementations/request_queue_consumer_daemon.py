import threading

from time import sleep
from src.mengine.interfaces.i_request_queue_consumer import IRequestQueueConsumer
from src.mengine.interfaces.i_request_dispatcher import IRequestDispatcher
from src.mengine.utils.log_utils import logging_deco
"""
This class runs on it's own thread perodically emptying the request queue
and passing on the request to the backend
"""


class RequestQueueConsumerDaemon(IRequestQueueConsumer):

    def __init__(self, request_queue: IRequestDispatcher, timer: int):
        self.request_queue = request_queue
        self.timer = timer
        self.stop_event = threading.Event()

    @logging_deco
    def consume(self):
        while not self.stop_event.is_set():
            sleep(self.timer)
            self.request_queue.dispatch_request()

    def stop(self):
        self.stop_event.set()
