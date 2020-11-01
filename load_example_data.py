from gooutsafe import create_app
import json
from werkzeug.security import generate_password_hash


PATH_HEALTH_AUTH_DATA = 'example_data/health_authority.json'


def load_example_data():
    create_app()
    from gooutsafe import db
    from gooutsafe.models import health_authority
    from gooutsafe.dao.health_authority_manager import AuthorityManager
    example_health_auth = load_health_auth_data(health_authority)
    AuthorityManager.create_authority(example_health_auth)

  
def load_health_auth_data(health_authority):
    dict_health_auth = {}
    with open(PATH_HEALTH_AUTH_DATA) as json_file:
        dict_health_auth = json.load(json_file)
    email = dict_health_auth["email"]
    password = generate_password_hash(dict_health_auth["password"])
    name = dict_health_auth["name"]
    city = dict_health_auth["city"]
    address = dict_health_auth["address"]
    phone = dict_health_auth["phone"]
    new_health_authority = health_authority.Authority(email=email, password=password, name=name,
                              city=city,
                              address=address, phone=phone
                              )
    return new_health_authority


if __name__ == "__main__":  
    load_example_data()
