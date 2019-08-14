# convert string to datetime
select to_timestamp('2015/12/18 03:15:17', 'YYYY/MM/DD HH24:MI:SS');

# define datetime format for the input field in the file format
COPY INTO my_table
FROM (
  SELECT *
  FROM @my_stage
)
FILE_FORMAT = (
  TYPE = CSV
  COMPRESSION = GZIP
  SKIP_HEADER = 1
  FIELD_OPTIONALLY_ENCLOSED_BY = '"'
  ESCAPE_UNENCLOSED_FIELD = NONE
  ENCODING = UTF8
  TIMESTAMP_FORMAT = 'YYYY/MM/DD HH24:MI:SS'
)