from PIL import Image 
def main():
  filename = input("Enter the image file name: ")
  # red = int(input("Enter an integer [0..255] for red: "))
  # green = int(input("Enter an integer [0..255] for green: "))
  # blue = int(input("Enter an integer [0..255] for blue: "))  
                    
  with Image.open(filename).convert('RGB') as image:
    def blackAndWhite(image):
      """Converts the argument image to black and white."""
      blackPixel = (0, 0, 0)
      whitePixel = (255, 255, 255)
      # width, height = image.size
      for y in range(image.getHeight()):
          for x in range(image.getWidth()):
              (r, g, b) = image.getPixel(x, y)
              average = (r + g + b) // 3
              if average < 128:
                  image.setPixel(x, y, blackPixel)
              else:
                  image.setPixel(x, y, whitePixel)
                  
    blackAndWhite(image)
    image.draw()

if __name__ == "__main__":
   main()

