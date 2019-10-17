from abc import ABC, abstractmethod


class APIProxy(ABC):
    def __init__(self):
        self.req = None
        self.id = None

    @abstractmethod
    def get_data(self):
        pass
