from satlink import Satellite


class Api:
    def __init__(self, service):
        self.__service = service
        self.__satellite = Satellite()
        self.__satellite.get("/flights")(self.__flights)

    def __flights(self, uplink, downlink):
        flights = [f.__dict__ for f in self.__service.flights]
        return downlink.json(flights)

    def start(self):
        self.__service.start()
        self.__satellite.transmit()
