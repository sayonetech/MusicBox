
set job.name 'job-songsearch';

base = load 'msd/static-all/songs_20cols' using PigStorage('\t') as (
    track_id:chararray,artist_familiarity:chararray,artist_hotttnesss:chararray,
    artist_id:chararray,artist_latitude:chararray,artist_location:chararray,artist_longitude:chararray,
    artist_name:chararray,artist_terms:chararray,
    artist_terms_freq:chararray,artist_terms_weight:chararray,danceability:chararray,
    duration:chararray,energy:chararray,release:chararray,similar_artists:chararray,
    song_hotttnesss:chararray,title:chararray,track_7digitalid:chararray,year:chararray);

base1 = foreach base generate CONCAT(artist_name,'::',track_id) as comp_key,
    track_id,artist_familiarity,artist_hotttnesss
    ,artist_id,artist_latitude,artist_location,artist_longitude,
    artist_name,artist_terms,
    artist_terms_freq,artist_terms_weight
    ,danceability,duration
    ,energy
    ,release
    ,similar_artists,song_hotttnesss
    ,title,track_7digitalid,year;

store base1 into 'msd/static-all/songsearch' using PigStorage('\t');

-- T = STORE base1 INTO 'hbase://song_info' USING org.apache.pig.backend.hadoop.hbase.HBaseStorage('info:*');

-- # END # --

