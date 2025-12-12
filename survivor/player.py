from __future__ import annotations
from dataclasses import dataclass
from typing import TYPE_CHECKING

from survivor.traits import Traits

if TYPE_CHECKING:
    from survivor.strategies import Strategy

@dataclass
class Player:
    name: str
    traits: Traits
    strategy: "Strategy"
    alive: bool = True
