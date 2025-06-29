#some vibecoded bot to check some values
import time
from unittest.mock import patch
from games_and_tools import blackjack, googol


def run_simulation(rounds=100):
    """Run blackjack simulation for a given number of rounds and report stats"""
    wins = losses = ties = 0
    total_change = 0
    for i in range(1, rounds + 1):
        # set fixed bet
        blackjack.bet = 10
        # record money before
        money_before = int(googol.display_money_value())

        # bot input logic
        def smart_input(prompt=""):
            prompt_lower = prompt.lower()
            # hit/stand decision
            if "hit" in prompt_lower and "stand" in prompt_lower:
                # get current scores
                player_score = blackjack.count_best_hand("player_1")
                upcard = blackjack.extract_card_value(blackjack.hand_dealer[0])
                # convert dealer upcard to numeric value
                if upcard == "A":
                    dealer_value = 11
                elif upcard in ("K", "Q", "J"):
                    dealer_value = 10
                else:
                    dealer_value = int(upcard)
                # basic strategy
                if player_score <= 11:
                    return 'h'
                elif player_score == 12:
                    return 'h' if dealer_value >= 7 else 's'
                elif player_score <= 16:
                    return 'h' if dealer_value >= 7 else 's'
                else:
                    return 's'
            # default Enter for all other prompts
            return ""

        # run one round with patched input and no sleep delays
        with patch('builtins.input', smart_input), patch('time.sleep', lambda x: None):
            blackjack.main_blackjack_classic()

        # record money after
        money_after = int(googol.display_money_value())
        change = money_after - money_before
        total_change += change
        if change > 0:
            wins += 1
        elif change < 0:
            losses += 1
        else:
            ties += 1
    
    # calculate expected value
    expected_value = total_change / rounds
    
    # print summary
    print(f"Simulation complete: {rounds} rounds")
    print(f"Wins: {wins}")
    print(f"Losses: {losses}")
    print(f"Ties: {ties}")
    print(f"Erwartungswert: {expected_value:.4f}")
    print(f"Total Money Change: {total_change}")


if __name__ == "__main__":
    run_simulation(50000)