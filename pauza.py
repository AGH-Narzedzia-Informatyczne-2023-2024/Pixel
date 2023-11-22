# Funkcja rysująca tekst pauzy
def draw_pause_text():
    pause_text = pause_text_font.render("Gra wstrzymana. Naciśnij 'P' aby wznowić grę.", True, WHITE)
    text_rect = pause_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(pause_text, text_rect)
