# Generating Recs from Data

After the Similar Product Engine is built, the system enters model training, and subsequent serving functionality. 

Formally, the commands for this process in PredictionIO are:

```
pio build --verbose
pio train
pio deploy
```

To generate recommendations for completing a user's playlist, the system uses the pattern below. 

### query for completing the playlist:

```
curl -H "Content-Type: application/json" \
-d '{"items": ["spotify:track:6za48riBTylMJHsf4AJPxK"], 
"num": 500, 
"categories": ["Hollywood: A Story of a Dozen Roses (Deluxe Version)","spotify:album:79EyqF9taW9XFPKci2U5D9","spotify:track:6za48riBTylMJHsf4AJPxK","Ride out","spotify:artist:7LnaAXbDVIL75IVPnndf7w","Jamie Foxx","You Changed Me"], 
"blackList": ["spotify:track:6za48riBTylMJHsf4AJPxK"]}' \
http://localhost:8000/queries.json \

```

### Elements defined

items = spotify track uris that are already in the playlist

num = 500 tracks to complete the playlist

categories = selected metadata from the playlist, including the following rows : playlist_name, album_uri, artist_uri, track_name, album_name, artist_name, track_uri

blacklist = spotify track uris that are already in the playlist

# System Memory  

## The following memory flags were used in model training:

```
pio train -- --conf spark.network.timeout=10000000 --master local --driver-memory 300G --executor-memory 300G --conf spark.executor.heartbeatInterval=10000000

```

The resulting trained model was too large to query from PostgreSQL, so rather than storing the model relationally, it is stored in the local file system, by modifying the system settings within the PredictionIO configuration.

## To serve the model

```
pio deploy -- --driver-memory 300G
```
## Playlists with no tracks

The spotify recommendation challenge included 1,000 playlists with no tracks. For the creative track a reverse indexing approach was used to infer likely tracks from the available data by way of a playlist name. 

Tracks from the training data which had used the same playlist name or similar playlist name as the challenge set were identified; those tracks were then used for generating recommendations. The system used the playlist name as a category in the query pattern described above. 

 Note that challenge data was used in creating about half of this reverse index, since the creative track allowed for the use of openly available datasets.

