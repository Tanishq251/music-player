import os
from tkinter import *
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, window):
        window.geometry('400x300')
        window.title('Music Player')
        window.resizable(0, 0)

        # Frame for List Box
        listbox_frame = Frame(window)
        listbox_frame.pack(pady=10)

        # List Box
        self.song_listbox = Listbox(listbox_frame, width=40)
        self.song_listbox.pack()

        # Frame for Buttons
        button_frame = Frame(window)
        button_frame.pack(pady=10)

        load_button = Button(button_frame, text='Load', width=10, font=('Times', 10), command=self.load)
        play_button = Button(button_frame, text='Play', width=10, font=('Times', 10), command=self.play)
        pause_button = Button(button_frame, text='Pause', width=10, font=('Times', 10), command=self.pause)
        stop_button = Button(button_frame, text='Stop', width=10, font=('Times', 10), command=self.stop)
        prev_button = Button(button_frame, text='Previous', width=10, font=('Times', 10), command=self.play_previous)
        next_button = Button(button_frame, text='Next', width=10, font=('Times', 10), command=self.play_next)

        load_button.pack(side=LEFT)
        play_button.pack(side=LEFT)
        pause_button.pack(side=LEFT)
        stop_button.pack(side=LEFT)
        prev_button.pack(side=LEFT)
        next_button.pack(side=LEFT)

        self.music_files = []
        self.current_song_index = 0
        self.playing_state = False

        # Bind the list box selection event
        self.song_listbox.bind("<<ListboxSelect>>", self.on_song_select)

    def load(self):
        self.music_files = filedialog.askopenfilenames(filetypes=[('MP3 Files', '*.mp3')])
        self.song_listbox.delete(0, END)
        for music_file in self.music_files:
            song_name = os.path.basename(music_file)
            self.song_listbox.insert(END, song_name)

    def play(self):
        if self.music_files:
            pygame.mixer.init()
            pygame.mixer.music.load(self.music_files[self.current_song_index])
            pygame.mixer.music.play()

    def pause(self):
        if not self.playing_state and self.music_files:
            pygame.mixer.music.pause()
            self.playing_state = True
        else:
            pygame.mixer.music.unpause()
            self.playing_state = False

    def stop(self):
        if self.music_files:
            pygame.mixer.music.stop()
            self.playing_state = False

    def play_previous(self):
        if self.music_files:
            self.current_song_index = (self.current_song_index - 1) % len(self.music_files)
            self.play()

    def play_next(self):
        if self.music_files:
            self.current_song_index = (self.current_song_index + 1) % len(self.music_files)
            self.play()

    def on_song_select(self, event):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            self.current_song_index = index

root = Tk()
app = MusicPlayer(root)
root.mainloop()


