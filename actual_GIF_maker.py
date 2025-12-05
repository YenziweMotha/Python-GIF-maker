from PIL import Image
import glob
frames_folder=  "/home/yenziwev"
def make_GIF(frame_folder):
    frames = [Image.open(image) for image  in glob.glob(f"{frame_folder}/*.PNG")]
    frame_one = frames[0]
    frame_one.save("party_ yenz.gif" , format="GIF", append_images= frames, save_all = True, duration = 100 , loop= 0 )


if __name__ == "__main__":
    make_GIF("/vidoegood1frames")

