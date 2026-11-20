-- Day 14: Unity Catalog governance basics
-- VERIFY row filter / column mask availability in your edition and region.

-- Three-level namespace: catalog.schema.table
CREATE CATALOG IF NOT EXISTS main;
CREATE SCHEMA IF NOT EXISTS main.sales;

-- Permissions are inherited down the hierarchy.
GRANT USE CATALOG ON CATALOG main TO `data-analysts`;
GRANT USE SCHEMA ON SCHEMA main.sales TO `data-analysts`;
GRANT SELECT ON TABLE main.sales.orders TO `data-analysts`;

-- Column mask: hide a sensitive column from everyone outside a group.
CREATE OR REPLACE FUNCTION main.sales.mask_email(email STRING)
RETURN CASE WHEN is_account_group_member('pii-readers') THEN email ELSE '***' END;

ALTER TABLE main.sales.customers ALTER COLUMN email SET MASK main.sales.mask_email;

-- Row filter: each group only sees its region.
CREATE OR REPLACE FUNCTION main.sales.region_filter(region STRING)
RETURN is_account_group_member('admins') OR is_account_group_member(concat('region-', region));

ALTER TABLE main.sales.orders SET ROW FILTER main.sales.region_filter ON (region);

-- Audit: who accessed what (system tables must be enabled).
SELECT event_time, user_identity.email, action_name, request_params
FROM system.access.audit
WHERE service_name = 'unityCatalog'
ORDER BY event_time DESC
LIMIT 100;
