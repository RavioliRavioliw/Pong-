import pygame as pyg

class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pyg.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):

		action = False

		surface.blit(self.image, (self.rect.x, self.rect.y))

		pos = pyg.mouse.get_pos()

		if self.rect.collidepoint(pos):
			if pyg.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True
			if pyg.mouse.get_pressed()[0] == 0 and self.clicked == True:
				self.clicked = False
		return action
