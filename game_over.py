def draw_game_over_screen():
   quit_screen = quit_screen.render("Game Over. 'R' Restart 'Q' Quit", True, WHITE)
   quit_rect = quit_screen.get_rect(center=(WIDTH // 2, HEIGHT // 2))
   screen.blit(quit_screen, quit_rect)
