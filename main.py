# Dependencies
import customtkinter
from tkinter.messagebox import showinfo
from tkinter import filedialog as fd
from moviepy import VideoFileClip
import tempfile

customtkinter.set_appearance_mode("System") 

# Setting the main window
app = customtkinter.CTk(fg_color="#111111")
app.geometry("600x400")
app.resizable(False, False)
app.title("Video Compressor")

# Input and search frame
class InputAndSearchFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        def select_file():
            # Only allowing mp4 files
            filetypes = (('MP4 files', '*.mp4'),)

            # Asking for file
            filename = fd.askopenfilename(title='Open a file',initialdir='/',filetypes=filetypes)
            
            message = ""
            try:
                # Cheking if a file is selected
                if not filename:
                    showinfo(title='No file selected', message='Please select a valid MP4 file.')
                    return
                
                # Gettin main info about the video
                video_clip = VideoFileClip(filename)
                bitrate = video_clip.reader.bitrate
                duration = video_clip.duration
                print(f"Bitrate: {bitrate} bps, Duration: {duration} seconds")

                # Making it ~10 MB and estimated bitrate
                target_size = 10 * 1024 * 1024 - 100 * 1024 
                target_bitrate = (target_size) / duration 

                # Setting audio to be ~128 kbps
                audio_bitrate = 128 
                video_bitrate = int(target_bitrate - audio_bitrate)/250

                print(f"Target video bitrate: {video_bitrate} bps, Audio bitrate: {audio_bitrate} bps")
                # Writing the file
                video_clip.write_videofile(
                    "output.mp4",
                    codec="libx264",
                    audio_codec="aac",
                    bitrate=f"{video_bitrate}k",
                    audio_bitrate=f"{audio_bitrate}k",
                    ffmpeg_params=["-vf", "scale=-1:720"],
                    temp_audiofile=f"{tempfile.gettempdir()}/compressionTempAudio.mp4"
                )

                # Message saying its done
                print(f"Compression successful for {filename}")
                message = f"File '{filename}' has been successfully compressed and saved as 'output.mp4'."
                showinfo(
                    title='Converting completed',
                    message="filename: output.mp4\nFile saved in the current directory."
                )
            except Exception as e:
                print(f"Error compressing {filename}: {str(e)}")
                message = f"Error compressing {filename}: {str(e)}"


        # Open file button
        open_button = customtkinter.CTkButton(
            self,
            text='Open a File',
            command=select_file
        )

        open_button.pack(expand=True)

# Creating and adding the file input frame to the main window
frame = InputAndSearchFrame(master=app, width=500, height=100)
frame.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

app.mainloop()