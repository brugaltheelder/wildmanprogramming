# Mark Wildman-based programming randomizer

Launch in Binder here (be patient, may take a minute to load up):
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/brugaltheelder/wildmanprogramming/main)

[Mark Wildman Mace Tutorials](https://www.youtube.com/watch?v=2PRpaJERX3E&list=PLk4oYPJ7TXKh050XTrfVFjPtDSeqYCfsh)

[Mark Wildman Club Tutorials](https://www.youtube.com/watch?v=Exuf3a7RhYs&list=PLk4oYPJ7TXKgVZH0qykDznDeaAcFImRuS)

You can use the get_mace_workout, get_1h_club_workout, and get_2h_club_workout functions to generate a workout that
may be sorted by difficulty, bounded by difficulty/complexity, and have a time bound (within 1 minute). See notes for details.

I added URLs to the mace workouts, will do for the club ones eventually.

I've added Kettlebell breakout exercises (first ~100 videos from [Mark Wildman Kettlebell Tutorials](https://www.youtube.com/watch?v=RE6CSomDvl8&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=1)). The L and R variations just count as 1 time until (unlike mace/club), as it is assumed 
you'd do your own timing/reps for these. I'll be adding more options (single/double/1v2-handed) eventually. 


# Notes
time_limit is the number of movements/variations you plan on doing, each assumed to be 1 minute

only_isolation --> if true, only chooses L and R isloation exercises

only_alternating --> if true, only chooses alternating exercises

level_lower_bound and level_upper_bound are bounds on the complexity of movement

order_by_level sorts the exercises in order of least complex to most complex

randomize_RL randomizes if L or R comes first in exercises that have a left and right version. If set to false, it defaults to left-first.

reverse_RL will set R to first for exercise that have L and R components

print_urls will print links to Wildman's videos for each movement

# Future Work

* Cleaning up the code and writing up a more accurate description of what I'm actually doing
* Implement long movement pattern generator (may need some expert input)
* Combining movement pattern generation with long workout randomization (basically giving the ability to have multiple-move movement patterns and variable time limits for long-form workout generation)
* Adding in skill-work/movement pattern breakdown exercises (e.g., kneeling clean series, TGU breakdowns, etc) for warmup skillwork
* Adding in muscle group target areas for balancing workout load (or focusing on an area)
* Building in EMOM programming to make a fixed number of weeks programming at a time (having auto-incrementing so a large spreadsheet is generated)
* Adding in pickling so you can save your historical workouts
* Adding in overall programming generation, along with skill exclusions for KB ones you've already done recently

# Disclaimer

This was done independently from Wildman Athletica. 

