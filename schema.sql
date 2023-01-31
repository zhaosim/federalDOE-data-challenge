drop table if exists Person;

create table `Person` (
  `person_id` int not null auto_increment,
  `given_name` varchar(80) default null,
  `family_name` varchar(80) default null,
  `date_of_birth` datetime default null,
  `place_of_birth` varchar(80) default null,
  primary key (`person_id`)
);

drop table if exists Place;

create table `Place` (
  `place_id` int not null auto_increment,
  `city` varchar(80) default null,
  `county` varchar(80) default null,
  `country` varchar(80) default null,
  primary key (`place_id`)
);