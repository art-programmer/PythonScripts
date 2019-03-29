def tileImages(image_list, background_color=0, padding=5):
    image_width = image_list[0][0].shape[1]
    image_height = image_list[0][0].shape[0]
    width = image_width * len(image_list[0]) + padding * (len(image_list[0]) + 1)
    height = image_height * len(image_list) + padding * (len(image_list) + 1)
    tiled_image = np.zeros((height, width, 3), dtype=np.uint8)
    tiled_image[:, :] = background_color
    for y, images in enumerate(image_list):
        offset_y = image_height * y + padding * (y + 1)        
        for x, image in enumerate(images):
            offset_x = image_width * x + padding * (x + 1)                    
            tiled_image[offset_y:offset_y + image_height, offset_x:offset_x + image_width] = image
            continue
        continue
    return tiled_image
