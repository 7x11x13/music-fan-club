#!/usr/bin/env python3
import json
import subprocess

url = "https://www.youtube.com/playlist?list=PLr9e7ejE5Qjmz0CPtB2uceFwHr3ncdlv1"
output = subprocess.check_output(["yt-dlp", "-j", "--flat-playlist", url])
playlist = "playlistVideos = [\n"
for line in output.decode('utf-8').split('\n'):
    if line:
        video = json.loads(line)
        title = video['title'].replace("'", "\\'")
        playlist += f"    {{id: '{video['id']}', title: '{title}'}},\n"
playlist += "];\n"
playlist += """function shuffle(array) {
    let currentIndex = array.length
    while (currentIndex != 0) {
        const randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex--;
        [array[currentIndex], array[randomIndex]] = [array[randomIndex], array[currentIndex]];
    }
    return array;
}
shuffle(playlistVideos);"""
with open("playlist.js", "w", encoding="utf-8") as f:
    f.write(playlist)
