-- Day 06: ZORDER vs Liquid Clustering
-- VERIFY runtime requirements for Liquid Clustering in your Databricks version.

-- Before: partitioning + ZORDER (keys are hard to change later)
CREATE TABLE sales_legacy (id BIGINT, country STRING, sale_date DATE)
PARTITIONED BY (country);

OPTIMIZE sales_legacy ZORDER BY (sale_date);

-- After: Liquid Clustering (replaces partitioning and ZORDER, do not combine them)
CREATE TABLE sales (id BIGINT, country STRING, sale_date DATE)
CLUSTER BY (country, sale_date);

OPTIMIZE sales;

-- Query pattern changed? Change the clustering keys without recreating the table.
ALTER TABLE sales CLUSTER BY (id);

-- Check the current clustering columns.
DESCRIBE DETAIL sales;
