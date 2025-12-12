from __future__ import annotations
from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Vote:
    voter: str
    target: str

@dataclass
class RoundResult:
    round_no: int
    immunity_winner: str
    votes: List[Vote]
    eliminated: str
