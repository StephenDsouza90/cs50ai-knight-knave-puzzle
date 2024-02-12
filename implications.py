from logic import *
from players import *
from scenarios import *

# Puzzle 0
if_a_knight_a_is_both = Implication(AKnight, a_knight_and_knave)
if_a_knave_a_is_not_both = Implication(AKnave, a_not_knight_and_knave)

# Puzzle 1
if_a_knight_a_and_b_knave = Implication(AKnight, a_and_b_knave)
if_knave_a_and_b_not_knave = Implication(AKnave, a_and_b_not_knave)

# Puzzle 2
if_a_knight_a_and_b_are_same_kind = Implication(AKnight, Or(a_and_b_knight, a_and_b_knave))
if_a_knave_a_and_b_are_not_same_kind = Implication(AKnave, Not(Or(a_and_b_knight, a_and_b_knave)))
if_b_knight_a_and_b_are_different_kind = Implication(BKnight, Or(a_knight_and_b_knave, a_knave_and_b_knight))
if_b_knave_a_and_b_are_not_different_kind = Implication(BKnave, Not(Or(a_knight_and_b_knave, a_knave_and_b_knight)))

# Puzzle 3
if_b_knight_c_knave = Implication(BKnight, CKnave)
if_b_knave_c_not_knave = Implication(BKnave, c_not_knave)

if_c_knight_a_knight = Implication(CKnight, AKnight)
if_c_knave_a_not_knight = Implication(CKnave, a_not_knight)

# Assuming B is Knight (And says A said A is a Knave): but actually A says "I am a Knave"?
if_a_knight_a_not_knave = Implication(AKnight, a_not_knave)
if_a_knave_a_not_knave = Implication(AKnave, a_not_knave)
if_b_knight_a_says_knave = Implication(BKnight, And(if_a_knight_a_not_knave, if_a_knave_a_not_knave))

# Assuming B is Knave (And says A said A is Knave): but actually A says "I am a Knight"
if_a_knight_a_knight = Implication(AKnight, AKnight)
if_a_knave_a_not_knight = Implication(AKnave, a_not_knight)
if_b_knave_a_says_knight = Implication(BKnave, And(if_a_knight_a_knight, if_a_knave_a_not_knight))
