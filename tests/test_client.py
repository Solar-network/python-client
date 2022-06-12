from solar_client.client import SolarClient
from solar_client.connection import Connection


def test_client_creation_calls_import_api(mocker):
    import_mock = mocker.patch.object(SolarClient, "_import_api")

    client = SolarClient("http://127.0.0.1:4002")

    assert isinstance(client.connection, Connection)
    assert import_mock.call_count == 1
