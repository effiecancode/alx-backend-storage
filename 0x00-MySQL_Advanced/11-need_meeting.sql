-- Script that creates a view need_meeting thats lists all students
-- that have a score under 80 (strict) and not last_meeting or more than 1 months
CREATE VIEW need_meeting AS SELECT name from students WHERE score < 80
AND (last_meeting IS NULL OR last_meeting < DATE(CURDATE() - INTERVAL 1 MONTH));
