import pygame

class Square:
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height

		self.abs_x = x * width
		self.abs_y = y * height
		self.abs_pos = (self.abs_x, self.abs_y)
		self.pos = (x, y)
		self.color = 'light' if (x + y) % 2 == 0 else 'dark'
		self.draw_color = (241, 211, 170) if self.color == 'light' else (180, 126, 82)
		self.highlight_color = (150, 255, 100) if self.color == 'light' else (50, 220, 0)
		self.frozen_colours = [(132, 250, 250), (157, 250, 250), (188, 245, 245)] if self.color == "light" else \
							  [(92, 210, 210), (117, 210, 210), (148, 205, 205)]
		self.occupying_piece = None
		self.coord = self.get_coord()
		self.frozen = False
		self.freeze_level = None
		self.chain_colour = (206, 89, 22) if self.color == 'light' else (246, 129, 62)
		self.highlight = False
		self.chain = False

		self.rect = pygame.Rect(
			self.abs_x,
			self.abs_y,
			self.width,
			self.height
		)


	def get_coord(self):
		columns = 'abcdefgh'
		return columns[self.x] + str(self.y + 1)


	def draw(self, display):
		colour = self.draw_color
		if self.highlight:
			colour = self.highlight_color
		elif self.chain:
			colour = self.chain_colour	
		elif self.frozen:
			colour = self.frozen_colours[self.freeze_level]
		pygame.draw.rect(display, colour, self.rect)

		if self.occupying_piece != None:
			centering_rect = self.occupying_piece.img.get_rect()
			centering_rect.center = self.rect.center
			display.blit(self.occupying_piece.img, centering_rect.topleft)

