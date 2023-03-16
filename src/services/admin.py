import src.models.admin as models

class Admin:
    def turn_into_admin(self, id) -> str:
        return models.turn_indo_admin_by_id(id)