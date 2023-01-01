from dataclasses import dataclass


@dataclass
class Aircraft:
    name: str
    iata: str
    icao: str


@dataclass
class Airline:
    name: str
    iata: str
    icao: str
    callsign: str
    country: str


@dataclass
class Airport:
    name: str
    city: str
    country: str
    iata: str
    icao: str
    latitude: float
    longitude: float
    elevation: int


@dataclass
class Flight:
    callsign: str
    aircraft: str
    latitude: str
    longitude: str
    altitude: str
    speed: str
    origin: str
    destination: str
