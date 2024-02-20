from rolepermissions.roles import AbstractUserRole

class Totver(AbstractUserRole):
    available_permissions = {
        'see_dashboard': True,
    }
    
class Canal(AbstractUserRole):
    available_permissions = {
        'edit_db': True,
    }
