# MusicBox - My project for Insight Data Engineering
#### The challenge is to build a report engine at scale for hundreds of concurrent events (*play, skip, thumbs-up, thumbs-dn*), for a music recommendation engine.
_Note: This project is very beta, and is being polished as we speak._

## Lots of moving parts
In order to create a mock Music Listening app, several parts of the puzzle were created from scratch.   
##### Software

* The general flow starts with an automated event generator which creates listen-events at random time intervals for a configurable number of active listeners (1-1000).  The python generator script sends a request to the webserver which uses nginx, uWSGI, Flask, and Bootstrap. 
* Kafka receives these messages, and once an hour a collector script stores them in HDFS.  Currently, Kafka is a single server.
* The Hadoop cluster contains one name node and three data nodes, all running on Ubuntu 12.10 64-bit.
* A python collector script is run every hour to take messages from Kafka and store them in HDFS.  
* Every night a Hive cron job aggregates the day's data and adds a row to the HBase event_log table.
* HBase is used as the NoSQL datastore and uses the same 4-node cluster as Hadoop
* Lastly, a second webserver is implemented to separate listener activity from report data requests.

##### Data
Several datasets were created with simulated data to create a historic timeline of users and events.  The Million Song Dataset was used as the music dataset.  

HBase Table | Description | Row Key
----------- | ----------- | --------
artist_info | Lookup table of artists by ARTIST_ID | AR87439FDL8349DF
artist_search | Search table of artists by ARTIST_NAME::ARTIST_ID | The Black Crows::AR3424FLDJ93F3
song_info | Lookup table of songs by TRACK_ID | TR343LDFKJ34881KF
song_search | Search table of songs by TITLE::TRACK_ID | Guero Canelo::TR3400FDKLJ3437KJ
user_info | List of users by USER_ID | 8c24dbaf-e50e-4b47-9fd6-da426752b6d4
artist_event_log | Historical event messages aggregated by day for a specific artist | AR3424FLDJ93F3_20140213
song_event_log | Historical event messages aggregated by day for a specific song | TR3400FDKLJ3437KJ_20130514


## Data Pipeline
![Data Pipeline](https://github.com/talldave/MusicBox/blob/master/WebServer/www/musicbox/slides/img/insight_data_pipeline.png "Data Pipeline")  
There are several flows of information here.  First, we have a number of listeners who make a request to the webserver.  This is for a specific user event: search, play, pause, skip, thumbs-up, thumbs-down, exit.   For search and play the request is sent directly to Hbase to retrieve the requested information (search results or mp3).  Playing an mp3 is not yet implemented, I will soon add a preview clip from 7digital.
In addition to contacting Hbase, and for all other requests, an event message is generated and sent to the Kafka message queue in JSON format.  

```JSON
{"timestamp": "Thu Dec 19 13:11:06 2013", "songid": "4ad8e5ac8c3ff7d706b3221d8692ceb2", "uid": "8c24dbaf-e50e-4b47-9fd6-da426752b6d4", "ip4": "248.132.126.127", "event": "tup"}
{"timestamp": "Thu Dec 19 13:18:14 2013", "songid": "323eeeea1d41be8f6f12fe28b9037d6c", "uid": "8c24dbaf-e50e-4b47-9fd6-da426752b6d4", "ip4": "248.132.126.127", "event": "play"} 
```   
At one-hour intervals, the messages from Kafka are loaded to Hadoop/HDFS.  At daily intervals, a Hive Map-Reduce program aggregrates that day's messages into a single day and adds them to the HBase:*event_log* table.

Secondly, we have users who request metric data from MusicBox.  These might be music promoters and accountants wanting to know how often a particular band or song is listened to.  Or, they might be advertisers wanting more information about the listeners in general, for a specific zipcode, or for a particular genre of music.  This request is sent to a separate Report-Engine web server which visualizes the aggregated HBase:*event_log* dataset.

## Challenges
## TODO
* Improve 'engineered data' to show natural rise and decline of interest in song/artist
* Implement funkload.py to stress test webapp against N users
* Write doc for API
* Complete UI for demo purposes
* Expand data input options (1-10 stars, text input, tags)
* Expand data capabilities (maps, sentiment analysis, listener collaboration)

## Changelog
Version 1.0 - Initial README
## In Action
You can see the web app in action at ...  
The report engine is [here](http://insight.davidbianco.net:8090/)
And the slides can be found [here](http://insight.davidbianco.net/slides) 

## About Me
http://davidbianco.net/about-me


