# Mark Wildman-based programming randomizer

Launch in Binder here:
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/brugaltheelder/wildmanprogramming/main)

You can use the get_workout and print_workout functions to generate a workout that
may be sorted by difficulty, bounded by difficulty/complexity, and have a time bound (within 1 minute).

Exercise Lists:

mace_exercises
club_exercises_1h
club_exercises_2h

order_by_level sorts the exercises in order of least complex to most complex
randomize_RL randomizes if L or R comes first in exercises that have a left and right version. If set to false, it defaults to left-first.
reverse_RL will set R to first for exercise that have L and R components

