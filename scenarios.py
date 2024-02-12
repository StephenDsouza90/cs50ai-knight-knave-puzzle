from players import *

a_knight_or_knave = Or(AKnight, AKnave)
b_knight_or_knave = Or(BKnight, BKnave)
c_knight_or_knave = Or(CKnight, CKnave)

a_not_knight_and_knave = Not(And(AKnight, AKnave))
b_not_knight_and_knave = Not(And(BKnight, BKnave))
c_not_knight_and_knave = Not(And(CKnight, CKnave))

a_knight_and_knave = And(AKnight, AKnave)

a_and_b_knight = And(AKnight, BKnight)

a_and_b_knave = And(AKnave, BKnave)

a_and_b_not_knave = Not(And(AKnave, BKnave))

a_knight_and_b_knave = And(AKnight, BKnave)

a_knave_and_b_knight = And(AKnave, BKnight)

a_not_knave = Not(AKnave)

a_not_knight = Not(AKnight)

c_not_knave = Not(CKnave)