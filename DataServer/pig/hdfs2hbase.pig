
set job.name 'copy-valid2hbase.job';

base = load 'msd/static-all/valid_values' using PigStorage('\t') 
as (
track_id,analysis_sample_rate,artist_7digitalid,artist_familiarity,artist_hotttnesss
,artist_id,artist_latitude,artist_location,artist_longitude,artist_mbid
,artist_mbtags,artist_mbtags_count,artist_name,artist_playmeid,artist_terms
,artist_terms_freq,artist_terms_weight,audio_md5,bars_confidence,bars_start
,beats_confidence,beats_start,danceability,duration,end_of_fade_in
,energy,key,key_confidence,loudness,mode
,mode_confidence,release,release_7digitalid,sections_confidence,sections_start
,segments_confidence,segments_loudness_max,segments_loudness_max_time,segments_loudness_max_start,segments_pitches
,segments_start,segments_timbre,similar_artists,song_hotttnesss,song_id
,start_of_fade_out,tatums_confidence,tatums_start,tempo,time_signature
,time_signature_confidence,title,track_7digitalid,year);


base1 = foreach base generate
    track_id,artist_familiarity,artist_hotttnesss
    ,artist_id,artist_latitude,artist_location,artist_longitude,
    artist_name,artist_terms,
    artist_terms_freq,artist_terms_weight
    ,danceability,duration
    ,energy
    ,release
    ,similar_artists,song_hotttnesss
    ,title,track_7digitalid,year;


T = STORE base1 INTO 'hbase://song_info' USING org.apache.pig.backend.hadoop.hbase.HBaseStorage('info:*');

-- # END # --

