import numpy as np


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
                only_isolation=False, only_alternating=False):
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