Write SQL to get the output for this Input data as shown below
Table-fund_investment
+--------------------------------------------------+
| Fundid | Allocation type | Allocation Percentage | 
| 2342   | BOND            | 0.2                    
| 2342   | CASH            | 0.7                   | 
| 2342   | CTSK            | 0.1                   |   
+--------------------------------------------------+
Table-participant
+------------------------------+
| Part_id  | Fundid | Balance |  
|----------|--------|----------|
| 34546778 | 2342   | 5000     | ---  
| 11254678 | 2342   | 50000    |
+------------------------------+
Table-output
+---------------------------------------------------------------------------+
| Part_id  | Fundid | Balance | Bond Balance | Cash Balance | Stock Balance | 
|----------|--------|---------|--------------|--------------|---------------| 
| 34546778 | 2342   | 5000    | 1000         | 3500         | 500           | 
| 11254678 | 2342   | 50000   | 10000        | 35000        | 5000          |
+---------------------------------------------------------------------------+

select 
b.*,case when b.allocation_type = "BOND" then a.balance*b.allocationper end as Bond_balance,
case when allocation_type = "CASH" then a.balance*b.allocationper end as cash_balance,
allocation_type = "CTSK" then a.balance*b.allocationper end as stock_balance
from 
fund_investment a,
participant b
where a.Fundid = b.Fundid


34556778 2342  5000 1000 0 0
34546778 | 2342 50000 0 3500 0
34546778 | 2342 0 0 500



