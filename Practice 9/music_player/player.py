import pygame
import os

class MusicPlayer:
    def __init__(self, music_dir):
        self.music_dir = music_dir
        self.playlist = [f for f in os.listdir(music_dir) if f.endswith(('.mp3', '.wav'))]
        self.current_idx = 0
        self.is_playing = False

    def play(self):
        if self.playlist:
            path = os.path.join(self.music_dir, self.playlist[self.current_idx])
            pygame.mixer.music.load(path)
            pygame.mixer.music.play()
            self.is_playing = True

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False

    def pause_unpause(self):
        if self.is_playing:
            pygame.mixer.music.pause()
            self.is_playing = False
        else:
            pygame.mixer.music.unpause()
            self.is_playing = True

    def next_track(self):
        if self.playlist:
            self.current_idx = (self.current_idx + 1) % len(self.playlist)
            self.play()

    def prev_track(self):
        if self.playlist:
            self.current_idx = (self.current_idx - 1) % len(self.playlist)
            self.play()

    def get_current_track_name(self):
        if self.playlist:
            return self.playlist[self.current_idx]
        return "No tracks found"