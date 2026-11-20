-- Day 09: SCD Type 2 with MERGE in Delta
-- TEST before publishing: run the three cases at the bottom of this file.

CREATE OR REPLACE TABLE dim_customer (
  customer_id BIGINT,
  city STRING,
  row_hash STRING,
  start_date DATE,
  end_date DATE,
  is_current BOOLEAN
);

-- Staging with a hash of the tracked columns.
CREATE OR REPLACE TEMP VIEW stg_customer AS
SELECT customer_id, city, sha2(concat_ws('||', city), 256) AS row_hash
FROM raw_customer;

MERGE INTO dim_customer t
USING (
  -- 1) Real key: closes the current row if something changed.
  SELECT customer_id AS merge_key, customer_id, city, row_hash
  FROM stg_customer
  UNION ALL
  -- 2) NULL key: never matches, so the new version gets inserted.
  SELECT NULL, s.customer_id, s.city, s.row_hash
  FROM stg_customer s
  JOIN dim_customer d
    ON s.customer_id = d.customer_id AND d.is_current
  WHERE s.row_hash <> d.row_hash
) u
ON t.customer_id = u.merge_key AND t.is_current
WHEN MATCHED AND t.row_hash <> u.row_hash THEN
  UPDATE SET is_current = false, end_date = current_date()
WHEN NOT MATCHED THEN
  INSERT (customer_id, city, row_hash, start_date, end_date, is_current)
  VALUES (u.customer_id, u.city, u.row_hash, current_date(), NULL, true);

-- Test cases (load raw_customer, run the MERGE twice, check the result):
--   Run 1: (1, 'Bogota'), (2, 'Medellin')               -> 2 current rows
--   Run 2: (1, 'Cali'),   (2, 'Medellin'), (3, 'Lima')
--     customer 1: old row closed + new current row       (changed)
--     customer 2: untouched                              (no change)
--     customer 3: inserted as current                    (new)
SELECT * FROM dim_customer ORDER BY customer_id, start_date;
