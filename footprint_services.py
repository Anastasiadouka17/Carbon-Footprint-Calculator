# COMP 202 A1: Part 2
# Footprint of utilities & university
# Author: Anastasia Douka
#ID=260768503

import doctest
from unit_conversion import *

INCOMPLETE = -1

######################################### Utilities

def fp_from_gas(monthly_gas):
    '''(num) -> float
    Calculate metric tonnes of CO2E produced annually
    based on monthly natural gas bill in $.

    Source: https://www.forbes.com/2008/04/15/green-carbon-living-forbeslife-cx_ls_0415carbon.html#1f3715d01852
        B.) Multiply your monthly gas bill by 105 [lbs, to get annual amount] 

    >>> fp_from_gas(0)
    0.0
    >>> round(fp_from_gas(100), 4)
    4.7627
    >>> round(fp_from_gas(25), 4)
    1.1907
    '''
    lbs_to_kg=pound_to_kg(105)
    lbs_to_tonnes=kg_to_tonnes(lbs_to_kg)
    return monthly_gas*lbs_to_tonnes
    
                           

def fp_from_hydro(daily_hydro):
    '''(num) -> float
    Calculate metric tonnes of CO2E produced annually
    based on average daily hydro usage.

    To find out your average daily hydro usage in kWh:
        Go to https://www.hydroquebec.com/portail/en/group/clientele/portrait-de-consommation
        Scroll down to "Annual total" and press "kWh"

    Source: https://www.hydroquebec.com/data/developpement-durable/pdf/co2-emissions-electricity-2017.pdf
        0.6 kg CO2E / MWh

    >>> fp_from_hydro(0)
    0.0
    >>> round(fp_from_hydro(10), 4)
    0.0022
    >>> round(fp_from_hydro(48.8), 4)
    0.0107
    '''
    
    kwh_to_mwh= daily_hydro/1000
    annual_hydro= daily_to_annual(kwh_to_mwh)
    tonnes=kg_to_tonnes(0.6)
    
    return annual_hydro*tonnes
    

def fp_of_utilities(daily_hydro, monthly_gas):
    '''(num, num, num) -> float
    Calculate metric tonnes of CO2E produced annually from
    daily hydro (in kWh) and gas bills (in $).

    >>> fp_of_utilities(0, 0)
    0.0
    >>> round(fp_of_utilities(100, 0), 4)
    0.0219
    >>> round(fp_of_utilities(0, 100), 4)
    4.7627
    >>> round(fp_of_utilities(50, 20), 4)
    0.9635
    '''
    
    return (fp_from_hydro(daily_hydro)+fp_from_gas(monthly_gas))


#################################################


def fp_of_studies(annual_uni_credits):
    '''(num, num, num) -> flt
    Return metric tonnes of CO2E from being a student, based on
    annual university credits.

    Source: https://www.mcgill.ca/facilities/files/facilities/ghg_inventory_report_2017.pdf
        1.12 tonnes per FTE (30 credit) student

    >>> round(fp_of_studies(0), 4)
    0.0
    >>> round(fp_of_studies(30), 4)
    1.12
    >>> round(fp_of_studies(18), 4)
    0.672
    '''
    credits_to_fte=annual_uni_credits/30 #1 FTE is 30 credits, so to find the number of FTE of a student divide credits by 30.
    
    return credits_to_fte*1.12



#################################################

if __name__ == '__main__':
    doctest.testmod()
