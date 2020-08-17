
CREATE TABLE IF NOT EXISTS `student` (
  `name` varchar(100) not null,
  `email` varchar(150) not null,
  `id` serial,
  PRIMARY KEY (`id`),
  unique (`email`)
);

CREATE TABLE IF NOT EXISTS `schedule` (
  `start_time` time not null,
  `end_time` time not null,
  `id` SERIAL,
  PRIMARY KEY (`id`),
  unique (`start_time`, `end_time`)
);


CREATE TABLE IF NOT EXISTS `custom_schedule` (
  `id` serial,
  `date` date not null,
  `schedule_id` bigint UNSIGNED not null,
  `commission_id` bigint UNSIGNED not null,
  PRIMARY KEY (`id`),
  unique (`date`),
  foreign key (`schedule_id`)
    references `schedule` (`id`) on delete restrict on update cascade
);

CREATE TABLE IF NOT EXISTS `faculty` (
  `name` varchar(200) not null,
  `reception_interval_in_minutes` varchar(150) not null,
  `id` serial,
  PRIMARY KEY (`id`),
  unique(`name`)
);

CREATE TABLE IF NOT EXISTS `commission` (
  `name` varchar(100) not null,
  `id` serial,
  PRIMARY KEY (`id`),
  unique (`name`),

);


CREATE TABLE IF NOT EXISTS `commission_faculty` (
  `id` serial,
  `faculty_id` bigint UNSIGNED not null,
  `commission_id` bigint UNSIGNED not null,
  PRIMARY KEY (`id`),
  unique (`commission_id`, `faculty_id`),
  foreign key (`faculty_id`)
    references `faculty` (`id`) on delete restrict on update cascade,
  foreign key (`commission_id`)
    references `commission` (`id`) on delete restrict on update cascade
);


CREATE TABLE IF NOT EXISTS `form` (
  `submit_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `preferred_time` date not null,
  `preferred_date` time not null,
  `commission_id` bigint UNSIGNED not null,
  `student_id` bigint UNSIGNED not null,
  `id` serial,
  unique(`student_id`, `commission_id`),
  PRIMARY KEY (`id`),
  foreign key (`commission_id`)
    references `commission` (`id`) on delete restrict on update cascade,
  foreign key (`student_id`)
    references `student` (`id`) on delete restrict on update cascade
);


