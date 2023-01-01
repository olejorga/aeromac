from components.api import Api
from components.vatsim import Vatsim
from components.service import Service


LOGO = """
       d8888 8888888888 8888888b.   .d88888b.  888b     d888        d8888  .d8888b. 
      d88888 888        888   Y88b d88P" "Y88b 8888b   d8888       d88888 d88P  Y88b
     d88P888 888        888    888 888     888 88888b.d88888      d88P888 888    888
    d88P 888 8888888    888   d88P 888     888 888Y88888P888     d88P 888 888       
   d88P  888 888        8888888P"  888     888 888 Y888P 888    d88P  888 888       
  d88P   888 888        888 T88b   888     888 888  Y8P  888   d88P   888 888    888
 d8888888888 888        888  T88b  Y88b. .d88P 888   "   888  d8888888888 Y88b  d88P
d88P     888 8888888888 888   T88b  "Y88888P"  888       888 d88P     888  "Y8888P"
"""


def main():
    print(LOGO)

    provider = Vatsim()
    service = Service(provider)
    api = Api(service)

    api.start()


if __name__ == "__main__":
    main()
