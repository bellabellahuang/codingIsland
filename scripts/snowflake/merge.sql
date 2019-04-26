# tableA is the table with latest records
# tableB is the table with new/updated records
MERGE INTO tableA
USING (SELECT * FROM tableB)
ON tableA.id = tableB.id
    when matched then update set tableA.name = tableB.name
    when not matched then insert (id, name) values (tableB.id, tableB.name);