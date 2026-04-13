USE project;

-- SELECT * from accountinfo;

-- SELECT * FROM transactions WHERE transactionNumber = 1;

-- UPDATE transactions
-- SET amount = 16.66
-- WHERE transactionNumber = 1;

-- SELECT * FROM transactions WHERE transactionNumber = 1;

SELECT * FROM transactions;
SELECT * FROM accountinfo;

DELETE FROM transactions WHERE transactionNumber = 63;
DELETE FROM accountinfo WHERE accountNumber = 8231;

SELECT * FROM transactions;
SELECT * FROM accountinfo;