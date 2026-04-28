from services.reqres_in.auth.login_user import LoginUser
from services.reqres_in.auth.register_user import RegisterUser
from services.reqres_in.resources.get_resource import GetResource
from services.reqres_in.resources.get_resources import GetResources
from services.reqres_in.users.create_user import CreateUser
from services.reqres_in.users.delete_user import DeleteUser
from services.reqres_in.users.get_user import GetUser
from services.reqres_in.users.update_user_patch import UpdateUserPatch
from services.reqres_in.users.update_user_put import UpdateUserPut


class Application:
    def __init__(self, env_config):

        self.login = LoginUser(env_config)
        self.register = RegisterUser(env_config)
        self.create = CreateUser(env_config)
        self.get = GetUser(env_config)
        self.get_resources = GetResources(env_config)
        self.get_resource = GetResource(env_config)
        self.update_put = UpdateUserPut(env_config)
        self.update_patch = UpdateUserPatch(env_config)
        self.delete = DeleteUser(env_config)


