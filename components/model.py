from dataclasses import dataclass


@dataclass
class Flight:
    callsign: str
    origin: str
    destination: str
