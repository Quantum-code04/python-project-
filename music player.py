import os
import pygame
from tkinter import Tk, Frame, Label, Button, Listbox, Scrollbar, filedialog

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        master.title("Music Player")
        self.playlist = []
        self.current_index = 0

        self.frame = Frame(master)
        self.frame.pack()

        self.song_label = Label(self.frame, text="No song playing")
        self.song_label.pack()

        self.playlist_box = Listbox(self.frame)
        self.playlist_box.pack(side="left", fill="both", expand=True)

        self.scrollbar = Scrollbar(self.frame, orient="vertical", command=self.playlist_box.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.playlist_box.config(yscrollcommand=self.scrollbar.set)

        self.load_button = Button(self.frame, text="Load Songs", command=self.load_songs)
        self.load_button.pack()
        
        self.play_button = Button(self.frame, text="Play", command=self.play_song)
        self.play_button.pack()
        
        self.pause_button = Button(self.frame, text="Pause", command=self.pause_song)
        self.pause_button.pack()
        
        self.stop_button = Button(self.frame, text="Stop", command=self.stop_song)
        self.stop_button.pack()

    def load_songs(self):
        songs = filedialog.askopenfilenames(filetypes=[("Audio Files", "*.mp3 *.wav")])
        self.playlist.extend(songs)
        for song in songs:
            self.playlist_box.insert("end", os.path.basename(song))

    def play_song(self):
        if self.playlist:
            pygame.mixer.init()
            pygame.mixer.music.load(self.playlist[self.current_index])
            pygame.mixer.music.play()
            self.song_label.config(text="Playing: " + os.path.basename(self.playlist[self.current_index]))

    def pause_song(self):
        pygame.mixer.music.pause()

    def stop_song(self):
        pygame.mixer.music.stop()
        self.song_label.config(text="No song playing")

if __name__ == "__main__":
    root = Tk()
    app = MusicPlayer(root)
    root.mainloop()
