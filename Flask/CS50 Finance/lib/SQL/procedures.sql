CREATE PROCEDURE calculate total_value(vID) RETURN REAL AS
BEGIN

    /************ calculate_total********************'
            Calculates the total of stock_value and
            cash value.

    *****************************************************************/

    --  Declare variables
    DECLARE cash REAL;
    DECLARE endloop TINYINT;
    DECLARE stock_value REAL;

    --  Initializing the declared variable

    SET cash = SELECT cash FROM users WHERE id = vID;
    SET stock_value = SELECT stock_value FROM users WHERE id = vID;

    RETURN cash + stock_value;
END;
