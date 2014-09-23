
set job.name 'specs-all.job';

base = load 'msd/source' using PigStorage('\t') 
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
base2 = foreach grouped generate COUNT(base) as count_all_rows;
store base2 into 'msd/static-all/count_total' using JsonStorage();

-- FILTER OUT NAN
filter_validvals = filter base by artist_familiarity != 'nan'
	and artist_hotttnesss != 'nan'
	and danceability != 'nan'
	and year != 'nan'
	and artist_longitude != 'nan'
	and artist_latitude != 'nan'
;
store filter_validvals into 'msd/static-all/valid_values' using PigStorage('\t');

-- COUNT ALL VALID VALUES
vv_group = group filter_validvals all;
vv_group_count = foreach vv_group generate COUNT(filter_validvals) as count_all_valid_rows;
store vv_group_count into 'msd/static-all/count_valid_values' using JsonStorage();

filter_vv_y0 = filter filter_validvals by year != 0;
group_fvv_y0 = group filter_vv_y0 all;
yearmin = foreach group_fvv_y0 generate MIN(filter_vv_y0.year) as min_year;
store yearmin into 'msd/static-all/minyear' using JsonStorage();

-- MIN MAX
minmax = foreach vv_group generate group, MIN(filter_validvals.artist_familiarity) as min_famil, MAX(filter_validvals.artist_familiarity) as max_famil
	,MIN(filter_validvals.artist_hotttnesss) as min_hottt, MAX(filter_validvals.artist_hotttnesss) as max_hottt
	,MIN(filter_validvals.danceability) as min_dance, MAX(filter_validvals.danceability) as max_dance
	,MIN(filter_validvals.year) as min_year, MAX(filter_validvals.year) as max_year
	,MIN(filter_validvals.artist_longitude) as minx,MIN(filter_validvals.artist_latitude) as miny
	,MAX(filter_validvals.artist_longitude) as maxx,MAX(filter_validvals.artist_latitude) as maxy
;
store minmax into 'msd/static-all/minmax' using JsonStorage();


-- COUNT NAN GEO
-- base_geo = filter base by artist_latitude != 'nan' and artist_longitude != 'nan';
-- base_geo_group_all = group base_geo all;
-- base3 = foreach base_geo_group_all generate COUNT(base_geo) as count;
-- dump base3;
-- store base3 into 'msd/static/count_geo' using JsonStorage();
-- minmax_geo = foreach base_geo_group_all generate
	-- MIN(base_geo.artist_longitude) as minx,MIN(base_geo.artist_latitude) as miny,MAX(base_geo.artist_longitude) as maxx,MAX(base_geo.artist_latitude) as maxy
-- ;
-- store minmax_geo into 'msd/static/minmax_geo' using JsonStorage();

-- COUNT DECADES

-- # END # --

