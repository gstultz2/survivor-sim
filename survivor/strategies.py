from __future__ import annotations
from typing import Protocol, List
import random

from survivor.traits import Traits
from survivor.player import Player

class Strategy(Protocol):
    def vote(self, *, me: Player, players: List[Player], rng: random.Random) -> str: ...

class RandomVoteStrategy:
    def vote(self, *, me: Player, players: List[Player], rng: random.Random) -> str:
        options = [p.name for p in players if p.alive and p.name != me.name]
        return rng.choice(options)

class VoteBigThreat:
    def vote(self, *, me: Player, players: List[Player], rng: random.Random) -> str:
        return max(players, key=lambda x: x.traits.physicality)