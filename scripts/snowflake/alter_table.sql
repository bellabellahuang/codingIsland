-- add columns
ALTER TABLE [ IF EXISTS ] <name>
ADD COLUMN <col_name> <col_type>[, <col_name> <col_type> ...];

-- drop columns
ALTER TABLE [ IF EXISTS ] <name>
DROP [COLUMN] <col_name> [, <col_name> ...];