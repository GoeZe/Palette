from pathlib import Path
from colorsys import rgb_to_hsv
import math

import fast_colorthief
from PIL import Image
from tqdm import tqdm

class GridPainting:
    def __init__(self, logo_path, num_logos=1000, image_size=None, grid_size=None):
        self.path = Path(logo_path)
        self.num_logos = num_logos

        if grid_size is None:
            self.grid_size = [math.ceil(math.sqrt(self.num_logos))] * 2
        else:
            self.grid_size = grid_size       
        if image_size is None:
            self.image_size = [150,150]
        else:
            self.image_size = image_size
        self.output_size = [self.grid_size[0]*image_size[0], self.grid_size[1]*image_size[1]]
        self.taken = [[0] * self.grid_size[1] for i in range(self.grid_size[0])]
    
    # Use H and S as X and Y axis
    def get_dominant_color(self, image_path):
        # Get the dominant color in RGB
        dominant_color = fast_colorthief.get_dominant_color(image_path, quality=1)
        # Convert the dominant color to HSV
        dominant_color_hsv = rgb_to_hsv(*[ch / 255.0 for ch in dominant_color])

        return int(dominant_color_hsv[0]*self.grid_size[0]), int(dominant_color_hsv[1]*self.grid_size[1])
    
    def replace_transparent_with_white(self, image_path):
        # Open the image file
        img = Image.open(image_path)
        # Make sure the image has an alpha (transparency) channel
        if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
            # Convert the image into RGBA if it is not already
            alpha = img.convert('RGBA')
            # Create a new image ('RGB') and paste the RGBA image into it
            # A white (255, 255, 255) background is created for this new image
            bg = Image.new('RGB', alpha.size, (255, 255, 255))
            bg.paste(alpha, mask=alpha.split()[3])  # 3 is the alpha channel in an RGBA image
            return bg
        else:
            return img
    
    def paste_image_on_grid(self, paste_image_path, img=None):
        row, col = self.get_dominant_color(paste_image_path)
        
        # calcualte subplot size
        # sub_size = image_size

        # create a blank image if there is no input
        if img is None:
            img = Image.new('RGB', self.output_size, (255, 255, 255))
        
        # return if place is taken
        if self.taken[row][col] == 1:
            return img

        # read paste image
        paste_img = self.replace_transparent_with_white(paste_image_path)
        paste_img = paste_img.resize(self.image_size, Image.ANTIALIAS)

        # paste and mark
        img.paste(paste_img, (col*self.image_size[0], row*self.image_size[1]))
        self.taken[row][col] = 1
        return img

    def paint(self):
        t=1
        path_img = self.path.iterdir()
        for imagepath in tqdm(path_img):
            if t==1:
                img = self.paste_image_on_grid(imagepath)
                t=0
            else:
                img = self.paste_image_on_grid(imagepath, img=img)

        img.save(f"Grid {self.grid_size[0]} by {self.grid_size[1]}.png")


if __name__ == "__main__":
    logo_painting = GridPainting('/workspaces/Palette/images/passport', num_logos=200, image_size=[90,160], grid_size=[20,20])
    logo_painting.paint()

# rank_df.to_excel(f'uni ranking xy 0617 {size}.xlsx',index=False)
# draw_df = rank_df.loc[rank_df.groupby(['X','Y'])['ranking'].idxmin()]