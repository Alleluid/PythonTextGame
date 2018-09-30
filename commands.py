"""
Commands for use in main textgame module.
"""
from __future__ import annotations

import format_templates as ft
import utility


class Command:
    """
    Base class to get list of input strings and perform actions.
    """
    def __init__(self, user_split_input: list, player=utility._debug_player):
        self.player = player
        self.user_input = user_split_input
        self.func_format = ft.FuncFormat(self.player)
        self._run()

    def _run(self):
        """
        Abstract method run after init.

        Used to perform actions based on user input.
        :return: None
        """
        raise NotImplementedError


class MoveCommand(Command):
    """
    Move player in a direction, and update.
    """
    def _run(self):
        directions = {
            ("north", "up", "forward"): "north",
            ("east", "right"): "east",
            ("south", "down", "backward"): "south",
            ("west", "left"): "west",
        }  # Standardizes directions to always be cardinal

        for keywords, value in directions.items():
            if self.user_input[1] in keywords:
                self.func_format.display('movement', direction=value)
                return
        print(ft.temps['invalid'])


class AttackCommand(Command):
    def _run(self):
        pass  # TODO: Implement entity target by name


class WaitCommand(Command):
    def _run(self):
        self.func_format.display('wait')


class LookCommand(Command):
    def _run(self):
        self.func_format.display('look')


class DebugCommand(Command):
    def _run(self):
        self.func_format.display('invalid')


class CMDInput:
    """
    Handle user input and call appropriate class.

    Has options for which command words are used to do the specified action.

    """
    cmds_dict = {
        ("move", "go", "step"): MoveCommand,
        ("attack", "hit"): AttackCommand,
        ("skip", "wait", "."): WaitCommand,
        ("look", "see", "inspect"): LookCommand,
        ("debug",): DebugCommand
    }

    @classmethod
    def get(cls, k, default=None):
        """Calls .get on internal `cmds_dict`.

        :param k: key
        :param default:
        :return: requested key, or default.
        """
        return cls.cmds_dict.get(k, default)

    def __init__(self, player, default_prompt="> "):
        self.prompt = default_prompt
        self.player = player

    def __call__(self):
        """
        Parses input from player.

        Parses and executes command based on first word of input.
        :return: None
        """
        self.text = input(self.prompt)
        self.input_cmds = self.text.split(' ')
        self._parse()

    def _parse(self):
        for keywords, command in self.cmds_dict.items():
            if self.input_cmds[0] in keywords:
                command(self.input_cmds, self.player)
                return
        print("Invalid input")


def _test():

    while True:
        cmd = CMDInput(utility._debug_player)
        cmd()


if __name__ == '__main__':
    _test()
