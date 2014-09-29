# MusicBox
#### The challenge is to build a report engine at scale for hundreds of concurrent events (*play, skip, thumbs-up*), for a music recommendation engine.
<Note: This project is very beta, and is being polished as we speak.>

## Lot of moving parts
## Data Pipeline
![Alt Text](https://github.com/talldave/MusicBox/blob/master/WebServer/www/musicbox/slides/img/insight_data_pipeline.png "Data Pipeline")  
There are several flows of information here.  First, we have a number of listeners who make a request to the webserver.  This is for a specific user event: search, play, pause, skip, thumbs-up, thumbs-down, exit.   For search and play the request is sent directly to Hbase retrieve the requested information (search results or mp3).  Playing an mp3 is not yet implemented, I will soon add a preview clip from 7digital.
In addition to contacting Hbase, and for all other requests, an event message is generated and sent to the Kafka message queue in JSON format.  
``` {"timestamp": "Thu Dec 19 13:11:06 2013", "songid": "4ad8e5ac8c3ff7d706b3221d8692ceb2", "uid": "8c24dbaf-e50e-4b47-9fd6-da426752b6d4", "ip4": "248.132.126.127", "event": "tup"}
{"timestamp": "Thu Dec 19 13:18:14 2013", "songid": "323eeeea1d41be8f6f12fe28b9037d6c", "uid": "8c24dbaf-e50e-4b47-9fd6-da426752b6d4", "ip4": "248.132.126.127", "event": "play"} ```   
At one-hour intervals, the messages from Kafka are loaded to Hadoop/HDFS.  At daily intervals, a Hive Map-Reduce program aggregrates that day's messages into a single day and adds them to the HBase:*event_log* table.

Secondly, we have users who request metric data from MusicBox.  These might be music promoters and accountants wanting to know how often a particular band or song is listened to.  Or, they might be advertisers wanting more information about the listeners in general, for a specific zipcode, or for a particular genre of music.  This request is sent to a separate Report-Engine web server which visualizes the aggregated HBase:*event_log* dataset.

## Challenges
## TODO
## Changelog
Version 1.0 - Initial README
## In Action
You can see the web app in action at ...  
The report engine is here ...  
And the slides can be found here ...  

