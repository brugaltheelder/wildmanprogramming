import numpy as np
from math import floor

class exercise(object):
    def __init__(self, name, type_list, level = 1, url = ''):
        self.name = name
        self.type_list = type_list
        self.count = len(type_list)
        self.level = level
        self.url = url
    def get_exercises(self, reverse_RL=False):
        return_set = [t+" - "+self.name for t in self.type_list]
        if reverse_RL:
            return_set = return_set[::-1]
        return return_set

    
    
    
def get_mace_workout(time_limit, level_lower_bound = 0, level_upper_bound = 10, 
                only_isolation=False, only_alternating=False, order_by_level=True, 
                     randomize_RL = True, reverse_RL=False, print_urls=True):

    print("generating mace workout")    
    mace = get_workout(mace_exercises,time_limit, level_lower_bound=level_lower_bound, level_upper_bound=level_upper_bound,
                      only_isolation=only_isolation, only_alternating=only_alternating)
    print_workout(mace,order_by_level=order_by_level, randomize_RL = randomize_RL, reverse_RL=reverse_RL, print_urls=print_urls)
    round_time = 1 # time in minutes
    print('total time:{}'.format(round_time* sum([e.count for e in mace])))
    

def get_1h_club_workout(time_limit, level_lower_bound = 0, level_upper_bound = 10, 
                only_isolation=False, only_alternating=False, order_by_level=True, 
                     randomize_RL = True, reverse_RL=False, print_urls=True):

    print("generating 1h club workout")    
    mace = get_workout(club_exercises_1h,time_limit, level_lower_bound=level_lower_bound, level_upper_bound=level_upper_bound,
                      only_isolation=only_isolation, only_alternating=only_alternating)
    print_workout(mace,order_by_level=order_by_level, randomize_RL = randomize_RL, reverse_RL=reverse_RL, print_urls=print_urls)
    round_time = 1 # time in minutes
    print('total time:{}'.format(round_time* sum([e.count for e in mace])))
    
def get_kb_exercises(num_exercises, level_lower_bound = 0, level_upper_bound = 10,only_single_bell=False, reverse_RL=False, randomize_RL=True, print_urls=True, order_by_level=True):
    print("generating 2h club workout")    
    kb = get_workout(kettlebell_movements,num_exercises, level_lower_bound=level_lower_bound, level_upper_bound=level_upper_bound, count_all_as_one=True)
    print_workout(kb,order_by_level=order_by_level, randomize_RL = randomize_RL, reverse_RL=reverse_RL, print_urls=print_urls)
    round_time = 1 # time in minutes
    print('total movementst:{}'.format(round_time* sum([e.count for e in kb])))

def get_2h_club_workout(time_limit, level_lower_bound = 0, level_upper_bound = 10, 
                only_isolation=False, only_alternating=False, order_by_level=True, 
                     randomize_RL = True, reverse_RL=False, print_urls=True):

    print("generating 2h club workout")    
    mace = get_workout(club_exercises_2h,time_limit, level_lower_bound=level_lower_bound, level_upper_bound=level_upper_bound,
                      only_isolation=only_isolation, only_alternating=only_alternating)
    print_workout(mace,order_by_level=order_by_level, randomize_RL = randomize_RL, reverse_RL=reverse_RL, print_urls=print_urls)
    round_time = 1 # time in minutes
    print('total time:{}'.format(round_time* sum([e.count for e in mace])))
    
def get_workout(exercise_list, desired_time_bound, level_lower_bound = 0, level_upper_bound = 10, 
                only_isolation=False, only_alternating=False, count_all_as_one=False):
    total_time = 0
    output_exercises = []
    shuffled_indices = np.arange(len(exercise_list))
    np.random.shuffle(shuffled_indices)
    time_bound = min(sum([e.count for e in exercise_list]), desired_time_bound)
    for s in shuffled_indices:
        if exercise_list[s].level<=level_upper_bound and exercise_list[s].level>=level_lower_bound:
            if only_isolation:
                if exercise_list[s].count==1:
                    continue
            if only_alternating and not only_isolation:
                if exercise_list[s].count==2:
                    continue
            output_exercises.append(exercise_list[s])
            if count_all_as_one:
                total_time+=1
            else:
                total_time+=exercise_list[s].count
            if total_time>=time_bound:
                return output_exercises
    return output_exercises
        
def print_workout(exercise_str_list, order_by_level=False, 
                  randomize_RL=False, reverse_RL=False, print_urls=False):
    if order_by_level:
        exercise_str_list.sort(key=lambda x: x.level)    
    rev = reverse_RL
    if randomize_RL:
        rev = True if np.random.rand()>0.5 else False
    for s in exercise_str_list:        
        for e in s.get_exercises(rev):
            print('level:{}'.format(s.level) +'\t' + e )
        if print_urls:
            print('\turl: {}'.format(s.url))
    print('-'*10)
    print('without URLs:')
    if print_urls:
        for s in exercise_str_list:        
            for e in s.get_exercises(rev):
                print('level:{}'.format(s.level) +'\t' + e )




def generate_sandbag_table(weight, percent_sand_weight, time_limit_minutes=10, starting_time_minuites = 3,initial_gap_seconds = 10, final_gap_seconds=6):
    print('Sandbag rountine for {} lb person at {} percent sand weight of {:.1f} lbs'.format(weight, percent_sand_weight, weight*percent_sand_weight))
    print('Total Min\tDelay(s)\tReps')
    for i in range(starting_time_minuites,time_limit_minutes):
        print('{}\t\t{}\t\t{:.0f}'.format(i,initial_gap_seconds,floor(i*60/initial_gap_seconds)))
    for i in range(initial_gap_seconds-1,final_gap_seconds-1,-1):
        print('{}\t\t{}\t\t{:.0f}'.format(time_limit_minutes,i,floor(time_limit_minutes*60/i)))


mace_exercises = []
mace_exercises.append(exercise('360',['L','R'], level=1, url='https://youtu.be/TyZ8iYv6Ip0?list=PLk4oYPJ7TXKh050XTrfVFjPtDSeqYCfsh'))
mace_exercises.append(exercise('gamma cast',['L','R'], level=1, url='https://www.youtube.com/watch?v=ccifkBh2JSI&list=PLk4oYPJ7TXKh050XTrfVFjPtDSeqYCfsh&index=3'))
mace_exercises.append(exercise('prayer transition',['alternating'], level=1, url='https://www.youtube.com/watch?v=0fjn0vidH2M&list=PLk4oYPJ7TXKh050XTrfVFjPtDSeqYCfsh&index=5'))
mace_exercises.append(exercise('prayer transition to 360',['alternating'], level=2, url='https://www.youtube.com/watch?v=0fjn0vidH2M&list=PLk4oYPJ7TXKh050XTrfVFjPtDSeqYCfsh&index=5'))
mace_exercises.append(exercise('barbell transition',['alternating'], level=1, url='https://www.youtube.com/watch?v=WQjHBHoC-MQ&list=PLk4oYPJ7TXKh050XTrfVFjPtDSeqYCfsh&index=4'))
mace_exercises.append(exercise('barbell transition to 360',['alternating'], level=2, url='https://www.youtube.com/watch?v=WQjHBHoC-MQ&list=PLk4oYPJ7TXKh050XTrfVFjPtDSeqYCfsh&index=4'))
mace_exercises.append(exercise('90 degree pivot uppercut',['L','R'], level=2, url='https://www.youtube.com/watch?v=ULFal2-zDt0&list=PLk4oYPJ7TXKh050XTrfVFjPtDSeqYCfsh&index=7'))
mace_exercises.append(exercise('90 degree pivot uppercut to 360 barbell transition',['alternating'], level=3, url='https://www.youtube.com/watch?v=ULFal2-zDt0&list=PLk4oYPJ7TXKh050XTrfVFjPtDSeqYCfsh&index=7'))
mace_exercises.append(exercise('inverted side-to-side swings',['L','R'], level=2, url='https://www.youtube.com/watch?v=bLA2KSghSdc&list=PLk4oYPJ7TXKh050XTrfVFjPtDSeqYCfsh&index=8'))
mace_exercises.append(exercise('horizontal prayer transition to target squat',['L','R'], level=2, url='https://www.youtube.com/watch?v=2yUz84zdBlk&list=PLk4oYPJ7TXKh050XTrfVFjPtDSeqYCfsh&index=13'))
mace_exercises.append(exercise('horizontal prayer transition to squat',['L','R'], level=2, url='https://www.youtube.com/watch?v=2yUz84zdBlk&list=PLk4oYPJ7TXKh050XTrfVFjPtDSeqYCfsh&index=13'))
mace_exercises.append(exercise('barbell transition to squat',['L','R'], level=2, url='https://www.youtube.com/watch?v=kZK8Eq6ka0U&list=PLk4oYPJ7TXKh050XTrfVFjPtDSeqYCfsh&index=14'))
mace_exercises.append(exercise('barbell transition to target squat',['L','R'], level=2, url='https://www.youtube.com/watch?v=kZK8Eq6ka0U&list=PLk4oYPJ7TXKh050XTrfVFjPtDSeqYCfsh&index=14'))
mace_exercises.append(exercise('horizontal prayer transition to squat to 360',['alternating'], level=3, url='https://www.youtube.com/watch?v=2yUz84zdBlk&list=PLk4oYPJ7TXKh050XTrfVFjPtDSeqYCfsh&index=13'))
mace_exercises.append(exercise('barbell transition to squat to 360',['alternating'], level=3, url='https://www.youtube.com/watch?v=kZK8Eq6ka0U&list=PLk4oYPJ7TXKh050XTrfVFjPtDSeqYCfsh&index=14'))
mace_exercises.append(exercise('low block spin with prayer transition', ['L','R'], level=1, url='https://www.youtube.com/watch?v=fk8AG0s1-UI&list=PLk4oYPJ7TXKh050XTrfVFjPtDSeqYCfsh&index=9'))
mace_exercises.append(exercise('low block spin with prayer transition', ['alternating'], level=2, url='https://www.youtube.com/watch?v=fk8AG0s1-UI&list=PLk4oYPJ7TXKh050XTrfVFjPtDSeqYCfsh&index=9'))
mace_exercises.append(exercise('low block spin with prayer transition to 360', ['alternating'], level=3, url='https://www.youtube.com/watch?v=GXMSVSDtJVc&list=PLk4oYPJ7TXKh050XTrfVFjPtDSeqYCfsh&index=10'))
mace_exercises.append(exercise('simple martial spin',['L','R'], level=2, url='https://www.youtube.com/watch?v=p_VgqCIGb-E&list=PLk4oYPJ7TXKh050XTrfVFjPtDSeqYCfsh&index=11'))
mace_exercises.append(exercise('simple martial spin with prayer transition',['alternating'], level=3, url='https://www.youtube.com/watch?v=p_VgqCIGb-E&list=PLk4oYPJ7TXKh050XTrfVFjPtDSeqYCfsh&index=11'))
mace_exercises.append(exercise('paddle row to upper block',['L','R'], level=2, url='https://www.youtube.com/watch?v=4or7Sb8HyaU&list=PLk4oYPJ7TXKh050XTrfVFjPtDSeqYCfsh&index=12'))
mace_exercises.append(exercise('paddle row to upper block with barbell transition',['alternating'], level=2, url='https://www.youtube.com/watch?v=4or7Sb8HyaU&list=PLk4oYPJ7TXKh050XTrfVFjPtDSeqYCfsh&index=12'))
mace_exercises.append(exercise('paddle row to upper block with barbell transition to 360',['alternating'], level=3, url='https://www.youtube.com/watch?v=4or7Sb8HyaU&list=PLk4oYPJ7TXKh050XTrfVFjPtDSeqYCfsh&index=12'))
mace_exercises.append(exercise('single arm inside circle',['L','R'], level=2, url='https://www.youtube.com/watch?v=MSt1cYAiLzI&list=PLk4oYPJ7TXKh050XTrfVFjPtDSeqYCfsh&index=16'))
mace_exercises.append(exercise('single arm outside circle',['L','R'], level=2, url='https://www.youtube.com/watch?v=ZuaKcM41dP4&list=PLk4oYPJ7TXKh050XTrfVFjPtDSeqYCfsh&index=17'))
mace_exercises.append(exercise('single arm alternating circles',['L','R'], level=2, url='https://www.youtube.com/watch?v=XWIFyifqSr8&list=PLk4oYPJ7TXKh050XTrfVFjPtDSeqYCfsh&index=18'))
mace_exercises.append(exercise('single arm inside circle to alternate hand coin flip',['L','R'], level=4, url='https://www.youtube.com/watch?v=opgqoNcD1Ds&list=PLk4oYPJ7TXKh050XTrfVFjPtDSeqYCfsh&index=19'))
mace_exercises.append(exercise('single arm outside circle to alternate hand coin flip',['L','R'], level=4, url='https://www.youtube.com/watch?v=qX0nE-3VMN0&list=PLk4oYPJ7TXKh050XTrfVFjPtDSeqYCfsh&index=20'))
mace_exercises.append(exercise('single arm alternating circle to alternate hand coin flip',['L','R'], level=5, url='https://www.youtube.com/watch?v=as46Zm9oibE&list=PLk4oYPJ7TXKh050XTrfVFjPtDSeqYCfsh&index=21'))
mace_exercises.append(exercise('single arm inside circle to same hand coin flip catch',['L','R'], level=5, url='https://www.youtube.com/watch?v=xlClTZRbmc0&list=PLk4oYPJ7TXKh050XTrfVFjPtDSeqYCfsh&index=22'))
mace_exercises.append(exercise('single arm outside circle to same hand coin flip catch',['L','R'], level=5, url='https://www.youtube.com/watch?v=UwR4uFqvUyY&list=PLk4oYPJ7TXKh050XTrfVFjPtDSeqYCfsh&index=23'))
mace_exercises.append(exercise('single arm alternating circle to same hand coin flip catch',['L','R'], level=6, url='https://www.youtube.com/watch?v=T5x3xsfHqs8&list=PLk4oYPJ7TXKh050XTrfVFjPtDSeqYCfsh&index=24'))
mace_exercises.append(exercise('single arm inside continuous circle with alternate hand nunchuck flip',['L','R'], level=4, url='https://www.youtube.com/watch?v=rCgrNJLsrBM&list=PLk4oYPJ7TXKh050XTrfVFjPtDSeqYCfsh&index=25'))
mace_exercises.append(exercise('single arm outside continuous circle with alternate hand flip aerial catch',['L','R'], level=5, url='https://www.youtube.com/watch?v=T5lfsHi1rDY&list=PLk4oYPJ7TXKh050XTrfVFjPtDSeqYCfsh&index=26'))
mace_exercises.append(exercise('single arm outside continuous circle with alternate hand flip touching catch',['L','R'], level=4, url='https://www.youtube.com/watch?v=T5lfsHi1rDY&list=PLk4oYPJ7TXKh050XTrfVFjPtDSeqYCfsh&index=26'))
mace_exercises.append(exercise('single arm inside mill with same side flip catch',['L','R'], level=5, url='https://www.youtube.com/watch?v=uFsPwnClx-M&list=PLk4oYPJ7TXKh050XTrfVFjPtDSeqYCfsh&index=27'))
mace_exercises.append(exercise('single arm outside mill with same side flip catch',['L','R'], level=5, url='https://www.youtube.com/watch?v=jKbelC2dZVo&list=PLk4oYPJ7TXKh050XTrfVFjPtDSeqYCfsh&index=28'))
mace_exercises.append(exercise('single arm inside mill with alt side flip catch (nunchuck flip to change back)',['L','R'], level=5, url='https://www.youtube.com/watch?v=Hmk80iWQHjM&list=PLk4oYPJ7TXKh050XTrfVFjPtDSeqYCfsh&index=29'))
mace_exercises.append(exercise('single arm outside mill with alt side flip catch',['L','R'], level=5, url='https://www.youtube.com/watch?v=aIxKwvzj9Hk&list=PLk4oYPJ7TXKh050XTrfVFjPtDSeqYCfsh&index=30'))
mace_exercises.append(exercise('symmetrical stance front circles',['L','R'], level=3, url='https://www.youtube.com/watch?v=ULozVN0nz_U&list=PLk4oYPJ7TXKh050XTrfVFjPtDSeqYCfsh&index=31'))
mace_exercises.append(exercise('symmetrical stance alternating circles',['L','R'], level=4, url='https://www.youtube.com/watch?v=MsrcRGT0YzA&list=PLk4oYPJ7TXKh050XTrfVFjPtDSeqYCfsh&index=35'))
mace_exercises.append(exercise('symmetrical stance backward circles',['L','R'], level=3, url='https://www.youtube.com/watch?v=KSja97kaEHY&list=PLk4oYPJ7TXKh050XTrfVFjPtDSeqYCfsh&index=32'))
mace_exercises.append(exercise('warrior stance front circles',['L','R'], level=3, url='https://www.youtube.com/watch?v=-4GMydVrlSk&list=PLk4oYPJ7TXKh050XTrfVFjPtDSeqYCfsh&index=34'))
mace_exercises.append(exercise('warrior stance backward circles',['L','R'], level=3, url='https://www.youtube.com/watch?v=ZfGdlIsWKXQ&list=PLk4oYPJ7TXKh050XTrfVFjPtDSeqYCfsh&index=37'))
mace_exercises.append(exercise('warrior stance alternating circles',['L','R'], level=3, url='https://www.youtube.com/watch?v=h_wcGKGlCus&list=PLk4oYPJ7TXKh050XTrfVFjPtDSeqYCfsh&index=38'))
mace_exercises.append(exercise('warrior stance 360 - bent leg same as top hand',['L','R'], level=4, url='https://www.youtube.com/watch?v=IgJXJy3zPGk&list=PLk4oYPJ7TXKh050XTrfVFjPtDSeqYCfsh&index=36'))
mace_exercises.append(exercise('warrior stance gamma cast - bent leg same as top hand',['L','R'], level=4, url='https://www.youtube.com/watch?v=IgJXJy3zPGk&list=PLk4oYPJ7TXKh050XTrfVFjPtDSeqYCfsh&index=36'))
mace_exercises.append(exercise('warrior stance 360 - bent leg opposite as top hand',['L','R'], level=4, url='https://www.youtube.com/watch?v=IgJXJy3zPGk&list=PLk4oYPJ7TXKh050XTrfVFjPtDSeqYCfsh&index=36'))
mace_exercises.append(exercise('warrior stance gamma cast - bent leg opposite as top hand',['L','R'], level=4, url='https://www.youtube.com/watch?v=IgJXJy3zPGk&list=PLk4oYPJ7TXKh050XTrfVFjPtDSeqYCfsh&index=36'))





club_exercises_2h = []
club_exercises_2h.append(exercise('inside circles', ['L','R'], level=1, url='https://www.youtube.com/watch?v=Exuf3a7RhYs&list=PLk4oYPJ7TXKgVZH0qykDznDeaAcFImRuS'))
club_exercises_2h.append(exercise('outside circles', ['L','R'], level=1, url='https://www.youtube.com/watch?v=-MuseVIc0bg&list=PLk4oYPJ7TXKgVZH0qykDznDeaAcFImRuS&index=2'))
club_exercises_2h.append(exercise('alternating circles', ['L','R'], level=2, url='https://www.youtube.com/watch?v=bIr0q5k9x8I&list=PLk4oYPJ7TXKgVZH0qykDznDeaAcFImRuS&index=16'))
club_exercises_2h.append(exercise('pullover', ['L','R'], level=1, url='https://www.youtube.com/watch?v=HsM0J39EmXg&list=PLk4oYPJ7TXKgVZH0qykDznDeaAcFImRuS&index=3'))
club_exercises_2h.append(exercise('alternating pullover', ['L','R'], level=1, url='https://www.youtube.com/watch?v=HsM0J39EmXg&list=PLk4oYPJ7TXKgVZH0qykDznDeaAcFImRuS&index=3'))
club_exercises_2h.append(exercise('shield cast', ['L','R'], level=2, url='https://www.youtube.com/watch?v=oBdXsknqSEM&list=PLk4oYPJ7TXKgVZH0qykDznDeaAcFImRuS&index=4'))
club_exercises_2h.append(exercise('gamma cast', ['L','R'], level=2, url='https://www.youtube.com/watch?v=rjhwF50fyd8&list=PLk4oYPJ7TXKgVZH0qykDznDeaAcFImRuS&index=5'))
club_exercises_2h.append(exercise('inside pendulum',['L','R'], level=2, url='https://www.youtube.com/watch?v=Maz36Iuixk4&list=PLk4oYPJ7TXKgVZH0qykDznDeaAcFImRuS&index=9'))
club_exercises_2h.append(exercise('outside pendulum',['L','R'], level=2, url='https://www.youtube.com/watch?v=y9qsJ0bpmzs&list=PLk4oYPJ7TXKgVZH0qykDznDeaAcFImRuS&index=10'))
club_exercises_2h.append(exercise('alternating pendulum',['L','R'], level=3, url='https://www.youtube.com/watch?v=GULjXPS_ba4&list=PLk4oYPJ7TXKgVZH0qykDznDeaAcFImRuS&index=14'))
club_exercises_2h.append(exercise('half kneeling shield cast',['L','R'],level=3,url='https://www.youtube.com/watch?v=vyLu0AFD-Mc&list=PLk4oYPJ7TXKgVZH0qykDznDeaAcFImRuS&index=31'))
club_exercises_2h.append(exercise('hammer swing',['L','R'],level=4,url='https://www.youtube.com/watch?v=Zk_uT6dHfFM&list=PLk4oYPJ7TXKgVZH0qykDznDeaAcFImRuS&index=34'))
club_exercises_2h.append(exercise('inside mill', ['L','R'], level=3))
club_exercises_2h.append(exercise('outside mill', ['L','R'], level=3))
club_exercises_2h.append(exercise('alternating mill circle transition', ['L','R'], level=4))
club_exercises_2h.append(exercise('alternating mill pendulum transition', ['L','R'], level=4))
club_exercises_2h.append(exercise('alternating mill pullover transition', ['L','R'], level=4))


club_exercises_1h = []
club_exercises_1h.append(exercise('inside circles', ['L','R'], level=1, url='https://www.youtube.com/watch?v=0ZzoCasyoAM&list=PLk4oYPJ7TXKgVZH0qykDznDeaAcFImRuS&index=6'))
club_exercises_1h.append(exercise('outside circles', ['L','R'], level=1, url='https://www.youtube.com/watch?v=OydLETgLfMA&list=PLk4oYPJ7TXKgVZH0qykDznDeaAcFImRuS&index=7'))
club_exercises_1h.append(exercise('shield cast', ['L','R'], level=2, url='https://www.youtube.com/watch?v=LKNgPDX2wRk&list=PLk4oYPJ7TXKgVZH0qykDznDeaAcFImRuS&index=8'))
club_exercises_1h.append(exercise('gamma cast', ['L','R'], level=2, url='https://www.youtube.com/watch?v=LKNgPDX2wRk&list=PLk4oYPJ7TXKgVZH0qykDznDeaAcFImRuS&index=8'))
club_exercises_1h.append(exercise('alternating 180 degree pullover', ['L','R'], level=3, url='https://www.youtube.com/watch?v=9JeH7kTi1ys&list=PLk4oYPJ7TXKgVZH0qykDznDeaAcFImRuS&index=21'))
club_exercises_1h.append(exercise('pullover', ['L','R'], level=1))
club_exercises_1h.append(exercise('inside mill', ['L','R'], level=3, url='https://www.youtube.com/watch?v=MqVk-qZruus&list=PLk4oYPJ7TXKgVZH0qykDznDeaAcFImRuS&index=11'))
club_exercises_1h.append(exercise('outside mill', ['L','R'], level=3, url='https://www.youtube.com/watch?v=MqVk-qZruus&list=PLk4oYPJ7TXKgVZH0qykDznDeaAcFImRuS&index=11'))
club_exercises_1h.append(exercise('inside pendulum',['L','R'], level=2, url='https://www.youtube.com/watch?v=n-fzOSaOiKY&list=PLk4oYPJ7TXKgVZH0qykDznDeaAcFImRuS&index=13'))
club_exercises_1h.append(exercise('outside pendulum',['L','R'], level=2, url='https://www.youtube.com/watch?v=SchCGLfQbjI&list=PLk4oYPJ7TXKgVZH0qykDznDeaAcFImRuS&index=12'))
club_exercises_1h.append(exercise('alternating pendulum',['L','R'], level=3, url='https://www.youtube.com/watch?v=CTPm9DBfZEU&list=PLk4oYPJ7TXKgVZH0qykDznDeaAcFImRuS&index=15'))
club_exercises_1h.append(exercise('inside circle hand change',['alternating'], level=2, url='https://www.youtube.com/watch?v=AWh_AdoASRY&list=PLk4oYPJ7TXKgVZH0qykDznDeaAcFImRuS&index=17'))
club_exercises_1h.append(exercise('outside circle hand change',['alternating'], level=2, url='https://www.youtube.com/watch?v=ucLZBDCYX3o&list=PLk4oYPJ7TXKgVZH0qykDznDeaAcFImRuS&index=18'))
club_exercises_1h.append(exercise('continuous inside circle hand change',['alternating'], level=3, url='https://www.youtube.com/watch?v=XPZgv-vf7ME&list=PLk4oYPJ7TXKgVZH0qykDznDeaAcFImRuS&index=19'))
club_exercises_1h.append(exercise('continuous outside circle hand change',['alternating'], level=3, url='https://www.youtube.com/watch?v=49iRIY2fMpE&list=PLk4oYPJ7TXKgVZH0qykDznDeaAcFImRuS&index=20'))
club_exercises_1h.append(exercise('crossbody clean',['L','R'],level=4,url='https://www.youtube.com/watch?v=HevZY3DmWhA&list=PLk4oYPJ7TXKgVZH0qykDznDeaAcFImRuS&index=40'))
club_exercises_1h.append(exercise('crossbody swipe',['L','R'],level=5,url='https://www.youtube.com/watch?v=ASZw05sMCxw&list=PLk4oYPJ7TXKgVZH0qykDznDeaAcFImRuS&index=41'))
club_exercises_1h.append(exercise('stagger stance crossbody clean',['L','R'],level=5,url='https://www.youtube.com/watch?v=PbxiyoCg1NU&list=PLk4oYPJ7TXKgVZH0qykDznDeaAcFImRuS&index=42'))
club_exercises_1h.append(exercise('stagger stance crossbody swipe',['L','R'],level=5,url='https://www.youtube.com/watch?v=Yc5kVA2hH1A&list=PLk4oYPJ7TXKgVZH0qykDznDeaAcFImRuS&index=43'))
club_exercises_1h.append(exercise('inside mill inside circle transition', ['alternating'], level=3))
club_exercises_1h.append(exercise('outside mill outside circle transition', ['alternating'], level=3))
club_exercises_1h.append(exercise('inside mill forward swing transition', ['alternating'], level=3))
club_exercises_1h.append(exercise('outside mill forward swing transition', ['alternating'], level=3))
club_exercises_1h.append(exercise('pendulum alternating mill', ['L','R'], level=3))
club_exercises_1h.append(exercise('swipe', ['L','R'], level=2))
club_exercises_1h.append(exercise('swipe forward swing transition', ['alternating'], level=3))
club_exercises_1h.append(exercise('forward swing', ['L','R'], level=1))
club_exercises_1h.append(exercise('forward swing hand to hand', ['alternating'], level=2))


kettlebell_movements = []
kettlebell_movements.append(exercise('swing',['2-handed'],level=0, url='https://www.youtube.com/watch?v=EIyOdqTf3r8&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=2'))
kettlebell_movements.append(exercise('goblet squat hands under',['2-handed'], level=0 , url='https://www.youtube.com/watch?v=7EGVKUH0K10&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=3'))
kettlebell_movements.append(exercise('goblet squat inverted grip',['2-handed'], level=0 , url='https://www.youtube.com/watch?v=7EGVKUH0K10&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=3'))
kettlebell_movements.append(exercise('goblet squat offset rack',['L','R'], level=1 , url='https://www.youtube.com/watch?v=7EGVKUH0K10&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=3'))
kettlebell_movements.append(exercise('flat back pullover',['2-handed'], level=1 , url='https://www.youtube.com/watch?v=b6JhIX3H2Nc&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=26'))
kettlebell_movements.append(exercise('pullover situp',['2-handed'], level=2 , url='https://www.youtube.com/watch?v=N4PxP6qGvqE&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=27'))
kettlebell_movements.append(exercise('pullover situp and press',['2-handed'], level=3 , url='https://www.youtube.com/watch?v=3vtRH4QulJo&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=28'))
kettlebell_movements.append(exercise('halo',['2-handed'], level=1 , url='https://www.youtube.com/watch?v=PJTIftBgGVk&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=30'))
kettlebell_movements.append(exercise('alternating halo',['2-handed'], level=2 , url='https://www.youtube.com/watch?v=eaOHhZlHSp4&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=32'))
kettlebell_movements.append(exercise('halo goblet squat',['2-handed'], level=2 , url='https://www.youtube.com/watch?v=tOAZDLFzdLE&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=34'))
kettlebell_movements.append(exercise('standing pullover',['2-handed'], level=1 , url='https://www.youtube.com/watch?v=YrUNuYiyi8g&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=38'))
kettlebell_movements.append(exercise('goblet/bottoms up step back lunge',['2-handed'], level=2 , url='https://www.youtube.com/watch?v=hKc-F9dxTro&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=86'))
kettlebell_movements.append(exercise('bottoms down step back lunge',['2-handed'], level=2 , url='https://www.youtube.com/watch?v=hKc-F9dxTro&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=86'))
kettlebell_movements.append(exercise('front rock-it',['2-handed'], level=1 , url='https://www.youtube.com/watch?v=CcJqrCGxWIo&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=89'))
kettlebell_movements.append(exercise('side-to-side rock-it',['2-handed'], level=2 , url='https://www.youtube.com/watch?v=EQGUPetJ3LY&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=90'))
kettlebell_movements.append(exercise('step forward lunge bottoms up',['2-handed'], level=3 , url='https://www.youtube.com/watch?v=X0MLRBuNiIg&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=93'))
kettlebell_movements.append(exercise('step forward lunge bottoms down',['2-handed'], level=3 , url='https://www.youtube.com/watch?v=X0MLRBuNiIg&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=93'))
# kettlebell_movements.append(exercise('',['2-handed'], level= , url=''))
# kettlebell_movements.append(exercise('',['2-handed'], level= , url=''))
# kettlebell_movements.append(exercise('',['2-handed'], level= , url=''))
# kettlebell_movements.append(exercise('',['2-handed'], level= , url=''))
# kettlebell_movements.append(exercise('',['2-handed'], level= , url=''))
# kettlebell_movements.append(exercise('',['2-handed'], level= , url=''))
kettlebell_movements.append(exercise('hand-to-hand swing',['L','R'], level=1 , url='https://www.youtube.com/watch?v=FCcKJ78k7mQ&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=4'))
kettlebell_movements.append(exercise('clean',['L','R'], level=0 , url='https://www.youtube.com/watch?v=RyIq9ZBxnNo&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=5'))
kettlebell_movements.append(exercise('snatch',['L','R'], level=2 , url='https://www.youtube.com/watch?v=xQqCyl-2ixQ&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=7'))
kettlebell_movements.append(exercise('TGU',['L','R'], level=1 , url='https://www.youtube.com/watch?v=2YollP91Wro&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=14'))
kettlebell_movements.append(exercise('inside circles',['L','R'], level=2 , url='https://www.youtube.com/watch?v=eLjxLunyBPY&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=19'))
kettlebell_movements.append(exercise('outside circles',['L','R'], level=2 , url='https://www.youtube.com/watch?v=ItwCc357GJo&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=20'))
kettlebell_movements.append(exercise('outside pendulum/outside clean',['L','R'], level=3, url='https://www.youtube.com/watch?v=87TMT9yCxx8&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=21'))
kettlebell_movements.append(exercise('inside pendulum/inside clean',['L','R'], level=3 , url='https://www.youtube.com/watch?v=Jtw0HexRySo&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=22'))
kettlebell_movements.append(exercise('alternating pendulum/alternating clean',['L','R'], level=4 , url='https://www.youtube.com/watch?v=3Wz30DVa1Z8&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=23'))
kettlebell_movements.append(exercise('alternating circles',['L','R'], level=3 , url='https://www.youtube.com/watch?v=gn_FzvH6JYw&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=25'))
kettlebell_movements.append(exercise('high windmill, bent leg',['L','R'], level=2 , url='https://www.youtube.com/watch?v=xtTI8yNgbS0&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=31'))
kettlebell_movements.append(exercise('high windmill, straight leg',['L','R'], level=3 , url='https://www.youtube.com/watch?v=VFHj4FehsfM&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=33'))
kettlebell_movements.append(exercise('high windmill, no foot movement',['L','R'], level= 4, url='https://www.youtube.com/watch?v=8w9zQBv7Wvk&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=35'))
kettlebell_movements.append(exercise('rock bottom front squat transitions',['alternating'], level=2 , url='https://www.youtube.com/watch?v=z3cwkA3pkh4&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=36'))
kettlebell_movements.append(exercise('seated globe up press',['2-handed'], level=2 , url='https://www.youtube.com/watch?v=xbOdGBjeKCc&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=37'))
kettlebell_movements.append(exercise('double windmill',['L','R'], level=4 , url='https://www.youtube.com/watch?v=E6gpvI1pFnY&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=42'))
kettlebell_movements.append(exercise('around the world',['alternating'], level=1 , url='https://www.youtube.com/watch?v=91citDXgmoE&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=44'))
kettlebell_movements.append(exercise('front to back figure 8',['alternating'], level=1 , url='https://www.youtube.com/watch?v=JUcmmpcEP0w&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=45'))
kettlebell_movements.append(exercise('back to front figure 8',['alternating'], level=1 , url='https://www.youtube.com/watch?v=gyD56KzniO8&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=46'))
kettlebell_movements.append(exercise('front to back figure 8 with around the world',['L','R'], level=2 , url='https://www.youtube.com/watch?v=owiXLvQmVrg&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=48'))
kettlebell_movements.append(exercise('back to front figure 8 with around the world',['L','R'], level=2 , url='https://www.youtube.com/watch?v=T_lITJHSZ4M&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=49'))
kettlebell_movements.append(exercise('inside circle hand transitions',['alternating'], level=4 , url='https://www.youtube.com/watch?v=NuA4Pb-Bens&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=50'))
kettlebell_movements.append(exercise('outside circle hand transitions',['alternating'], level=4 , url='https://www.youtube.com/watch?v=bhtU0qy6VpI&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=51'))
kettlebell_movements.append(exercise('half-kneeling clean',['L','R'], level=3 , url='https://www.youtube.com/watch?v=e-mFHJIVwYE&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=52'))
kettlebell_movements.append(exercise('half-kneeling press',['L','R'], level=3 , url='https://www.youtube.com/watch?v=xAwVy089Lgg&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=54'))
kettlebell_movements.append(exercise('clean to opposite leg stepback lunge',['L','R'], level=3 , url='https://www.youtube.com/watch?v=8mC0eaIAXMk&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=56'))
kettlebell_movements.append(exercise('half-kneeling clean and press windmill',['L','R'], level=4 , url='https://www.youtube.com/watch?v=2pzh4ZigTjE&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=57'))
kettlebell_movements.append(exercise('half-kneeling snatch',['L','R'], level=4 , url='https://www.youtube.com/watch?v=guwI1RWTiag&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=58'))
kettlebell_movements.append(exercise('half-kneeling windmill',['L','R'], level=3 , url='https://www.youtube.com/watch?v=uwVEb1fKqLM&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=59'))
kettlebell_movements.append(exercise('half-kneeling side press',['L','R'], level=2 , url='https://www.youtube.com/watch?v=6GjtemsVJQk&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=60'))
kettlebell_movements.append(exercise('half-kneeling bent position press',['L','R'], level=4 , url='https://www.youtube.com/watch?v=Bc3kZPDt6WE&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=62'))
kettlebell_movements.append(exercise('standing side press',['L','R'], level=3 , url='https://www.youtube.com/watch?v=QOTuMN9A0Hc&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=67'))
kettlebell_movements.append(exercise('bridge chess press',['L','R'], level=1 , url='https://www.youtube.com/watch?v=nCRpmIwT-as&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=68'))
kettlebell_movements.append(exercise('ball chest press',['L','R'], level=3 , url='https://www.youtube.com/watch?v=hdcKPiCBblw&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=69'))
kettlebell_movements.append(exercise('TGU base floor press',['L','R'], level=2 , url='https://www.youtube.com/watch?v=DSYpqFSpZEg&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=72'))
kettlebell_movements.append(exercise('TGU press to roll',['L','R'], level=3 , url='https://www.youtube.com/watch?v=XIy_XOUAEto&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=73'))
kettlebell_movements.append(exercise('TGU 1/4 getup to elbow',['L','R'], level=3 , url='https://www.youtube.com/watch?v=LDS7Grx3mLc&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=74'))
kettlebell_movements.append(exercise('TGU 1/2 getup to hand',['L','R'], level= 3, url='https://www.youtube.com/watch?v=3JXbBTysXpA&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=77'))
kettlebell_movements.append(exercise('waiter clean',['L','R'], level=3 , url='https://www.youtube.com/watch?v=F86s3FSXoPA&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=79'))
kettlebell_movements.append(exercise('waiter position transition/hot potato',['alternating'], level=4 , url='https://www.youtube.com/watch?v=AKiu97ruJoM&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=80'))
kettlebell_movements.append(exercise('outside swing',['L','R'], level=4 , url='https://www.youtube.com/watch?v=JPKCHFPoAFU&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=81'))
kettlebell_movements.append(exercise('outside swing to waiter catch',['L','R'], level=4 , url='https://www.youtube.com/watch?v=9RRWCkMIRSs&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=82'))
kettlebell_movements.append(exercise('outside swing to waiter catch transition',['alternating'], level=4 , url='https://www.youtube.com/watch?v=9RRWCkMIRSs&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=82'))
kettlebell_movements.append(exercise('figure 8 to waiter catch',['L','R'], level=4 , url='https://www.youtube.com/watch?v=o5gwVapaO-s&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=83'))
kettlebell_movements.append(exercise('figure 8 to waiter catch',['alternating'], level=4 , url='https://www.youtube.com/watch?v=o5gwVapaO-s&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=83'))
kettlebell_movements.append(exercise('static lunge cross rack loaded',['L','R'], level=2 , url='https://www.youtube.com/watch?v=Y7x667svnYo&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=85'))
kettlebell_movements.append(exercise('stepback lunge rack loaded same side',['L','R'], level=2 , url='https://www.youtube.com/watch?v=hKc-F9dxTro&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=86'))
kettlebell_movements.append(exercise('stepback lunge rack loaded opposite side',['L','R'], level=2 , url='https://www.youtube.com/watch?v=hKc-F9dxTro&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=86'))
kettlebell_movements.append(exercise('stepback lunge rack loaded alternating',['L','R'], level=2 , url='https://www.youtube.com/watch?v=hKc-F9dxTro&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=86'))
kettlebell_movements.append(exercise('snatch press',['L','R'], level=4 , url='https://www.youtube.com/watch?v=--Va9kOkkKE&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=88'))
kettlebell_movements.append(exercise('bench row',['L','R'], level=2, url='https://www.youtube.com/watch?v=l_cgMGUbFfc&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=92'))
kettlebell_movements.append(exercise('step forward lunge rack loaded same side',['L','R'], level=2 , url='https://www.youtube.com/watch?v=X0MLRBuNiIg&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=93'))
kettlebell_movements.append(exercise('step forward lunge rack loaded opposite side',['L','R'], level=3 , url='https://www.youtube.com/watch?v=X0MLRBuNiIg&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=93'))
kettlebell_movements.append(exercise('step forward lunge rack loaded alternating',['L','R'], level=3 , url='https://www.youtube.com/watch?v=X0MLRBuNiIg&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=93'))
kettlebell_movements.append(exercise('unsupported row',['L','R'], level=3 , url='https://www.youtube.com/watch?v=bZ4h1Bqw-to&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=94'))
kettlebell_movements.append(exercise('neutral stance alternating row',['L','R'], level=2 , url='https://www.youtube.com/watch?v=NkO2g54npjM&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=95'))
kettlebell_movements.append(exercise('TGU clean - step back - clean',['L','R'], level=3 , url='https://www.youtube.com/watch?v=WdG1lZ9b4cw&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=97'))
kettlebell_movements.append(exercise('Hunters squat/lunge same side load',['L','R'], level=4 , url='https://www.youtube.com/watch?v=LLt-wIkB_Xs&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=98'))
kettlebell_movements.append(exercise('Hunters squat/lunge opposite side load',['L','R'], level=4 , url='https://www.youtube.com/watch?v=LLt-wIkB_Xs&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=98'))
kettlebell_movements.append(exercise('clean and press',['L','R'], level= 0, url='https://www.youtube.com/watch?v=48qvCvJJr8Y&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=99'))
kettlebell_movements.append(exercise('clean and press to half-kneeling clean and press',['L','R'], level= 3, url='https://www.youtube.com/watch?v=5Uai_S4drVU&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=100'))
kettlebell_movements.append(exercise('TGU with complexity added',['L','R'], level=4 , url='https://www.youtube.com/watch?v=dNLd-OF4ydg&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=101'))
kettlebell_movements.append(exercise('snatch press with stepback lunge',['L','R'], level=3 , url='https://www.youtube.com/watch?v=9-DZXunyYbc&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=102'))
kettlebell_movements.append(exercise('snatch press with stepback lunge overhead bell',['L','R'], level=4 , url='https://www.youtube.com/watch?v=qYDZ4-LINUY&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=103'))
kettlebell_movements.append(exercise('side-to-side swing',['L','R'], level=5, url='https://www.youtube.com/watch?v=yQUYjqDvvfM&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=107'))
kettlebell_movements.append(exercise('dead clean',['L','R'], level=3 , url='https://www.youtube.com/watch?v=9OBl-jEPWo4&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=108'))
# kettlebell_movements.append(exercise('',['L','R'], level= , url=''))
# kettlebell_movements.append(exercise('',['L','R'], level= , url=''))
# kettlebell_movements.append(exercise('',['L','R'], level= , url=''))
kettlebell_movements.append(exercise('clean',['double bell'], level=2 , url='https://www.youtube.com/watch?v=26GZTfSdz-s&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=70'))
kettlebell_movements.append(exercise('alternating clean',['double bell'], level=3 , url='https://www.youtube.com/watch?v=y4MFTparTmE&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=71'))
kettlebell_movements.append(exercise('press',['double bell'], level=2 , url='https://www.youtube.com/watch?v=VJZDDi-0vGU&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=75'))
kettlebell_movements.append(exercise('seesaw press',['double bell'], level=3 , url='https://www.youtube.com/watch?v=7Pnein1QoCk&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=76'))
kettlebell_movements.append(exercise('clean and press',['double bell'], level=3 , url='https://www.youtube.com/watch?v=3OaK-lDtCY4&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=78'))
kettlebell_movements.append(exercise('outside swing',['double bell'], level=3 , url='https://www.youtube.com/watch?v=_Uy18LZ5sI0&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=84'))
kettlebell_movements.append(exercise('rock-it',['double bell'], level=2 , url='https://www.youtube.com/watch?v=RT8BNDpSe70&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=91'))
kettlebell_movements.append(exercise('alternating double row unsupported',['double bell'], level=3 , url='https://www.youtube.com/watch?v=6nyznu2WKbc&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=96'))
kettlebell_movements.append(exercise('alternating double row supported',['double bell'], level=3 , url='https://www.youtube.com/watch?v=6nyznu2WKbc&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=96'))
kettlebell_movements.append(exercise('double clean to alternating cleans low',['double bell'], level=4, url='https://www.youtube.com/watch?v=P4-QApZNIGo&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=104'))
kettlebell_movements.append(exercise('symmetrical press to seesaw press',['double bell'], level=3 , url='https://www.youtube.com/watch?v=cEXrSDF2CzI&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=105'))
kettlebell_movements.append(exercise('double clean to alternating cleans high',['double bell'], level=4, url='https://www.youtube.com/watch?v=39ngyHsT6NA&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=106'))
kettlebell_movements.append(exercise('dead clean',['double bell'], level=3 , url='https://www.youtube.com/watch?v=bET3BJkaYKQ&list=PLk4oYPJ7TXKg4lvvabXEn9BI4c9i696kx&index=109'))
# kettlebell_movements.append(exercise('',['double bell'], level= , url=''))
# kettlebell_movements.append(exercise('',['double bell'], level= , url=''))
# kettlebell_movements.append(exercise('',['double bell'], level= , url=''))
# kettlebell_movements.append(exercise('',['double bell'], level= , url=''))

