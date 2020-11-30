# COMP 202 A1: Part 3
# Footprint of local transportation and travel
# Author: Anastasia Douka
#ID=260768503

import doctest
from unit_conversion import *

INCOMPLETE = -1


################################################


def fp_from_transit(weekly_bus_rides, weekly_rail_rides):
    '''
    (num, num) -> flt
    Annual CO2E tonnes from public transit based on number of weekly bus
    rides and weekly rail (metro/commuter train) rides.

    Source: https://en.wikipedia.org/wiki/Transportation_in_Montreal
    The average amount of time people spend commuting with public transit in Montreal, for example to and from work, on a weekday is 87 min. 29.% of public transit riders, ride for more than 2 hours every day. The average amount of time people wait at a stop or station for public transit is 14 min, while 17% of riders wait for over 20 minutes on average every day. The average distance people usually ride in a single trip with public transit is 7.7 km, while 17% travel for over 12 km in a single direction.[28]
    Source: https://en.wikipedia.org/wiki/Société_de_transport_de_Montréal
    As of 2011, the average daily ridership is 2,524,500 passengers: 1,403,700 by bus, 1,111,700 by rapid transit and 9,200 by paratransit service.

    Source: How Bad Are Bananas
        A mile by bus: 150g CO2E 
        A mile by subway train: 160g CO2E for London Underground

    >>> fp_from_transit(0, 0)
    0.0
    >>> round(fp_from_transit(1, 0), 4)
    0.0374
    >>> round(fp_from_transit(0, 1), 4)
    0.0399
    >>> round(fp_from_transit(10, 2), 4)
    0.4544
    '''
    annual_bus_trips= weekly_to_annual(weekly_bus_rides)
    annual_rail_trips= weekly_to_annual(weekly_rail_rides)
    coe_from_bustrip= 7.7*kg_to_tonnes(0.09321)#1 mile->0.150kg CO2E, 1km->0.621371miles, kg=0.150*0.621371=0.09321kg, 1km->0.09321kg CO2E.
    coe_from_railtrip= 7.7*kg_to_tonnes(0.09942)#1 mile->0.160kg CO2E, 1km->0.621371miles,kg=0.160*0.621371=0.09942kg, 1km->0.09942kg CO2E.
    
    return (annual_bus_trips*coe_from_bustrip)+(annual_rail_trips*coe_from_railtrip)


def fp_from_taxi_uber(weekly_uber_rides):
    '''(num) -> flt
    Estimate in metric tonnes of CO2E the annual footprint from a given
    number of weekly uber/taxi/etc rides.

    Source: https://www.mapc.org/resource-library/the-growing-carbon-footprint-of-ride-hailing-in-massachusetts/
        81 million trips -> 100,000 metric tonnes

    >>> fp_from_taxi_uber(0)
    0.0
    >>> round(fp_from_taxi_uber(10), 4)
    0.6442
    >>> round(fp_from_taxi_uber(25), 4)
    1.6104
    '''
    annual_uber_rides= weekly_to_annual(weekly_uber_rides)
    
    return annual_uber_rides*(1/810) #if 81 million trips--> 100,00 mretric tonnes, then 1 trip-->1/810 metric tonnes.


def fp_from_driving(weekly_km_driven):
    '''
    (num) -> flt
    Approximate CO2E footprint for one year of driving, based on total km driven.
    Result in metric tonnes.
    Source: https://www.forbes.com/2008/04/15/green-carbon-living-forbeslife-cx_ls_0415carbon.html#1f3715d01852
    "D.) Multiply total yearly mileage by .79 (for pounds)"

    >>> fp_from_driving(0)
    0.0
    >>> round(fp_from_driving(100), 4)
    1.1618
    >>> round(fp_from_driving(1234), 4)
    14.3365
    '''
    mileage= km_to_miles(weekly_km_driven)#have to convert it to miles, in order to multiply by given 0.79 factor
    coe_in_pounds= mileage*0.79
    coe_in_kg= pound_to_kg(coe_in_pounds)#conversion from lbs to kg of CO2E
    coe_in_tonnes= kg_to_tonnes(coe_in_kg)#conversion from kg to tonnes of CO2E
    weekly_driving_to_annual= weekly_to_annual(coe_in_tonnes)#conversion from weekly number to annual as asked
    return weekly_driving_to_annual


def fp_of_transportation(weekly_bus_rides, weekly_rail_rides, weekly_uber_rides, weekly_km_driven):
    '''(num, num, num, num) -> flt
    Estimate in tonnes of CO2E the footprint of weekly transportation given
    specified annual footprint in tonnes of CO2E from transportation.

    >>> fp_of_transportation(0, 0, 0, 0)
    0.0
    >>> round(fp_of_transportation(2, 2, 1, 10), 4)
    0.3354
    >>> round(fp_of_transportation(1, 2, 3, 4), 4)
    0.3571
    '''
    return fp_from_transit(weekly_bus_rides, weekly_rail_rides)+fp_from_taxi_uber(weekly_uber_rides)+fp_from_driving(weekly_km_driven)

#################################################

def fp_from_flights(annual_long_flights, annual_short_flights):
    '''(num, num)-> float
    Based on the annual number of long flights (>4 h) and short flights (<4), calculate the annual CO2E footprint for flights, in metric tonnes.
    Source for flights: https://www.forbes.com/2008/04/15/green-carbon-living-forbeslife-cx_ls_0415carbon.html#1f3715d01852 --- in lbs
    ''Multiply the number of short flights by 1,100 lbs.
    Multiply the number of long flights by 4,400 lbs.''

    >>> round(fp_from_flights(1, 0), 4)
    1.9958
    >>> round(fp_from_flights(0, 1), 4)
    0.499
    >>> round(fp_from_flights(3,3), 4)
    7.4843
    '''
    coe_short_lbs_to_kg= pound_to_kg(1100)#coe=CO2E, of short rides from pounds to kg
    coe_short_in_tonnes= kg_to_tonnes(coe_short_lbs_to_kg)#coe=CO2E, from kg to tonnes
    coe_long_lbs_to_kg= pound_to_kg(4400)#coe=CO2E, of long rides from pounds to kg
    coe_long_in_tonnes= kg_to_tonnes(coe_long_lbs_to_kg)
    
    return (annual_long_flights*coe_long_in_tonnes)+(annual_short_flights*coe_short_in_tonnes)

    
def fp_from_train(annual_train):
    '''(num)-> float
    Based on an annual number of intercity train rides, calaculate the annual CO2E footprint from intercity train rides, in metric tonnes.
    Source for trains: https://media.viarail.ca/sites/default/files/publications/SustainableMobilityReport2016_EN_FINAL.pdf
    137,007 tCO2E from all of Via Rail, 3974000 riders
        -> 34.45 kg CO2E
    >>> round(fp_from_train(1), 4)
    0.0345
    >>> round(fp_from_train(5), 4)
    0.1723
    >>> round(fp_from_train(12), 4)
    0.4134
    '''
    coe_from_train_in_tonnes= kg_to_tonnes(34.45)

    return annual_train*coe_from_train_in_tonnes

def fp_from_coach(annual_coach):
    '''(num)-> float
    Based on an annual number of intercity coach bus rides, calculate the annual COE2 footprint from coach bus rides, in metric tonnes.
    Source for buses: How Bad Are Bananas
        66kg CO2E for ROUND TRIP coach bus ride from NYC to Niagara Falls
        I'm going to just assume that's an average length trip.
    >>> round(fp_from_coach(1), 4)
    0.033
    >>> round(fp_from_coach(30), 4)
    0.99
    >>> round(fp_from_coach(48), 4)
    1.584
    '''
    coe_coach_in_tonnes= kg_to_tonnes(33)
    
    return annual_coach*coe_coach_in_tonnes
    

def fp_from_hotels(annual_hotels):
    '''(num)-> float
    Based on the annual spending in hotels, calculate the annual CO2E footprint from spending in hotels, in metric tonnes.
    Source for hotels: How Bad Are Bananas
        270 g CO2E for every dollar spent #270g=0.270kg
    >>> round(fp_from_hotels(30), 4)
    0.0081
    >>> round(fp_from_hotels(100), 4)
    0.027
    >>> round(fp_from_hotels(1200), 4)
    0.324
    '''
    coe_hotels_in_tonnes= kg_to_tonnes(0.270)

    return annual_hotels*coe_hotels_in_tonnes



#################################################

def fp_of_travel(annual_long_flights, annual_short_flights, annual_train, annual_coach, annual_hotels):
    '''(num, num, num, num, num) -> float
    Approximate CO2E footprint in metric tonnes for annual travel, based on number of long flights (>4 h), short flights (<4), intercity train rides, intercity coach bus rides, and spending at hotels.

    Source for flights: https://www.forbes.com/2008/04/15/green-carbon-living-forbeslife-cx_ls_0415carbon.html#1f3715d01852 --- in lbs
    "E.) Multiply the number of flights--4 hours or less--by 1,100 lbs
    F.) Multiply the number of flights--4 hours or more--by 4,400 lbs"

    Source for trains: https://media.viarail.ca/sites/default/files/publications/SustainableMobilityReport2016_EN_FINAL.pdf
    137,007 tCO2E from all of Via Rail, 3974000 riders
        -> 34.45 kg CO2E

    Source for buses: How Bad Are Bananas
        66kg CO2E for ROUND TRIP coach bus ride from NYC to Niagara Falls
        I'm going to just assume that's an average length trip, because better data not readily avialible.

    Source for hotels: How Bad Are Bananas
        270 g CO2E for every dollar spent

    >>> fp_of_travel(0, 0, 0, 0, 0)
    0.0
    >>> round(fp_of_travel(0, 1, 0, 0, 0), 4) # short flight
    0.499
    >>> round(fp_of_travel(1, 0, 0, 0, 0), 4) # long flight
    1.9958
    >>> round(fp_of_travel(2, 2, 0, 0, 0), 4) # some flights
    4.9895
    >>> round(fp_of_travel(0, 0, 1, 0, 0), 4) # train
    0.0345
    >>> round(fp_of_travel(0, 0, 0, 1, 0), 4) # bus
    0.033
    >>> round(fp_of_travel(0, 0, 0, 0, 100), 4) # hotel
    0.027
    >>> round(fp_of_travel(6, 4, 24, 2, 2000), 4) # together
    15.4034
    >>> round(fp_of_travel(1, 2, 3, 4, 5), 4) # together
    3.2304
    '''

    return fp_from_flights(annual_long_flights, annual_short_flights)+ fp_from_train(annual_train)+ fp_from_coach(annual_coach)+ fp_from_hotels(annual_hotels)

#################################################

if __name__ == '__main__':
    doctest.testmod()
