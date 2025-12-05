from PIL import Image
import glob
frames_folder=  "./vidoegood1frames"
def make_GIF(frame_folder):
    frames = [Image.open(image) for image  in glob.glob(f"{frame_folder}/*.png")]
    frame_one = frames[0]
    frame_one.save("yenz.gif" , format="GIF", 
                        append_images= frames, save_all = True, duration = 100 , loop= 0 )

make_GIF(frames_folder)
