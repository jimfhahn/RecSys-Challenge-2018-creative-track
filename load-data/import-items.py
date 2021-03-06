import csv
import predictionio
import argparse

def import_events(client):
    print(client.get_status())
    print("Importing data...")

    with open('/home/new-home/creative-track/creative-spotify-corpus-50.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            track_parsed_csv = (row['track_uri'])
            categories_parsed_csv = (row['playlist_name']), (row['album_uri']), (row['artist_uri']), (row['artist_name']), (row['related_artist'])
            # push the items into the database
            categories = categories_parsed_csv
            item_ids = [track_parsed_csv]
            for item_id in item_ids:
                print("Set item", item_id)
                client.create_event(
                    event="$set",
                    entity_type="item",
                    entity_id=item_id,
                    properties={
                        "categories": categories
                    }
                )


if __name__ == '__main__':
        parser = argparse.ArgumentParser(
            description="Import sample data for similar product engine")
        parser.add_argument('--access_key', default='')
        parser.add_argument('--url', default="http://localhost:7070")

        args = parser.parse_args()
        print(args)

        client = predictionio.EventClient(
            access_key=args.access_key,
            url=args.url,
            threads=100,
            qsize=0)
        import_events(client)
