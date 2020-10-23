# Mark Wildman-based programming randomizer

Launch in Binder here:
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/brugaltheelder/wildmanprogramming/main)

[Mark Wildman Mace Tutorials](https://www.youtube.com/watch?v=2PRpaJERX3E&list=PLk4oYPJ7TXKh050XTrfVFjPtDSeqYCfsh)

[Mark Wildman Club Tutorials](https://www.youtube.com/watch?v=Exuf3a7RhYs&list=PLk4oYPJ7TXKgVZH0qykDznDeaAcFImRuS)

You can use the get_mace_workout, get_1h_club_workout, and get_2h_club_workout functions to generate a workout that
may be sorted by difficulty, bounded by difficulty/complexity, and have a time bound (within 1 minute). See notes for details.

I added URLs to the mace workouts, will do for the club ones eventually


# Notes
time_limit is the number of movements/variations you plan on doing, each assumed to be 1 minute

only_isolation --> if true, only chooses L and R isloation exercises

only_alternating --> if true, only chooses alternating exercises

level_lower_bound and level_upper_bound are bounds on the complexity of movement

order_by_level sorts the exercises in order of least complex to most complex

randomize_RL randomizes if L or R comes first in exercises that have a left and right version. If set to false, it defaults to left-first.

reverse_RL will set R to first for exercise that have L and R components

print_urls will print links to Wildman's videos for each movement

# Disclaimer

This was done independently from Wildman Athletica. 

