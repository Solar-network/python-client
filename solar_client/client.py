import inspect
import pkgutil
from importlib import import_module
from pathlib import Path

from solar_client.connection import Connection
from solar_client.resource import Resource


class SolarClient(object):
    def __init__(self, hostname):
        """
        :param string hostname: Node hostname. Examples: `http://127.0.0.1:6002` or
            `http://my.domain.io/api/`. This is to allow people to server the api
            on whatever url they want.
        """
        self.connection = Connection(hostname)
        self._import_api()

    def _import_api(self):
        """
        Dynamically imports API endpoints.
        """
        modules = pkgutil.iter_modules([str(Path(__file__).parent / "api")])
        for _, name, _ in modules:
            module = import_module("solar_client.api.{}".format(name))
            for attr in dir(module):
                # If attr name is `Resource`, skip it as it's a class and also has a
                # subclass of Resource
                if attr == "Resource":
                    continue

                attribute = getattr(module, attr)
                if inspect.isclass(attribute) and issubclass(attribute, Resource):
                    # Set module class as a property on the client
                    setattr(self, name, attribute(self.connection))
