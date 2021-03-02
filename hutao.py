from math import ceil
from math import floor

e_skill_values = {'1':0.0384, '2':0.0407, '3':0.043, '4':0.046, '5':0.0483, '6':0.0506, '7':0.0536, '8':0.0566, '9':0.0596, '10':0.0626, '11':0.0656, '12':0.0685, '13':0.0715}
hu_tao = {'hp':15552, 'atk': 106}

def compute_walnut_hp(e_skill_level, weapon_base_attack):
    return ceil((weapon_base_attack+hu_tao['atk'])/e_skill_values[e_skill_level]*4)

def represents_int(string):
    try: 
        string = int(string)
        if string >= 0:
            return True
        else:
            return False
    except ValueError:
        return False

def validate_skill(message):
    aux = input(message)
    if aux=='bye':
        return 'bye'
    elif aux not in e_skill_values.keys():
        return validate_skill('invalid value, please enter your e skill level\n')
    else:
        return aux

def validate_int(message):
    aux = input(message)
    if aux=='bye':
        return 'bye'
    else:
        try: 
            value = int(aux)
            if value >= 0:
                return value
            else:
                return validate_int('invalid value, please enter your weapon\'s base attack\n')
        except ValueError:
            return validate_int('invalid value, please enter your weapon\'s base attack\n')

print('welcome to hu tao\'s max hp calculator, type \'bye\' at any point to end the program\n')
while True:
    e_skill = validate_skill('type your e skill level\n')
    if e_skill=='bye':
        print('ok bai')
        break
    else:
        base_atk = validate_int('type your weapon\'s base attack\n')
        if base_atk=='bye':
            print('ok bai')
            break
        else:
            print('\nyour hp ceiling is:',compute_walnut_hp(e_skill, base_atk))
            print('1% atk gives you ', floor(base_atk+hu_tao['atk']*0.01), ' atk')
            print('1% hp gives you ', floor(hu_tao['hp']*0.01*e_skill_values[e_skill]), ' atk during e\n')
