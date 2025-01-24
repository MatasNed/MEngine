from abc import ABC, abstractmethod


class IRequestQueueConsumer(ABC):

    @abstractmethod
    def consume(self):
        pass
