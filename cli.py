from reso import Client
import click
import os

@click.command()
@click.option("-u", "--username", prompt="Enter username", required=True)
@click.option("-p", "--password", prompt="Enter password", required=True)
@click.option("-n", "--notes", required=True, help="A notes.txt file which creates a notes/ folder and saves all pdf inside.")
def run(username, password, notes):
    if os.path.exists(notes.replace('.txt', '')) == False:
        os.mkdir(notes.replace('.txt', ''))
    client = Client()
    client.login(username, password)
    note_ids = []
    with open(notes, 'r') as note_file:
        for url in note_file:
            note_ids.append(client.get_note_id(url))
    
    print("Downloading Notes...")
    for note_id in note_ids:
        client.download(note_id, notes.replace('.txt', ''))
    print("Done!!!")

if __name__ == "__main__":
    run()