from enum import Enum

class Function(Enum):
    REGISTER_DEVICE = "REGISTER_DEVICE"
    REMOVE_DEVICE = "REMOVE_DEVICE"
    TURN_ON_OFF = "TURN_ON_OFF"

class Switch(Enum):
    ON = "ON"
    OFF = "OFF"

class Domain(Enum):
    GENERAL = "GENERAL"
    ELECTRICITY = "ELECTRICITY"
    LIGHTNING = "LIGHTNING"