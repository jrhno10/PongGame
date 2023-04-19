def moveUp(self, pixels):
  self.rect.y -= pixels
	#Check that you are not going too far (off the screen)
  if self.rect.y < 0:
    elf.rect.y = 0
          
def moveDown(self, pixels):
  self.rect.y += pixels
	#Check that you are not going too far (off the screen)
  if self.rect.y > 400:
    self.rect.y = 400
