from survivor.engine import SurvivorGame
from survivor.player import Player
from survivor.strategies import RandomVoteStrategy
from survivor.traits import Traits

if __name__ == "__main__":
    strat = RandomVoteStrategy()
    players = [
        Player("Ava", Traits(), strat),
        Player("Ben", Traits(), strat),
        Player("Cy", Traits(), strat),
        Player("Dee", Traits(), strat),
        Player("Eli", Traits(), strat),
    ]

    game = SurvivorGame(players, seed=42)

    while len(game.alive_players()) > 1:
        rr = game.run_round()
        print(f"Round {rr.round_no}")
        print(f"{rr.immunity_winner} has immunity")
        print(f"Votes:")
        for v in rr.votes:
            print(f"  {v.voter} → {v.target}")
        print(f"Eliminated: {rr.eliminated}\n")

    print("Winner:", game.alive_players()[0].name)