from json import loads
from typing import List
from urllib.request import urlopen
from .model import Flight


def fetch(url: str):
    with urlopen(url) as res:
        return res.read().decode()


class Vatsim:
    URL = "https://data.vatsim.net/v3/vatsim-data.json"

    def data(self) -> List[Flight]:
        print("DEBUG: Fetching data!")

        body = fetch(self.URL)
        dataset = loads(body)

        flights = []

        for flight in dataset["pilots"]:
            plan = flight.get("flight_plan")

            flights.append(Flight(
                callsign=flight["callsign"],
                origin=plan["departure"] if plan else None,
                destination=plan["arrival"] if plan else None
            ))

        return flights
