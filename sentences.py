from scenarios import *

a_knight_or_knave_but_not_both = And(a_knight_or_knave, a_not_knight_and_knave)
b_knight_or_knave_but_not_both = And(b_knight_or_knave, b_not_knight_and_knave)
c_knight_or_knave_but_not_both = And(c_knight_or_knave, c_not_knight_and_knave)
