
class ImageDithering:

    def count(self, dithered, screen):
        num = 0
        for i in range(0, len(screen)):
            for idx, char in enumerate(screen[i]):
                # Left
                left_count = True
                right_count = True
                up_count = True
                down_count = True
                    
                
                # Right

                # Up

                # Down


A = ImageDithering()
b = "BW"
c = ["AAAAAAAA",
         "ABWBWBWA",
          "AWBWBWBA",
           "ABWBWBWA",
            "AWBWBWBA",
             "AAAAAAAA"]
A.count(b, c)
