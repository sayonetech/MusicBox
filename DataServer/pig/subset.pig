
set job.name 'specs-all.job';

base = load 'msd/source/D.tsv.b' using PigStorage('\t') 
as (
track_id ,analysis_sample_rate ,artist_7digitalid ,artist_familiarity ,artist_hotttnesss
,artist_id ,artist_latitude ,artist_location ,artist_longitude ,artist_mbid
,artist_mbtags ,artist_mbtags_count ,artist_name ,artist_playmeid ,artist_terms
,artist_terms_freq ,artist_terms_weight ,audio_md5 ,bars_confidence ,bars_start
,beats_confidence ,beats_start ,danceability ,duration ,end_of_fade_in
,energy ,key ,key_confidence ,loudness ,mode
,mode_confidence ,release ,release_7digitalid ,sections_confidence ,sections_start
,segments_confidence ,segments_loudness_max ,segments_loudness_max_time ,segments_loudness_max_start ,segments_pitches
,segments_start ,segments_timbre ,similar_artists ,song_hotttnesss ,song_id
,start_of_fade_out ,tatums_confidence ,tatums_start ,tempo ,time_signature
,time_signature_confidence ,title ,track_7digitalid ,year);


-- FILTER OUT NAN
-- filter_validvals = filter base by artist_familiarity != 'nan'
f2 = filter base by artist_familiarity != 'nan'
	and artist_hotttnesss != 'nan'
	and danceability != 'nan'
	and year != 'nan'
	and artist_longitude != 'nan'
	and artist_latitude != 'nan'
;
-- f2 = limit filter_validvals 4000;
-- store f2 into 'msd/static-all/valid_subset' using PigStorage('\t');
STORE f2 INTO 'hbase://song_subset' USING org.apache.pig.backend.hadoop.hbase.HBaseStorage('info:*');


-- # END # --

