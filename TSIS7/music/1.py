import pygame
import os

pygame.init()
screen = pygame.display.set_mode((300, 100))
music_dir = os.getcwd()
music_files = os.listdir(music_dir)
current_track = 1
font = pygame.font.SysFont("comicsansms", 16)

# Global variable to track whether the music is paused or not
music_paused = False

def load_and_play_track(track_index):
    pygame.mixer.music.load(os.path.join(music_dir, music_files[track_index]))
    pygame.mixer.music.play(start=pygame.mixer.music.get_pos())  # Resume from the previous position

load_and_play_track(current_track)

def play_music():
    pygame.mixer.music.play()  # Unpause the music

def pause_music():
    global music_paused
    if music_paused:
        pygame.mixer.music.unpause()  # Unpause the music
        music_paused = False
    else:
        pygame.mixer.music.pause()  # Pause the music
        music_paused = True

def next_track():
    global current_track
    current_track = (current_track + 1) % len(music_files)
    load_and_play_track(current_track)

def previous_track():
    global current_track
    current_track = (current_track - 1) % len(music_files)
    load_and_play_track(current_track)

running = True
while running:
    screen.fill((255, 255, 255))
    nam_mus = music_files[current_track]
    shugaru = font.render(str(nam_mus), 1, "red")
    screen.blit(shugaru, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play_music()
            elif event.key == pygame.K_p:  # Press 'P' to pause/play
                pause_music()
            elif event.key == pygame.K_RIGHT:
                next_track()
            elif event.key == pygame.K_LEFT:
                previous_track()
    
    pygame.display.flip()

# Previous track - 'LEFT', Next track - 'RIGHT', Pause/Play music - 'P'
pygame.quit()