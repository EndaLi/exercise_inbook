def country_city(country,city,population=''):
    if population:
        combine = country + ',' + city + ' - '+population
    else:
        combine = country + ',' + city
    return combine.title()
