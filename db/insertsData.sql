
insert into schedule (start_time, end_time)
values ('9:00:00', '16:00:00'),
 ('9:00:00', '14:00:00');



insert into faculty (name, reception_interval_in_minutes)
values('Економ', '00-15-00'),
('Юрфак', '00-15-00'),
('ФИПТ', '00-15-00'),
('Истфак', '00-15-00'),
('ФИЯ', '00-15-00'),
('ФХББ', '00-15-00'),
('Филфак', '00-15-00');


insert into commission (name)
values
('Бакалавры пзсо'),
('Магистры'),
('Бакалавры МС');

insert into commission_faculty (commission_id, faculty_id, id)
values
(1, 1, 1),
(1, 2, 2),
(1, 3, 3),
(1, 4, 4),
(1, 5, 5),
(1, 6, 6),
(1, 7, 7),

(2, 1, 8),
(2, 2, 9),
(2, 3, 10),
(2, 4, 11),
(2, 5, 12),
(2, 6, 13),
(2, 7, 14),

(3, 1, 15),
(3, 3, 16),
(3, 6, 17),
(3, 7, 18);

insert into custom_schedule (date, schedule_id, commission_id)
values
('2020:08:24', 1, 2),
('2020:08:25', 1, 2),
('2020:08:26', 1, 2),
('2020:08:27', 1, 2),
('2020:08:28', 1, 2),
('2020:08:29', 2, 2),
('2020:08:31', 1, 2),
('2020:09:01', 1, 2),
('2020:09:02', 1, 2),
('2020:09:03', 1, 2),
('2020:09:04', 1, 2),
('2020:09:05', 2, 2),
('2020:09:07', 1, 2),
('2020:09:08', 1, 2),
('2020:09:09', 1, 2),
('2020:09:10', 1, 2),
('2020:09:11', 1, 2),
('2020:09:12', 2, 2),
('2020:09:14', 1, 2),
('2020:09:15', 1, 2),
('2020:09:16', 1, 2),
('2020:09:17', 1, 2),
('2020:09:18', 1, 2),

('2020:08:24', 1, 1),
('2020:08:25', 1, 1),
('2020:08:26', 1, 1),
('2020:08:27', 1, 1),
('2020:08:28', 1, 1),
('2020:08:29', 2, 1),
('2020:08:31', 1, 1),
('2020:09:01', 1, 1),
('2020:09:02', 1, 1),
('2020:09:03', 1, 1),
('2020:09:04', 1, 1),
('2020:09:05', 2, 1),
('2020:09:07', 1, 1),
('2020:09:08', 1, 1),
('2020:09:09', 1, 1),
('2020:09:10', 1, 1),
('2020:09:11', 1, 1),
('2020:09:12', 2, 1),
('2020:09:14', 1, 1),
('2020:09:15', 1, 1),
('2020:09:16', 1, 1),
('2020:09:17', 1, 1),
('2020:09:18', 1, 1),
('2020:09:19', 2, 1),
('2020:09:21', 1, 1),
('2020:09:22', 1, 1),
('2020:09:23', 1, 1),
('2020:09:24', 1, 1),
('2020:09:25', 1, 1),
('2020:09:26', 2, 1),
('2020:09:28', 1, 1),
('2020:09:29', 1, 1),

('2020:08:24', 1, 3),
('2020:08:25', 1, 3),
('2020:08:26', 1, 3),
('2020:08:27', 1, 3),
('2020:08:28', 1, 3),
('2020:08:29', 2, 3),
('2020:08:31', 1, 3),
('2020:09:01', 1, 3),
('2020:09:02', 1, 3),
('2020:09:03', 1, 3),
('2020:09:04', 1, 3),
('2020:09:05', 2, 3),
('2020:09:07', 1, 3),
('2020:09:08', 1, 3),
('2020:09:09', 1, 3),
('2020:09:10', 1, 3),
('2020:09:11', 1, 3),
('2020:09:12', 2, 3),
('2020:09:14', 1, 3),
('2020:09:15', 1, 3),
('2020:09:16', 1, 3),
('2020:09:17', 1, 3),
('2020:09:18', 1, 3),
('2020:09:19', 2, 3),
('2020:09:21', 1, 3),
('2020:09:22', 1, 3),
('2020:09:23', 1, 3),
('2020:09:24', 1, 3),
('2020:09:25', 1, 3),
('2020:09:26', 2, 3),
('2020:09:28', 1, 3),
('2020:09:29', 1, 3);

