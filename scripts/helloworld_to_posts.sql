insert into posts_topic (name,description,created_date,updated_date) select * from helloworld_topic;
insert into posts_post (title,text,created_date,published_date,topic_name_id) select * from helloworld_post;
DROP TABLE helloworld_post;
DROP TABLE helloworld_topic;