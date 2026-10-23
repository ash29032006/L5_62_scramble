"""Interactive text box widget for Pygame input handling."""

# pylint: disable=no-member
import pygame


class TextBox:
    """A graphical text input box component supporting typing and backspace."""

    def __init__(self, x, y, width, height):
        """Initialize the text box dimensions and default state."""
        self.rect = pygame.Rect(x, y, width, height)
        self.text = ""
        self.active = True
        self.font = pygame.font.SysFont(None, 34)

    def handle_event(self, event):
        """Process keyboard keystrokes and focus-selection mouse clicks."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
        elif event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.unicode.isalpha() and len(self.text) < 15:
                self.text += event.unicode.upper()

    def clear(self):
        """Clear current string buffer."""
        self.text = ""

    def render(self, surface):
        """Draw the text box background, border outline, and active text."""
        box_color = (80, 150, 245) if self.active else (100, 105, 115)
        pygame.draw.rect(surface, (255, 255, 255), self.rect, border_radius=6)
        pygame.draw.rect(
            surface, box_color, self.rect, width=3, border_radius=6
        )

        text_surf = self.font.render(self.text, True, (20, 20, 20))
        surface.blit(text_surf, (self.rect.x + 14, self.rect.y + 8))
