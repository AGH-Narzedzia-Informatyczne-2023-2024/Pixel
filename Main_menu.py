class Menu():
    self.game = game
    self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
    self.run_display = True
    self.cursor_rect = pygame.React(0, 0, 20, 20)
    self.offset = - 100
