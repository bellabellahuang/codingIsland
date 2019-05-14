-- use IFF when there is only one condition to be validated for a column
SELECT
    video_id,
    channel_id,
    MAX(IFF(snapshot_id = '1', snapshot_data, NULL)) AS snapshot_1,
    MAX(IFF(snapshot_id = '2', snapshot_data, NULL)) AS snapshot_2,
    MAX(IFF(snapshot_id = '3', snapshot_data, NULL)) AS snapshot_3
FROM snapshots_table
GROUP BY video_id, channel_id;

-- use CASE if there are multiple conditions to be validated for a column
select
    column1,
    case
        when column1=1 then 'one'
        when column1=2 then 'two'
        else 'other'
    end as result
from (values(1),(2),(3)) v;