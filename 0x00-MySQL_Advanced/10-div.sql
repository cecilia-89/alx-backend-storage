-- SQL functions: Safe Divide
-- function that returns dividend
DELIMITER //
CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS FLOAT
DETERMINISTIC
BEGIN
IF b = 0 THEN
RETURN 0;
END IF;
RETURN (a * 1.0) / b;
END //
