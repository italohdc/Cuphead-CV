from enum import Enum
from .handle_keypress import HandleKeypress

DISABLE_FAILSAFE_INTERVAL = True

class Action(str, Enum):
    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'
    SHOOT = 'x'
    JUMP = 'z'
    DASH = 'shift'

class HandleAction:
    @staticmethod
    def execute(action, interval = 0.1):
        HandleKeypress.press(action, interval)

    @staticmethod
    def hold(action):
        HandleKeypress.hold(action)

    @staticmethod
    def release(action):
        HandleKeypress.release(action)

    @staticmethod
    def release_all():
        HandleKeypress.release([a.value for a in Action])
