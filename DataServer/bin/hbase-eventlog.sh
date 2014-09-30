
hbase org.apache.hadoop.hbase.mapreduce.ImportTsv -Dimporttsv.columns=HBASE_ROW_KEY,info:song_id,info:date,info:play_count,info:tup_count,info:tdn_count,info:skip event_log_songs msd/static-all/event-log-hist-songs

echo "*NEXT*"

hbase org.apache.hadoop.hbase.mapreduce.ImportTsv -Dimporttsv.columns=HBASE_ROW_KEY,info:artist_id,info:date,info:play_count,info:tup_count,info:tdn_count,info:skip event_log_arists msd/static-all/event-log-hist-artist



