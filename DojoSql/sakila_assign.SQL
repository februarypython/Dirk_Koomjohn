**1************************
select first_name, last_name, email, address, address2, postal_code from sakila.customer

join sakila.address

on address.address_id = customer.address_id

where address.city_id = '312'


**2************************
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name from sakila.film

JOIN sakila.film_category ON film.film_id = film_category.film_id

JOIN sakila.category ON film_category.category_id = category.category_id

WHERE category.name = 'Comedy';

**3************************ 
select actor.actor_id, concat(actor.first_name, ' ', actor.last_name) AS actor,
       title, film.description, film.release_year
 from sakila.film

join sakila.film_actor on film.film_id = film_actor.film_id

join sakila.actor on film_actor.actor_id = actor.actor_id

where actor.actor_id = 5;

**4************************
select customer.first_name, customer.last_name, customer.email, address.address from sakila.customer

join sakila.address on customer.address_id = address.address_id

join sakila.city on address.city_id = city.city_id
where customer.store_id = 1 and

      city.city_id = 1 or 42 or 312 or 459;

**5************************
select film.title, film.description, film.release_year, film.rating, film.special_features from sakila.film

join sakila.film_actor ON film.film_id = film_actor.film_id

join sakila.actor ON film_actor.actor_id = actor.actor_id

where film.rating = 'G'

and film.special_features like '%behind the scenes%'

and actor.actor_id = 15;

**6************************
select film.film_id, film.title, actor.actor_id, actor.first_name, actor.last_name from sakila.film

join sakila.film_actor on film.film_id = film_actor.film_id

join sakila.actor on actor.actor_id = film_actor.actor_id

where film.film_id = 369;

**7************************
select film.title, film.description, film.release_year, film.rating, film.special_features category_name from sakila.category

join sakila.film_category on film_category.category_id = category.category_id

join sakila.film on film.film_id = film_category.film_id

where film.rental_rate = 2.99;

**8************************
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name, 
       actor.first_name, actor.last_name from actor
join film_actor on actor.actor_id = film_actor.actor_id
join film on film_actor.film_id = film.film_id
join film_category ON film.film_id = film_category.film_id
join category on film_category.category_id = category.category_id
WHERE actor.first_name = 'Sandra'
and actor.last_name = 'Kilmer'
and category.name = 'Action';
