import pygame
from player import MusicPlayer


pygame.init()
pygame.mixer.init()


screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("KBTU Music Player")
font = pygame.font.SysFont("Arial", 24)


WHITE = (255, 255, 255)
BLACK = (30, 30, 30)
GREEN = (0, 255, 0)


player = MusicPlayer("music/")

running = True
while running:
    screen.fill(BLACK)

    
    track_name = player.get_current_track_name()
    status = "Playing" if player.is_playing else "Stopped/Paused"
    
    
    text_surf = font.render(f"Track: {track_name}", True, WHITE)
    status_surf = font.render(f"Status: {status}", True, GREEN)
    instr_surf = font.render("P: Play/Pause | S: Stop | N: Next | B: Back", True, (150, 150, 150))

    screen.blit(text_surf, (50, 100))
    screen.blit(status_surf, (50, 150))
    screen.blit(instr_surf, (50, 300))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:     
                
                if not pygame.mixer.music.get_busy():
                    player.play()
                else:
                    player.pause_unpause()
            
            elif event.key == pygame.K_s:   
                player.stop()
            
            elif event.key == pygame.K_n:    
                player.next_track()
            
            elif event.key == pygame.K_b:   
                player.prev_track()
            
            elif event.key == pygame.K_q:   
                running = False

    pygame.display.flip()

pygame.quit()