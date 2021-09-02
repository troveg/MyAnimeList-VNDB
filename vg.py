import binascii, operator, shutil, glob, os
from tkinter import *
from PIL import Image, ImageTk
import tkinter.ttk as ttk
import tkinter.filedialog as filedialog

# Tkinter Root Window
root = Tk()
root.geometry("1920x1020")
root.state("zoomed")
root.title("MyAnimeList")

# Declare Variables
database_directory = "B:\\MEDIA\\Python Projects\\MAL\\resources\\database\\Video Games\\"
temp_directory = "B:\\MEDIA\\Python Projects\\MAL\\resources\\-temp-\\"
resource_directory = "B:\\Media\\Python Projects\\MAL\\resources\\"
temp_image = (ImageTk.PhotoImage(Image.open(resource_directory + "temp.png").resize((72, 100), Image.ANTIALIAS)))
ranking_image = ImageTk.PhotoImage(Image.open(resource_directory + "margin.png"))
status_image = ImageTk.PhotoImage(Image.open(resource_directory + "status.png"))
star_image = ImageTk.PhotoImage(Image.open(resource_directory + "star.png"))
database_panel_height = 0
database_count = 0
progress_var = 0
search_var = ""
scroll = 233
database = []

# Background Wallpaper
bg_img = ImageTk.PhotoImage(Image.open(resource_directory + "vndb_bg.png"))
logo_img = ImageTk.PhotoImage(Image.open(resource_directory + "logo.png"))
background_image = Label(root, image=bg_img)
background_image.place(x=0, y=0, relwidth=1, relheight=1)

# Define Button Images
primary_button_home_img = ImageTk.PhotoImage(Image.open(resource_directory + "button_home.png"))
primary_button_anime_img = ImageTk.PhotoImage(Image.open(resource_directory + "button_anime.png"))
primary_button_manga_img = ImageTk.PhotoImage(Image.open(resource_directory + "button_manga.png"))
primary_button_vn_img = ImageTk.PhotoImage(Image.open(resource_directory + "button_vn.png"))
primary_button_vg_img = ImageTk.PhotoImage(Image.open(resource_directory + "button_vg.png"))
primary_button_search_img = ImageTk.PhotoImage(Image.open(resource_directory + "button_search.png"))

# Raise Frames
def load_database():
    global database, progress_var
    database = []
    database_max = 0
    os.chdir(database_directory)
    # Initialize Database
    for file in glob.glob("*.mal"):
        database_max += 1
    for file in glob.glob("*.mal"):
        with open(file, 'rb') as f:
            content = f.read()
            f.close()
        content = binascii.hexlify(content).upper()
        content = content.decode("ASCII")
        # Get Image Hex
        image_hex_get = str(content).split("696D6167653A3A60")
        image_hex_get = image_hex_get[1].split("60283A783A29")
        image_hex_get = image_hex_get[0]
        # Get Title
        title_get = str(content).split("7469746C653A3A60")
        title_get = title_get[1].split("60283A783A29")
        title_get = binascii.unhexlify(title_get[0]).decode("utf-8")
        # Get User Score
        user_score_get = str(content).split("73636F72653A3A60")
        user_score_get = user_score_get[1].split("60283A783A29")
        user_score_get = binascii.unhexlify(user_score_get[0]).decode("utf-8")
        # Get User Status
        user_status_get = str(content).split("7374617475733A3A60")
        user_status_get = user_status_get[1].split("60283A783A29")
        user_status_get = binascii.unhexlify(user_status_get[0]).decode("utf-8")
        # Get Units Sold
        members_get = str(content).split("706F70756C61726974793A3A60")
        members_get = members_get[1].split("60283A783A29")
        members_get = binascii.unhexlify(members_get[0]).decode("utf-8")
        # Get Type
        type_get = str(content).split("747970653A3A60")
        type_get = type_get[1].split("60283A783A29")
        type_get = binascii.unhexlify(type_get[0]).decode("utf-8")
        # Get Season
        season_get = str(content).split("736561736F6E3A3A60")
        season_get = season_get[1].split("60283A783A29")
        season_get = binascii.unhexlify(season_get[0]).decode("utf-8")
        # Get MAL Score
        mal_score_get = str(content).split("6D616C5F73636F72653A3A60")
        mal_score_get = mal_score_get[1].split("60283A783A29")
        mal_score_get = binascii.unhexlify(mal_score_get[0]).decode("utf-8")
        # Append to Database
        database.append(Game("1", temp_image, image_hex_get, title_get, type_get, season_get,
                             members_get, user_score_get, mal_score_get, user_status_get))
        # Update Loading Screen
        progress_var += 1
        progress_load.configure(value=((progress_var / database_max) * 100))
    # Sort Scores
    database = sorted(database, key=operator.attrgetter('score'), reverse=True)

def root_creation():
    # Frame Creation
    for item in database:
        item.ranking = database.index(item) + 1
        item.label_creation()
        item.frame_creation()
        item.panel_creation()
    label_margin.place(x=(-4), y=(-4))
    frame_margin.place(x=19, y=19)
    panel_root.place(x=550, y=233)
    panel_root.tkraise()

def generate_vg():
    # Fix Temp Directory
    try:
        shutil.rmtree(temp_directory)
    except FileNotFoundError:
        pass
    os.mkdir(temp_directory)
    mal_id = (input("MAL ID: "))
    data = []
    # Get Title
    data_title = input("Title: ")
    data_title = "title::`" + data_title + "`(:x:)"
    data.append(data_title)
    # Get Score
    data_score = input("Score: ")
    data_score = "score::`" + data_score + "`(:x:)"
    data.append(data_score)
    # Get Status
    data_status = "Completed"
    data_status = "status::`" + data_status + "`(:x:)"
    data.append(data_status)
    # Get Popularity
    data_popularity = input("Units Sold: ")
    data_popularity = "popularity::`" + data_popularity + "`(:x:)"
    data.append(data_popularity)
    # Get Type
    data_type = input("Console: ")
    data_type = "type::`" + data_type + "`(:x:)"
    data.append(data_type)
    # Get Season
    data_season = input("Season Released: ")
    data_season = "season::`" + data_season + "`(:x:)"
    data.append(data_season)
    # Get MAL Score
    data_mal_score = input("MAL Score: ")
    data_mal_score = "mal_score::`" + data_mal_score + "`(:x:)"
    data.append(data_mal_score)
    # Convert to HEX
    build_database = ""
    for item in data:
        build_database += item
    build_database += "image::`"
    build_database = build_database.encode("utf-8").hex().upper()
    database_end = "`(:x:)".encode("utf-8").hex().upper()
    # Get Image
    data_image = filedialog.askopenfilename()
    with open(data_image, 'rb') as f:
        content = f.read()
    image_hex = binascii.hexlify(content).upper()
    image_hex = image_hex.decode("ASCII")
    build_database += (image_hex + database_end)
    # Build File
    data_file = database_directory + mal_id + ".mal"
    with open(data_file, "wb") as f:
        f.write(binascii.unhexlify(build_database))

def raise_panel(panel):
    global scroll
    scroll = 233
    set_scroll(scroll)
    panel.tkraise()
    button_panel.tkraise()

def set_scroll(scroll_var):
    panel_root.place(x=550, y=scroll_var)

class Game:
    def __init__(self, ranking, image, image_hex, title, media_type,
                 season, members, score, mal_score, status):
        global database_count
        self.ranking = ranking
        self.ranking_x = 6
        self.image = image
        self.image_hex = image_hex
        self.title = title
        self.media_type = media_type
        self.season = season
        self.members = members
        self.score = score
        self.mal_score = mal_score
        self.status = status
        # Update Image
        data_file = temp_directory + str(self.score) + ".png"
        with open(data_file, "wb") as f:
            f.write(binascii.unhexlify(self.image_hex))
        self.image = ImageTk.PhotoImage((Image.open(data_file).resize((72, 100), Image.ANTIALIAS)))
        # Define Frames
        self.panel = Frame(panel_root, background="#1f2024", width=1020, height=115,
                           highlightbackground="#2e51a2", highlightthickness=1)
        self.ranking_frame = Frame(self.panel, background="#1f2024", width=76, height=115,
                                   highlightbackground="#2e51a2", highlightthickness=1)
        self.title_frame = Frame(self.panel, background="#1f2024", width=656, height=115,
                                 highlightbackground="#2e51a2", highlightthickness=1)
        self.score_frame = Frame(self.panel, background="#1f2024", width=98, height=115,
                                 highlightbackground="#2e51a2", highlightthickness=1)
        self.mal_score_frame = Frame(self.panel, background="#1f2024", width=98, height=115,
                                     highlightbackground="#2e51a2", highlightthickness=1)
        self.status_frame = Frame(self.panel, background="#1f2024", width=98, height=115,
                                  highlightbackground="#2e51a2", highlightthickness=1)
        # Define Labels
        self.image_label = Label(self.title_frame, background="#1f2024", width=72, height=100,
                                 highlightbackground="#2e51a2", highlightthickness=1, image=self.image)
        self.ranking_label = Label(self.ranking_frame, text=self.ranking, font=("Verdana", 30, 'bold'),
                                   fg='grey', background="#1f2024", highlightbackground="#2e51a2")
        self.title_label = Label(self.title_frame, text=self.title, font=("Verdana", 11, 'bold'),
                                 fg='#1d439b', background="#1f2024", highlightbackground="#2e51a2", cursor="hand2")
        self.type_label = Label(self.title_frame, text=self.media_type, font=("Verdana", 8, 'bold'),
                                fg='grey', background="#1f2024", highlightbackground="#2e51a2")
        self.season_label = Label(self.title_frame, text=self.season, font=("Verdana", 8, 'bold'),
                                  fg='grey', background="#1f2024", highlightbackground="#2e51a2")
        self.members_label = Label(self.title_frame, text=(f"{int(self.members):,d}" + " members"),
                                   font=("Verdana", 8, 'bold'), fg='grey',
                                   background="#1f2024", highlightbackground="#2e51a2")
        self.score_label = Label(self.score_frame, text=self.score, font=("Verdana", 11),
                                 fg='white', background="#1f2024", highlightbackground="#2e51a2")
        self.image_star = Label(self.score_frame, image=star_image, background="#1f2024")
        self.mal_score_label = Label(self.mal_score_frame, text=self.mal_score, font=("Verdana", 11),
                                     fg='white', background="#1f2024", highlightbackground="#2e51a2")
        self.image_mal_star = Label(self.mal_score_frame, image=star_image, background="#1f2024")
        self.image_status = Label(self.status_frame, image=status_image, background="#1f2024")
        self.status_label = Label(self.status_frame, text=self.status, font=("Avenir", 8), fg='#1853d9',
                                  background="#1f2024", highlightbackground="#2e51a2", cursor="hand2")
    def label_creation(self):
        # Set Ranking Position
        if int(self.ranking) < 10:
            self.ranking_x = 21
        # Place Labels
        self.ranking_label.configure(text=self.ranking)
        self.image_label.place(x=8, y=4)
        self.ranking_label.place(x=self.ranking_x, y=26)
        self.title_label.place(x=90, y=10)
        self.type_label.place(x=90, y=32)
        self.season_label.place(x=90, y=50)
        self.members_label.place(x=90, y=68)
        self.score_label.place(x=35, y=44)
        self.image_star.place(x=15, y=46)
        self.mal_score_label.place(x=35, y=44)
        self.image_mal_star.place(x=15, y=46)
        self.image_status.place(x=6, y=42)
        self.status_label.place(x=20, y=47)
    def frame_creation(self):
        self.ranking_frame.place(x=(-1), y=(-1))
        self.title_frame.place(x=74, y=(-1))
        self.score_frame.place(x=729, y=(-1))
        self.mal_score_frame.place(x=825, y=(-1))
        self.status_frame.place(x=921, y=(-1))
    def panel_creation(self):
        global database_count, database_panel_height
        self.panel.place(x=19, y=(45 + (database_count * 114)))
        database_panel_height = ((45 + (database_count * 114)) + 115)
        if database_panel_height < 763:
            database_panel_height = 763
        panel_root.configure(height=(database_panel_height + 21))  # +1
        database_count += 1

# Define Root Panel
panel_root = Frame(root, background="#1f2024", width=1060, height=784,
                   highlightbackground="#2e51a2", highlightthickness=1)
frame_margin = Frame(panel_root, width=1020, height=27,
                     highlightbackground="#2e51a2", highlightthickness=1)
label_margin = Label(frame_margin, image=ranking_image,
                     highlightbackground="#2e51a2", highlightthickness=1)

# Define Button Panel
button_panel = Frame(root, background="#2e51a2", width=1060, height=234,
                     highlightbackground="#2e51a2", highlightthickness=1)
logo_patch = Label(button_panel, image=logo_img, background="black",
                   highlightbackground="black")
button_home = Button(button_panel, command=raise_panel(panel_root),
                     image=primary_button_home_img, bd=0, background="#2e51a2", cursor="hand2")
button_anime = Button(button_panel, command=lambda: raise_panel(panel_root),
                      image=primary_button_anime_img, bd=0, background="#2e51a2", cursor="hand2")
button_manga = Button(button_panel, command=lambda: raise_panel(panel_root),
                      image=primary_button_manga_img, bd=0, background="#2e51a2", cursor="hand2")
button_vn = Button(button_panel, image=primary_button_vn_img, bd=0,
                   background="#2e51a2", cursor="hand2")
button_vg = Button(button_panel, command=lambda: raise_panel(panel_root),
                   image=primary_button_vg_img, bd=0, background="#2e51a2", cursor="hand2")
search_bar = Entry(button_panel, textvariable=search_var,
                   font=('arial', 10, 'normal'), width=74)
button_search = Button(button_panel, image=primary_button_search_img,
                       bd=0, background="#2e51a2", cursor="hand2", command=generate_vg)

# Define Loading Panel
panel_load = Frame(root, background="#1f2024", width=1060, height=784,
                   highlightbackground="#2e51a2", highlightthickness=1)
progress_load = ttk.Progressbar(panel_load, orient=HORIZONTAL, length=800, mode='determinate', value=progress_var)
button = Button(panel_load)

# Place Primary Buttons
button_home.place(x=0, y=200)
button_anime.place(x=80, y=200)
button_manga.place(x=163, y=200)
button_vn.place(x=246, y=200)
button_vg.place(x=309, y=200)
search_bar.place(x=500, y=207)
button_search.place(x=1022, y=206)
logo_patch.place(x=(-3), y=(-5))
button_panel.place(x=550, y=0)

# Place Loading Frames
progress_load.place(x=130, y=320)
panel_load.place(x=550, y=233)
panel_load.tkraise()

# Start Program
load_database()
root_creation()
root.mainloop()
