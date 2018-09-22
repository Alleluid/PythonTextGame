from __future__ import annotations

import random
from enum import Enum, auto

from game_classes.base import GameObject, GameActor, GameActorNPC, GameItem, GameStructure, Consts
import utility

from locations import Loc, Locations
import format_templates as ft
import typing


class GameTurn:
    class Enum(Enum):
        MOVE = auto

    def __init__(self):
        self.command = input("> ")


class Player(GameActor):
    def __init__(self):
        super().__init__(value=0, max_health=100)
        self.name = input("Name> ")
        self.turns = []


class GameSession:
    def __init__(self):
        self.turns = []  # type:typing.List[GameTurn]
        self.player = Player()


def game_main():
    locations = Locations()
    session = GameSession()
    ff = ft.FuncFormat()

    ft.func_format_print(ff, 'welcome',
        player=session.player,
        rand_name=utility.get_rand_name,
        rand_location=locations.rand_str
    )

    beast = GameActorNPC.from_enum(Consts.Enemies.MID_LVL)

    ft.func_format_print(ff, 'encounter',
        player=session.player,
        rand_name=utility.get_rand_name,
    )


if __name__ == "__main__":
    game_main()
