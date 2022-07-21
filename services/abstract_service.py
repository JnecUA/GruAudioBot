from typing import Any
from pymongo.collection import Collection


class AbstractService:
    def __init__(self, collection: Collection) -> None:
        self.model = collection

    def create_simple_query(self, vars: dict[str, Any]) -> dict[str, Any]:
        """Creates a dictionary from function variables obtained using locals()

        Args:
            vars (dict[str, Any]): use locals()

        Returns:
            dict[str, Any]: dict to database query
        """
        query = {}
        for key, value in vars.items():
            if (key != 'self' and key != 'query') and (value != None):
                query[key] = value
        return query
