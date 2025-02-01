from enum import Enum

class RoleType(str, Enum):
    PARTICIPANT = "participant"
    MEMBER = "member"
    ADMIN = "admin"