-- aggregate report_type by partner_id using '|' as the delimeter
-- i.e. a|b|c
SELECT partner_id, LISTAGG(report_type, '|') within GROUP (ORDER BY partner_id) AS report_list
FROM table
GROUP BY partner_id;