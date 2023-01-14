-- Calculates Students weighed average
-- creates the stored procedure

DELIMITER &&
DROP PROCEDURE
IF EXISTS ComputeAverageWeightedScoreForUser;

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
DECLARE sumAvg FLOAT;
SET sumAvg =  (
    SELECT AVG(score)
    FROM users
    JOIN corrections
    ON users.id = corrections.user_id
    JOIN projects
    ON corrections.project_id = projects.id
    WHERE users.id = user_id);
UPDATE users
SET average_score = sumAvg
WHERE id = user_id;
END &&
