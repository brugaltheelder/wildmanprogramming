import numpy as np


class exercise(object):
    def __init__(self, name, type_list, level = 1):
        self.name = name
        self.type_list = type_list
        self.count = len(type_list)
        self.level = level
    def get_exercises(self, reverse_RL=False):
        return_set = [t+" - "+self.name for t in self.type_list]
        if reverse_RL:
            return_set = return_set[::-1]
        return return_set

def get_workout(exercise_list, desired_time_bound, level_lower_bound = 0, level_upper_bound = 10):
    total_time = 0
    output_exercises = []
    shuffled_indices = np.arange(len(exercise_list))
    np.random.shuffle(shuffled_indices)
    time_bound = min(sum([e.count for e in exercise_list]), desired_time_bound)
    for s in shuffled_indices:
        if exercise_list[s].level<=level_upper_bound and exercise_list[s].level>=level_lower_bound:
            output_exercises.append(exercise_list[s])
            total_time+=exercise_list[s].count
            if total_time>=time_bound:
                return output_exercises
    return output_exercises
        
def print_workout(exercise_str_list, order_by_level=False, randomize_RL=False, reverse_RL=False):
    if order_by_level:
        exercise_str_list.sort(key=lambda x: x.level)    
    rev = reverse_RL
    if randomize_RL:
        rev = True if np.random.rand()>0.5 else False
    for s in exercise_str_list:        
        for e in s.get_exercises(rev):
            print('level:{}'.format(s.level) +'\t' + e )

mace_exercises = []
mace_exercises.append(exercise('360',['L','R'], level=1))
mace_exercises.append(exercise('gamma cast',['L','R'], level=1))
mace_exercises.append(exercise('prayer transition',['alternating'], level=1))
mace_exercises.append(exercise('prayer transition to 360',['alternating'], level=2))
mace_exercises.append(exercise('90 degree pivot uppercut',['L','R'], level=2))
mace_exercises.append(exercise('90 degree pivot uppercut to 360 barbell transition',['alternating'], level=3))
mace_exercises.append(exercise('inverted side-to-side swings',['L','R'], level=2))
mace_exercises.append(exercise('horizontal prayer transition to target squat',['L','R'], level=2))
mace_exercises.append(exercise('horizontal prayer transition to squat',['L','R'], level=2))
mace_exercises.append(exercise('barbell transition to squat',['L','R'], level=2))
mace_exercises.append(exercise('barbell transition to target squat',['L','R'], level=2))
mace_exercises.append(exercise('horizontal prayer transition to squat to 360',['alternating'], level=3))
mace_exercises.append(exercise('barbell transition to squat to 360',['alternating'], level=3))
mace_exercises.append(exercise('single arm inside circle',['L','R'], level=2))
mace_exercises.append(exercise('single arm outside circle',['L','R'], level=2))
mace_exercises.append(exercise('single arm alternating circles',['L','R'], level=2))
mace_exercises.append(exercise('single arm inside circle to alternate hand coin flip',['L','R'], level=4))
mace_exercises.append(exercise('single arm outside circle to alternate hand coin flip',['L','R'], level=4))
mace_exercises.append(exercise('single arm alternating circle to alternate hand coin flip',['L','R'], level=5))
mace_exercises.append(exercise('single arm inside circle to same hand coin flip catch',['L','R'], level=5))
mace_exercises.append(exercise('single arm outside circle to same hand coin flip catch',['L','R'], level=5))
mace_exercises.append(exercise('single arm alternating circle to same hand coin flip catch',['L','R'], level=6))
mace_exercises.append(exercise('single arm inside same hand coin flip catch',['L','R'], level=4))
mace_exercises.append(exercise('single arm outside same hand coin flip catch',['L','R'], level=4))
mace_exercises.append(exercise('single arm inside continuous circle with alternate hand nunchuck flip',['L','R'], level=4))
mace_exercises.append(exercise('single arm outside continuous circle with alternate hand flip aerial catch',['L','R'], level=5))
mace_exercises.append(exercise('single arm outside continuous circle with alternate hand flip touching catch',['L','R'], level=4))
mace_exercises.append(exercise('single arm inside mill with same side flip catch',['L','R'], level=5))
mace_exercises.append(exercise('single arm outside mill with same side flip catch',['L','R'], level=5))
mace_exercises.append(exercise('single arm inside mill with alt side flip catch (nunchuck flip to change back)',['L','R'], level=5))
mace_exercises.append(exercise('single arm outside mill with alt side flip catch',['L','R'], level=5))



club_exercises_2h = []
club_exercises_2h.append(exercise('inside circles', ['L','R'], level=1))
club_exercises_2h.append(exercise('outside circles', ['L','R'], level=1))
club_exercises_2h.append(exercise('pullover', ['L','R'], level=1))
club_exercises_2h.append(exercise('alternating pullover', ['L','R'], level=1))
club_exercises_2h.append(exercise('inside mill', ['L','R'], level=2))
club_exercises_2h.append(exercise('outside mill', ['L','R'], level=2))
club_exercises_2h.append(exercise('alternating mill circle transition', ['L','R'], level=3))
club_exercises_2h.append(exercise('alternating mill pendulum transition', ['L','R'], level=3))
club_exercises_2h.append(exercise('alternating mill pullover transition', ['L','R'], level=3))


club_exercises_1h = []
club_exercises_1h.append(exercise('inside circles', ['L','R'], level=1))
club_exercises_1h.append(exercise('outside circles', ['L','R'], level=1))
club_exercises_1h.append(exercise('pullover', ['L','R'], level=1))
club_exercises_1h.append(exercise('alternating pullover', ['L','R'], level=1))
club_exercises_1h.append(exercise('inside mill', ['L','R'], level=2))
club_exercises_1h.append(exercise('outside mill', ['L','R'], level=2))
club_exercises_1h.append(exercise('inside mill circle transition', ['alternating'], level=3))
club_exercises_1h.append(exercise('outside mill circle transition', ['alternating'], level=3))
club_exercises_1h.append(exercise('inside mill swing transition', ['alternating'], level=3))
club_exercises_1h.append(exercise('outside mill swing transition', ['alternating'], level=3))
club_exercises_1h.append(exercise('pendulum alternating mill', ['L','R'], level=3))
club_exercises_1h.append(exercise('swipe', ['L','R'], level=2))
club_exercises_1h.append(exercise('swipe', ['alternating'], level=3))
club_exercises_1h.append(exercise('outside swing', ['L','R'], level=1))
club_exercises_1h.append(exercise('outside swing', ['alternating'], level=2))