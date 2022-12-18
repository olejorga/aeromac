from threading import Thread
from time import sleep


class Service:
    def __init__(self, flights_provider):
        self.__flights_provider = flights_provider
        self.__flights = []
        
        self.__handler = Thread(target=self.__workflow, daemon=True)

    def __workflow(self):
        while(True):
            self.__flights = self.__flights_provider.data()
            sleep(60)

    def start(self):
        self.__handler.start()

    @property
    def flights(self):
        return self.__flights


