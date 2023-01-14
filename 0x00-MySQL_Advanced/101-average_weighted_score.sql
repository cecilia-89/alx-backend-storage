-- Calculates Students weighed average
-- creates the stored procedure

DELIMITER &&
DROP PROCEDURE
IF EXISTS ComputeAverageWeightedScoreForUser;

CREATE PROCEDURE ComputeAverageWeightedScoreForUser
BEGIN
DECLARE sumAvg FLOAT;
SET sumAvg =  (
  UPDATE users AS U,
  (SELECT U.id, SUM(score * weight) / SUM(weight) AS w_avg
  FROM users AS U
  JOIN corrections as C ON U.id=C.user_id
  JOIN projects AS P ON C.project_id=P.id
  GROUP BY U.id)
  AS WA
  SET U.average_score = WA.w_avg
  WHERE U.id=WA.id;
END &&
