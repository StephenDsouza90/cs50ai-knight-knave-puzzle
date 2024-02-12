from logic import *
from players import *
from scenarios import *
from implications import *
from statement import *

# Puzzle 0
# A says "I am both a knight and a knave."
# NOTE: Since A cannot be both then A has to be knave.
knowledge0 = And(
    a_knight_or_knave_but_not_both,  # statement
    if_a_knight_a_is_both,  # implication
    if_a_knave_a_is_not_both  # implication
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
# NOTE: Since both cannot be Knave and B is silent, A has to be Knave.
knowledge1 = And(
    a_knight_or_knave_but_not_both,  # statement
    b_knight_or_knave_but_not_both,  # statement
    if_a_knight_a_and_b_knave,  # implication
    if_knave_a_and_b_not_knave  # implication
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
# NOTE: Since both cannot be the same, A has be Knave that would make B the Knight.
knowledge2 = And(
    a_knight_or_knave_but_not_both,  # statement
    b_knight_or_knave_but_not_both,  # statement
    if_a_knight_a_and_b_are_same_kind,  # implication
    if_a_knave_a_and_b_are_not_same_kind,  # implication
    if_b_knight_a_and_b_are_different_kind,  # implication
    if_b_knave_a_and_b_are_not_different_kind  # implication
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
# NOTE: Since we do not know what A said, we rely on B and C.
knowledge3 = And(
    a_knight_or_knave_but_not_both,  # statement
    b_knight_or_knave_but_not_both,  # statement
    c_knight_or_knave_but_not_both,  # statement

    # B regarding A
    if_b_knight_a_says_knave,  # implication
    if_b_knave_a_says_knight,  # implication

    # B regarding C
    if_b_knight_c_knave,  # implication
    if_b_knave_c_not_knave,  # implication

    # C regarding A
    if_c_knight_a_knight,  # implication
    if_c_knave_a_not_knight  # implication
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
