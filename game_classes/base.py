from enum import Enum, auto
import random


class Consts:
    class Enemies(Enum):
        LOW_LVL = auto
        MID_LVL = auto
        HIGH_LVL = auto


class GameObject:
    def __init__(self, value):
        self.value = value


class GameItem(GameObject):
    def __init__(self, value):
        super().__init__(value)


class GameStructure(GameObject):
    def __init__(self, value=1, max_struct_health=1000):
        # Structure max health starts at 1000, 10x that of standard actors.
        super().__init__(value)
        self.max_struct_health = max_struct_health
        self.struct_health = max_struct_health

        # By default, buildings are worth their health * 10
        if value == 1:
            self.value = max_struct_health * 10


class GameActor(GameObject):
    def __init__(self, value, max_health=100):
        super().__init__(value)
        self.max_health = max_health
        self.health = max_health


class GameActorNPC(GameActor):
    @classmethod
    def from_enum(cls, enum: Consts.Enemies):
        return {
            Consts.Enemies.LOW_LVL: cls(value=5, max_health=random.randint(1, 35)),
            Consts.Enemies.MID_LVL: cls(value=20, max_health=random.randint(35, 65)),
            Consts.Enemies.HIGH_LVL: cls(value=50, max_health=random.randint(65, 100))
        }.get(enum)
