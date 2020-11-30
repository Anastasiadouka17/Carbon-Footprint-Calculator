# COMP 202 A1: Part 4
# Footprint of computing and diet
# Author: Anastasia Douka
#ID=260768503

import doctest
from unit_conversion import *

INCOMPLETE = -1

######################################
def fp_from_online_use(daily_online_use):
    '''(num)-> float
    Based on daily hours of online use, calculate in metric tonnes the annual CO2E produced from daily online use.
    Source for online use: How Bad Are Bananas
        55 g CO2E / hour, 55 g->0.055 kg
    >>> round(fp_from_online_use(1), 4)
    0.0201
    >>> round(fp_from_online_use(6), 4)
    0.1205
    >>> round(fp_from_online_use(15), 4)
    0.3013
    '''
    annual_online_use= daily_to_annual(daily_online_use)#convert daily use to annual
    coe_online_in_tonnes= kg_to_tonnes(0.055)#coe=CO2E, convert constant to metric tonnes

    return annual_online_use*coe_online_in_tonnes

def fp_from_phone_use(daily_phone_use):
    '''(num)-> float
    Based on the daily hours of phone use, calculate in metric tonnes the annual CO2E produced from this.
    Source for phone use: How Bad Are Bananas
        1250 kg CO2E for a year of 1 hour a day.
    >>> round(fp_from_phone_use(1), 4)
    1.25
    >>> round(fp_from_phone_use(3), 4)
    3.75
    >>> round(fp_from_phone_use(7), 4)
    8.75
    '''
    annual_phone_use= daily_to_annual(daily_phone_use)
    coe_in_tonnes= kg_to_tonnes(3.4224)#coe=CO2E, 1 year-> 1250kg, 1 hour->1250/365.2425(Gregorian calendar), 1hour-> 3.4224 kg.

    return annual_phone_use*coe_in_tonnes
       
def fp_from_light_devices(new_light_devices):
    '''(num)-> float
    Based on the number of new small portbale devices that were bought in a year, calculate the annual metric tones of CO2E this produces. 
    Assume that one new small portable device (e.g. phone, e-reader, small tablet) produces 75 kg CO2E.
    >>> round(fp_from_light_devices(2), 4)
    0.15
    >>> round(fp_from_light_devices(5), 4)
    0.375
    >>> round(fp_from_light_devices(10), 4)
    0.75
    '''
    coe_small_devices_in_tonnes= kg_to_tonnes(75)

    return new_light_devices*coe_small_devices_in_tonnes

def fp_from_medium_devices(new_medium_devices):
    '''(num)-> float
    Based on the number of new medium-sized devices that were bought in a year, calculate the annual metric tones of CO2E this produces. 
    Assume that one new medium-sized device (e.g. laptop, big tablet): 200 kg CO2E.
    >>> round(fp_from_medium_devices(1), 4)
    0.2
    >>> round(fp_from_medium_devices(6), 4)
    1.2
    >>> round(fp_from_medium_devices(12), 4)
    2.4
    '''
    coe_medium_in_tonnes= kg_to_tonnes(200)

    return new_medium_devices*coe_medium_in_tonnes
    
def fp_from_heavy_devices(new_heavy_devices):
    '''(num)-> float
    Based on the number of new large/heavy devices that were bought in a year, calculate the annual metric tonnes of CO2E this produces.
    Assume one new large/heavy device (e.g. desktop workstation, server, or gaming console): 800 kg CO2E
    >>> round(fp_from_heavy_devices(1), 4)
    0.8
    >>> round(fp_from_heavy_devices(6), 4)
    4.8
    >>> round(fp_from_heavy_devices(12), 4)
    9.6
    '''
    coe_heavy_in_tonnes= kg_to_tonnes(800)

    return new_heavy_devices*coe_heavy_in_tonnes

def fp_of_computing(daily_online_use, daily_phone_use, new_light_devices, new_medium_devices, new_heavy_devices):
    '''(num, num) -> float

    Metric tonnes of CO2E from computing, based on daily hours of online & phone use, and how many small (phone/tablet/etc) & large (laptop) & workstation devices you bought.

    Source for online use: How Bad Are Bananas
        55 g CO2E / hour

    Source for phone use: How Bad Are Bananas
        1250 kg CO2E for a year of 1 hour a day

    Source for new devices: How Bad Are Bananas
        200kg: new laptop
        800kg: new workstation
        And from: https://www.cnet.com/news/apple-iphone-x-environmental-report/
        I'm estimating 75kg: new small device

    >>> fp_of_computing(0, 0, 0, 0, 0)
    0.0
    >>> round(fp_of_computing(6, 0, 0, 0, 0), 4)
    0.1205
    >>> round(fp_of_computing(0, 1, 0, 0, 0), 4)
    1.25
    >>> fp_of_computing(0, 0, 1, 0, 0)
    0.075
    >>> fp_of_computing(0, 0, 0, 1, 0)
    0.2
    >>> fp_of_computing(0, 0, 0, 0, 1)
    0.8
    >>> round(fp_of_computing(4, 2, 2, 1, 1), 4)
    3.7304
    '''
    return fp_from_online_use(daily_online_use)+fp_from_phone_use(daily_phone_use)+fp_from_light_devices(new_light_devices)+fp_from_medium_devices(new_medium_devices)+fp_from_heavy_devices(new_heavy_devices)


######################################

def fp_from_meat(daily_g_meat):
    '''(num)-> float
    Based on the daily consumption of meat, calculate in metric tonnes the annual CO2E produced from this.
    A vegan diet is 2.89 kg CO2E / day in the UK. 
    It is stated that approximately 0.0268 kg CO2E/day per gram of meat eaten.
    >>> round(fp_from_meat(1), 4)
    0.0098
    >>> round(fp_from_meat(40), 4)
    0.3915
    >>> round(fp_from_meat(120), 4)
    1.1746
    '''
    coe_from_meat_in_tonnes= kg_to_tonnes(0.0268)
    annual_g_meat= daily_to_annual(daily_g_meat)
    return (annual_g_meat*coe_from_meat_in_tonnes)

def fp_from_cheese(daily_g_cheese):
    '''(num)-> float
    Based on the daily consumption of cheese, calculate in metric tonnes the annual amount of CO2E produced from this.
    A vegan diet is 2.89 kg CO2E / day in the UK.
    It is found from  How Bad Are Bananas:
        1 kg of hard cheese -> 12 kg CO2E
        1 gram of cheese -> 0.012 kg CO2E
    >>> round(fp_from_cheese(1), 4)
    0.0044
    >>> round(fp_from_cheese(10), 4)
    0.0438
    >>> round(fp_from_cheese(100), 4)
    0.4383
    '''
    coe_from_cheese_in_tonnes= kg_to_tonnes(0.012)
    annual_g_cheese= daily_to_annual(daily_g_cheese)
    return(annual_g_cheese*coe_from_cheese_in_tonnes)


def fp_from_milk(daily_L_milk):
    '''(num)-> float
    Based on the daily consumption of milk, calculate in metric tonnes the annual amount of CO2E produced from this.
    A vegan diet is 2.89 kg CO2E / day in the UK.
    From How Bad Are Bananas: 
        1 litre of milk produces 0.2677777 kg of CO2E
    >>> round(fp_from_milk(1), 4)
    0.0978
    >>> round(fp_from_milk(7), 4)
    0.6844
    >>> round(fp_from_milk(15), 4)
    1.4666
    '''
    coe_from_milk_in_tonnes= kg_to_tonnes(0.2677)
    annual_L_milk= daily_to_annual(daily_L_milk)
    return(annual_L_milk*coe_from_milk_in_tonnes)
                   
def fp_from_eggs(daily_num_eggs):
    '''(num)-> float
    Based on the daily consumption of eggs, calculate in metric tonnes the annual amount of CO2E produced from this.
    A vegan diet is 2.89 kg CO2E / day in the UK.
    From How Bad Are Bananas:
        12 eggs -> 3.6 kg CO2E 
            --> 0.3 kg CO2E per egg
    >>> round(fp_from_eggs(1), 4)
    0.1096
    >>> round(fp_from_eggs(8), 4)
    0.8766
    >>> round(fp_from_eggs(20), 4)
    2.1915
    '''
    coe_from_eggs_in_tonnes= kg_to_tonnes(0.3)
    annual_num_eggs= daily_to_annual(daily_num_eggs)
    return(annual_num_eggs*coe_from_eggs_in_tonnes)

    
def fp_of_diet(daily_g_meat, daily_g_cheese, daily_L_milk, daily_num_eggs):
    '''
    (num, num, num, num) -> flt
    Approximate annual CO2E footprint in metric tonnes, from diet, based on daily consumption of meat in grams, cheese in grams, milk in litres, and eggs.

    Based on https://link.springer.com/article/10.1007%2Fs10584-014-1169-1
    A vegan diet is 2.89 kg CO2E / day in the UK.
    I infer approximately 0.0268 kgCO2E/day per gram of meat eaten.

    This calculation misses forms of dairy that are not milk or cheese, such as ice cream, yogourt, etc.

    From How Bad Are Bananas:
        1 pint of milk (2.7 litres) -> 723 g CO2E 
                ---> 1 litre of milk: 0.2677777 kg of CO2E
        1 kg of hard cheese -> 12 kg CO2E 
                ---> 1 g cheese is 12 g CO2E -> 0.012 kg CO2E
        12 eggs -> 3.6 kg CO2E 
                ---> 0.3 kg CO2E per egg

    >>> round(fp_of_diet(0, 0, 0, 0), 4) # vegan
    1.0556
    >>> round(fp_of_diet(0, 0, 0, 1), 4) # 1 egg
    1.1652
    >>> round(fp_of_diet(0, 0, 1, 0), 4) # 1 L milk
    1.1534
    >>> round(fp_of_diet(0, 0, 1, 1), 4) # egg and milk
    1.2629
    >>> round(fp_of_diet(0, 10, 0, 0), 4) # cheeese
    1.0994
    >>> round(fp_of_diet(0, 293.52, 1, 1), 4) # egg and milk and cheese
    2.5494
    >>> round(fp_of_diet(25, 0, 0, 0), 4) # meat
    1.3003
    >>> round(fp_of_diet(25, 293.52, 1, 1), 4) 
    2.7941
    >>> round(fp_of_diet(126, 293.52, 1, 1), 4)
    3.7828
    '''
    return 1.0556+fp_from_meat(daily_g_meat)+fp_from_cheese(daily_g_cheese)+fp_from_milk(daily_L_milk)+fp_from_eggs(daily_num_eggs)
    #1.0556 is added because it is the annual value of COE2 produced without eating meat,dairy,or eggs (vegan).

#################################################

if __name__ == '__main__':
    doctest.testmod()

