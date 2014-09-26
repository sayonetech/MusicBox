
hbase org.apache.hadoop.hbase.mapreduce.ImportTsv -Dimporttsv.columns=HBASE_ROW_KEY,info:track_id,info:artist_familiarity,info:artist_hotttnesss,info:artist_id,info:artist_latitude,info:artist_location,info:artist_longitude,info:artist_name,info:artist_terms,info:artist_terms_freq,info:artist_terms_weight,info:danceability,info:duration,info:energy,info:release,info:similar_artists,info:song_hotttnesss,info:title,info:track_7digitalid,info:year artist_search msd/static-all/artistsearch

echo "*NEXT*"

hbase org.apache.hadoop.hbase.mapreduce.ImportTsv -Dimporttsv.columns=HBASE_ROW_KEY,info:track_id,info:artist_familiarity,info:artist_hotttnesss,info:artist_id,info:artist_latitude,info:artist_location,info:artist_longitude,info:artist_name,info:artist_terms,info:artist_terms_freq,info:artist_terms_weight,info:danceability,info:duration,info:energy,info:release,info:similar_artists,info:song_hotttnesss,info:title,info:track_7digitalid,info:year song_search msd/static-all/songsearch


