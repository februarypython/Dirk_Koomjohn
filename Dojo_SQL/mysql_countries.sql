*1**************************
select name, language, percentage from countries

join languages on countries.code = languages.country_code

where language = 'slovene'

order by percentage desc;

*2**************************
select countries.name, count(cities.id) as "Cities" from countries

join cities on countries.code = cities.country_code

group by countries.id;
order by Cities

*3**************************
select countries.name, cities.name, cities.population from countries

join cities on countries.code = cities.country_code

where countries.name = 'mexico' and cities.population > 500000

order by cities.population desc


*4**************************
select name, language, percentage from countries

join languages on countries.code = languages.country_code

where percentage > 89

order by percentage desc;


*5**************************
select name, surface_area from countries

where surface_area > 501 and population > 100000;

*6**************************
select name from countries

where life_expectancy > 75

and government_form = 'Constitutional Monarchy'

and capital > 200;

*7**************************
select countries.name, cities.name, cities.district, cities.population
from countries
join cities onN countries.id = cities.country_id
where countries.name = 'Argentina'
and cities.district = 'Buenos Aires'
and cities.population > 500000;

*8**************************
select countries.region, count(countries.id) as num_countries
from countries
group by countries.region
order by num_countries desc;