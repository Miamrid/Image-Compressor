from PIL import Image


def compress_image(input_path, output_path, quality=25):

    
    try:
        
        with Image.open(input_path) as img:
           
            img.save(output_path, 'PNG', quality=quality)
            print(f"Image compressed and saved to {output_path}")
    except Exception as e:
        print(f"Error: {e}")


input_image_path = 'kitten.jpg'
output_image_path = 'output_compressed.jpg'
compress_image(input_image_path, output_image_path, quality=25)
