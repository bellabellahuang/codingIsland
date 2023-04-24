# import data from external stage
COPY INTO {table_name} 
    FROM @{stage}/{file_path}
    FILE_FORMAT = (
      TYPE = 'CSV'
      COMPRESSION = GZIP
      FIELD_OPTIONALLY_ENCLOSED_BY = '"'
      ESCAPE_UNENCLOSED_FIELD = NONE
      ENCODING = UTF8
      SKIP_HEADER = 1
    )
    PURGE = TRUE; # delete the files in external stage after import

# export data from table to external stage
COPY INTO @{stage}/{file_path}/{file_name}.csv.gz
    FROM (
        SELECT * FROM {table_name})
    FILE_FORMAT = (
      TYPE = CSV
      COMPRESSION = GZIP
      FIELD_OPTIONALLY_ENCLOSED_BY = '"'
      ESCAPE_UNENCLOSED_FIELD = NONE
      ESCAPE = '"'
      NULL_IF = ('')
    )
    SINGLE = TRUE
    HEADER = TRUE
    OVERWRITE = TRUE
    MAX_FILE_SIZE = 5368709120;
