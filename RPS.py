import random

def player(prev_play, opponent_history=[]):
    # Save opponent history
    if prev_play != "":
        opponent_history.append(prev_play)

    # First few moves are random
    if len(opponent_history) < 5:
        return random.choice(["R", "P", "S"])

    # Function to beat a move
    def beat(move):
        return {"R": "P", "P": "S", "S": "R"}[move]

    # Counter opponent who copies your strategy
    if len(opponent_history) >= 2:
        if opponent_history[-1] == beat(opponent_history[-2]):
            return beat(beat(opponent_history[-1]))

    # Pattern detection (for repeating bots)
    last_three = opponent_history[-3:]
    pattern = {}

    for i in range(len(opponent_history) - 3):
        seq = tuple(opponent_history[i:i+3])
        next_move = opponent_history[i+3]
        if seq == tuple(last_three):
            pattern[next_move] = pattern.get(next_move, 0) + 1

    if pattern:
        predicted = max(pattern, key=pattern.get)
        return beat(predicted)

    # Frequency-based counter
    counts = {
        "R": opponent_history.count("R"),
        "P": opponent_history.count("P"),
        "S": opponent_history.count("S")
    }

    most_common = max(counts, key=counts.get)
    return beat(most_common)