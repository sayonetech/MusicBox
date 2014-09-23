
set job.name 'specs-all.job';

-- base = load 'msd/source' using PigStorage('\t') 
base = load 'msd/static-all/valid_values' using PigStorage('\t') 
-- base = load 'msd/source/A.*' using PigStorage('\t') 
-- base = load 'msd/source/A.tsv.a' using PigStorage('\t') 
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

-- base1 = foreach base generate
	-- artist_id,
	-- artist_latitude,
	-- artist_longitude
	-- (double) $7 as lat
	-- ,(double) $9 as lon
	 --,COUNT(track_id) as num_rows
-- ;
-- dump base1;
-- test = foreach base generate MIN(artist_familiarity) as min_famil;
-- store test into 'msd/static/min-famil-test1' using PigStorage();

grouped = group base all;

-- COUNT ALL ROWS
base2 = foreach grouped generate COUNT(base) as count_valid_rows;
store base2 into 'msd/static-all/count_valid_values' using JsonStorage();

-- MIN MAX
-- minmax = foreach vv_group generate group, MIN(filter_validvals.artist_familiarity) as min_famil, MAX(filter_validvals.artist_familiarity) as max_famil
	-- ,MIN(filter_validvals.artist_hotttnesss) as min_hottt, MAX(filter_validvals.artist_hotttnesss) as max_hottt
	-- ,MIN(filter_validvals.danceability) as min_dance, MAX(filter_validvals.danceability) as max_dance
	-- ,MIN(filter_validvals.year) as min_year, MAX(filter_validvals.year) as max_year
	-- ,MIN(filter_validvals.artist_longitude) as minx,MIN(filter_validvals.artist_latitude) as miny
	-- ,MAX(filter_validvals.artist_longitude) as maxx,MAX(filter_validvals.artist_latitude) as maxy
-- ;
-- store minmax into 'msd/static-all/minmax' using JsonStorage();


-- COUNT DECADES

-- # END # --

