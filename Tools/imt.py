from PIL import Image

OUTPUT_SIZE = (64, 64)
FILENAME = "/Users/rhine/Documents/GitHub/Raspberry-pi-pico-/Tools/happy.gif"  # The file to convert
MONOCHROME = True  # Set to True for monochrome output, False for RGB output

def convert_gif_to_bmp(filename, output_size, monochrome=True):
    gif = Image.open(filename)
    print(f"Size: {gif.size}")
    print(f"Frames: {gif.n_frames}")
    
    mode = "1" if monochrome else "RGB"
    output = Image.new(mode, (output_size[0] * gif.n_frames, output_size[1]), 0)
    output_filename = f"icon_{gif.n_frames}_frames.bmp"
    
    for frame in range(gif.n_frames):
        gif.seek(frame)
        extracted_frame = gif.resize(output_size)
        position = (output_size[0] * frame, 0)
        output.paste(extracted_frame, position)
    
    if not monochrome:
        output = output.convert("P", colors=8)
    
    output.save(output_filename)
    print(f"Conversion complete. Saved as {output_filename}")

convert_gif_to_bmp(FILENAME, OUTPUT_SIZE, MONOCHROME)
