

use twitter; 
select * from users;
select handle from users where users.id = 2;

insert into follows (followed_id, follower_id, created_at, updated_at) values (2, 3, now(), now());

delete from users where id = 2;

update users set handle = 'Big Bird' where id = 2;
