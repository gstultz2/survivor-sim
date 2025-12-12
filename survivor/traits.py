from __future__ import annotations
from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Traits:
    aggression: float = 0.5
    loyalty: float = 0.5
    physicality: float = 0.5

def AverageTraits():
    return Traits(aggression=0.5, loyalty=0.5, physicality=0.5)

def PhysicalThreat():
     return Traits(aggression=0.5, loyalty=0.5, physicality=0.9)
