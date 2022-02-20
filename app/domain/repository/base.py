import abc
from typing import Any, List


class AbstractRepository(abc.ABC):
    model = None

    def create(self, obj: Any) -> Any:
        return self.model.create()

    def first(self, criteria: dict) -> Any:
        return self.model.first(criteria=criteria)

    def filter_by(self, criteria: dict) -> Any:
        return self.model.filter_by(criteria=criteria)

    def get_by_id(self, _id: int) -> Any:
        return self.model.get_by_id(_id=_id)

    def update(self, _id: int, obj_in: Any) -> Any:
        data = obj_in.dict(exclude_unset=True)
        obj = self.model.get_by_id(_id=_id)
        return obj.update(data=data)

    def list(self) -> List[Any]:
        return self.model.list()

    def delete(self, _id: Any):
        obj = self.model.get_by_id(_id=_id)
        return obj.delete()

