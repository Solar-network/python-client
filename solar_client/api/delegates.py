from solar_client.resource import Resource


class Delegates(Resource):
    def all(self, page=None, limit=100, **kwargs):
        extra_params = {name: kwargs[name] for name in kwargs if kwargs[name] is not None}
        params = {"page": page, "limit": limit, **extra_params}
        return self.request_get("delegates", params)

    def get(self, delegate_id):
        return self.request_get("delegates/{}".format(delegate_id))

    def blocks(self, delegate_id, page=None, limit=100, orderBy=None):
        params = {
            "page": page,
            "limit": limit,
            "orderBy": orderBy,
        }
        return self.request_get("delegates/{}/blocks".format(delegate_id), params)

    def voters(self, delegate_id, page=None, limit=100, orderBy=None):
        params = {
            "page": page,
            "limit": limit,
            "orderBy": orderBy,
        }
        return self.request_get("delegates/{}/voters".format(delegate_id), params)
