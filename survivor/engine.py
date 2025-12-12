from __future__ import annotations
from typing import List, Dict
import random

from survivor.player import Player
from survivor.types import Vote, RoundResult

class SurvivorGame:
    def __init__(self, players: List[Player], seed: int = 0):
        self.players = players
        self.rng = random.Random(seed)
        self.round_no = 0

    def alive_players(self) -> List[Player]:
        return [p for p in self.players if p.alive]

    def run_round(self) -> RoundResult:
        self.round_no += 1
        alive = self.alive_players()

        votes: List[Vote] = []
        tally: Dict[str, int] = {p.name: 0 for p in alive}

        immune = self.immunity_challenge(alive) if len(alive) > 2 else None
        immune_name = immune.name if immune is not None else "Nobody"
        players_at_risk = [p for p in alive if p is not immune]

        for voter in alive:
            target = voter.strategy.vote(me=voter, players=players_at_risk, rng=self.rng)
            votes.append(Vote(voter=voter.name, target=target))
            tally[target] += 1

        max_votes = max(tally.values())
        top = [name for name, c in tally.items() if c == max_votes]
        eliminated_name = self.rng.choice(top)

        for p in self.players:
            if p.name == eliminated_name:
                p.alive = False
                break

        return RoundResult(round_no=self.round_no, immunity_winner=immune_name, votes=votes, eliminated=eliminated_name)

    def immunity_challenge(self, players: List[Player]) -> Player:
        return self.rng.choices(players, weights=[p.traits.physicality for p in players], k=1)[0]
