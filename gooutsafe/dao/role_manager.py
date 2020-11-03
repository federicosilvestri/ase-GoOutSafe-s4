from gooutsafe.models.role import Role
from .manager import Manager

class RoleManager(Manager):

    @staticmethod
    def create_role(role: Role):
        Manager.create(role=role)

    @staticmethod
    def retrieve_by_id(id_):
        Manager.check_none(id=id_)
        return Role.query.get(id_)

    @staticmethod
    def retrieve_by_name(name):
        Manager.check_none(name=name)
        return Role.query.filter_by(name=name).first()

    @staticmethod
    def delete_role(role: Role):
        Manager.delete(role=role)

    @staticmethod
    def delete_role_by_id(id_):
        role = RoleManager.retrieve_by_id(id_)
        RoleManager.delete_role(role)

    @staticmethod
    def delete_role_by_name(name):
        role = RoleManager.retrieve_by_name(name=name)
        RoleManager.delete_role(role)