# pylint: disable=protected-access
from tests import utils
import models
from app.domain import entity, repository


# ==================================================================
# User repository test
# ==================================================================
def test_create_user(db) -> None:
    last_name = utils.random_lower_string()
    first_name = utils.random_lower_string()
    weak_password = "D3m0.Zebrans2022"
    email = f"{last_name}.{first_name}@test.com"
    user_in = entity.UserIn(last_name=last_name, first_name=first_name, email=email, password=weak_password)
    rep = repository.UserRepository()
    user = rep.create(obj_in=user_in)
    assert user.last_name == last_name
    assert user.first_name == first_name


def test_first_user(db) -> None:
    rep = repository.UserRepository()
    user = rep.first({"is_active": True})
    assert isinstance(user, models.User)


def test_get_user(db) -> None:
    rep = repository.UserRepository()
    user = rep.get_by_id(_id=1)
    assert isinstance(user, models.User)


def test_list_user(db) -> None:
    rep = repository.UserRepository()
    user = rep.list()
    assert isinstance(user, list)


def test_update_user(db) -> None:
    rep = repository.UserRepository()
    obj_db_ref = rep.list()[-1]
    obj_db = rep.get_by_id(_id=obj_db_ref.id)
    last_name = utils.random_lower_string()
    first_name = utils.random_lower_string()
    weak_password = "D3m0.Zebrans2022"
    email = f"{last_name}.{first_name}@test.com"
    user_in = entity.UserIn(id=obj_db_ref.id,
                            last_name=last_name,
                            first_name=first_name,
                            email=email,
                            password=weak_password)
    
    user = rep.update(_id=obj_db.id, obj_in=user_in)
    assert user.last_name == last_name
    assert user.first_name == first_name


def test_delete_user(db) -> None:
    rep = repository.UserRepository()
    obj_db_ref = rep.list()[-1]
    rep.delete(_id=obj_db_ref.id)
    obj_db_deleted = rep.get_by_id(_id=obj_db_ref.id)
    assert None == obj_db_deleted

