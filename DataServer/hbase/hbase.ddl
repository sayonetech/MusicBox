CREATE TABLE
msd_valids (track_id STRING, c1 STRING, c2 STRING)
STORED BY 'org.apache.hcatalog.hbase.HBaseHCatStorageHandler'
TBLPROPERTIES (
  'hbase.table.name' = 'msd_valids',
  'hbase.columns.mapping' = 'd:c1,d:c2',
  'hcat.hbase.output.bulkMode' = 'true'
);

