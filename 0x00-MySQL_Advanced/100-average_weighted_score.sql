-- Write a SQL script that creates a stored procedure
-- ComputeAverageWeightedScoreForUser that computes and store
-- the average weighted score for a student.
-- Requirements:
--     Procedure ComputeAverageScoreForUser is taking 1 input:
--         user_id, a users.id value
--         (you can assume user_id is linked to an existing users)

DELIMITER $$
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN `user_id` INT)
BEGIN
    UPDATE users
    SET average_score = (SELECT SUM(corrections.score * projects.weight) / SUM(projects.weight)
        FROM corrections
        INNER JOIN projects
        ON projects.id = corrections.project_id
        WHERE corrections.user_id = user_id)
    WHERE users.id = user_id;
END $$
DELIMITER ;$$