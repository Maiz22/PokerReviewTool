from __future__ import annotations
import re
from typing import TYPE_CHECKING

#import for declaring parameters and return values
if TYPE_CHECKING:
    from action import BaseAction



class ActionRegistry:
    _registry = []

    
    @classmethod
    def register(cls) -> None:
        """
        Register decorator: Takes an action as paramerter.
        Registers (adds) it to the registry.
        """
        def wrapper(action_class:BaseAction):
            cls._registry.append(action_class)
        return wrapper

    @classmethod
    def get_action(cls, line:str) -> BaseAction|None:
        """
        Takes a line (str) and matches it to the pattern of any 
        class inside of the _registry. If a match could be found
        an instance of an action class is created and returned and 
        the match is passed to the constructor.
        """
        for action_class in cls._registry:
            match = re.search(pattern=action_class.pattern, string=line)
            if match:
                return action_class(match)
        return f"\n########## [Unknown Action] ########## {line}"