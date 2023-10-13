import pygame

path = __file__[:len(__file__.rpartition('\\')[0])] + '\\'

sprite_sheet = pygame.image.load(path + "Kayla.png")
sheet_dim = [sprite_sheet.get_width(), sprite_sheet.get_height()]
sprite_size = [32, 32]

label = "down"

def Capture(display,name,pos,size): # (pygame Surface, String, tuple, tuple)
    img = pygame.Surface(size)  # Create image surface
    img.blit(display,(0,0),(pos,size))  # Blit portion of the display to the image
    img.set_colorkey()
    pygame.image.save(img, name)  # Save the image to the disk

print(f"\n{sheet_dim[0]/sprite_size[0]}\n")

for column in range(0, int(sheet_dim[0]/sprite_size[0])):
    pos = (column*sprite_size[0], 0)
    size = (sprite_size[0], sprite_size[1])
    
    if column < 10:
        name = f"{label}_0{column}.png"
    else:
        name = f"{label}_{column}.png"
        
    Capture(sprite_sheet, name, pos, size)