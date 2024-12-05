class Role:
    ADMIN = "admin"
    CHUTRO = "chutro"
    NGUOITHUETRO = "nguoithuetro"

    def __init__(self, role_name):
        if role_name not in [self.ADMIN, self.CHUTRO, self.NGUOITHUETRO]:
            raise ValueError(f"Invalid role: {role_name}")
        self.role_name = role_name

    def is_admin(self):
        return self.role_name == self.ADMIN

    def is_chutro(self):
        return self.role_name == self.CHUTRO

    def is_nguoithuetro(self):
        return self.role_name == self.NGUOITHUETRO

    @staticmethod
    def get_all_role():
        return [Role.ADMIN,Role.CHUTRO,Role.NGUOITHUETRO]

