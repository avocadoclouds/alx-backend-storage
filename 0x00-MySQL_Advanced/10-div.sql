-- Write a SQL script that creates a function SafeDiv that divides
-- (and returns) the first by the second number
-- or returns 0 if the second number is equal to 0.
-- Requirements:
--     You must create a function
--     The function SafeDiv takes 2 arguments:
--         a, INT
--         b, INT
--     And returns a / b or 0 if b == 0


DELIMITER $$
CREATE FUNCTION SafeDiv(
	a INTEGER,
    b INTEGER
) 
RETURNS FLOAT
DETERMINISTIC
BEGIN
    DECLARE res FLOAT;
    IF b = 0 THEN
        SET res = 0;
    ELSE
        SET res = (a * 1.0) / b;
    END IF;
	RETURN (res);
END $$
DELIMITER ;