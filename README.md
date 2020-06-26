# Onlinereso Downloader

A cli tool to download notes/pdf from onlinereso.in

# Instructions

- install requirements

```sh
$ pip install -r requirements.txt
```

<hr>

## Notes setup

- here is an example of `maths.txt`

```sh
$ cat maths.txt                              
https://onlinereso.in/note/9280
https://onlinereso.in/note/9369
https://onlinereso.in/note/9271
https://onlinereso.in/note/9273
https://onlinereso.in/note/9272
https://onlinereso.in/note/9254
```
**NOTE**: Save `notes.txt` with url of note

# Downloading

1. Get your username and password
2. pass username, password and notes file through `cli.py`

```sh
$ python cli.py --username 1234 --password 1234 --notes maths.txt
```
It will save notes in `maths` named folder. Inside that all your notes will be there with `note_id.pdf`
