
A = load 'msd/event-log/daily';

B = group A by song_id;

C = foreach B generate;

D = group A by artist_id;

E = foreach D generate;

store C into 'msd/event-log/daily-aggregate/song';

store E into 'msd/event-log/daily-aggregate/artist';


