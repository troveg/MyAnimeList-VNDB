import binascii, operator, locale, shutil, wget, glob, os
from tkinter.simpledialog import askstring
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import jikanpy as jikan_error
from jikanpy import Jikan
import tkinter.ttk as ttk

# Tkinter Root Window
root = Tk()
root.geometry("1920x1020")
root.state("zoomed")
root.title("MyAnimeList")

# Set Variables
anime_database_directory = "B:\\MEDIA\\Python Projects\\MAL\\resources\\database\\Anime\\"
vg_database_directory = "B:\\MEDIA\\Python Projects\\MAL\\resources\\database\\Anime\\"
temp_directory = "B:\\MEDIA\\Python Projects\\MAL\\resources\\-temp-\\"
resource_directory = "B:\\Media\\Python Projects\\MAL\\resources\\"
locale.setlocale(locale.LC_ALL, 'en_US')
anime_panel_height = 0
vg_panel_height = 0
progress_var = 0
jikan = Jikan()
search_var = ""
scroll = 233
database = []
top_anime_count = 0
top_vg_count = 0

# Background Wallpaper
bg_img = ImageTk.PhotoImage(Image.open(resource_directory + "vndb_bg.png"))
logo_img = ImageTk.PhotoImage(Image.open(resource_directory + "logo.png"))
background_image = Label(root, image=bg_img)
background_image.place(x=0, y=0, relwidth=1, relheight=1)

# Raise Frames
def load_database():
    global database, progress_var
    anime_database = []
    database_load_max = 0
    # Load Anime Database
    os.chdir(anime_database_directory)
    for file in glob.glob("*.mal"):
        database_load_max += 1
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
        title_get = str(content).split("6A61705F7469746C653A3A60")
        title_get = title_get[1].split("60283A783A29")
        title_get = binascii.unhexlify(title_get[0]).decode("utf-8")
        # Get Type
        type_get = str(content).split("6D656469615F747970653A3A60")
        type_get = type_get[1].split("60283A783A29")
        type_get = binascii.unhexlify(type_get[0]).decode("utf-8")
        # Get Episodes
        media_count_get = str(content).split("6D656469615F636F756E743A3A60")
        media_count_get = media_count_get[1].split("60283A783A29")
        media_count_get = binascii.unhexlify(media_count_get[0]).decode("utf-8")
        # Get Season
        media_season_get = str(content).split("6D656469615F736561736F6E3A3A60")
        media_season_get = media_season_get[1].split("60283A783A29")
        media_season_get = binascii.unhexlify(media_season_get[0]).decode("utf-8")
        # Get Members
        mal_members_get = str(content).split("6D616C5F6D656D626572733A3A60")
        mal_members_get = mal_members_get[1].split("60283A783A29")
        mal_members_get = binascii.unhexlify(mal_members_get[0]).decode("utf-8")
        # Get MAL Score
        mal_score_get = str(content).split("6D616C5F73636F72653A3A60")
        mal_score_get = mal_score_get[1].split("60283A783A29")
        mal_score_get = binascii.unhexlify(mal_score_get[0]).decode("utf-8")
        # Get MAL Rank
        mal_ranking_get = str(content).split("6D616C5F72616E6B3A3A60")
        mal_ranking_get = mal_ranking_get[1].split("60283A783A29")
        mal_ranking_get = binascii.unhexlify(mal_ranking_get[0]).decode("utf-8")
        # Get User Score
        user_score_get = str(content).split("757365725F73636F72653A3A60")
        user_score_get = user_score_get[1].split("60283A783A29")
        user_score_get = binascii.unhexlify(user_score_get[0]).decode("utf-8")
        # Get User Status
        user_status_get = str(content).split("757365725F7374617475733A3A60")
        user_status_get = user_status_get[1].split("60283A783A29")
        user_status_get = binascii.unhexlify(user_status_get[0]).decode("utf-8")
        # Append to Database
        anime_database.append(Anime("1", panel_left_image_temp_2_img, image_hex_get, title_get, type_get, media_count_get,
                              media_season_get, mal_members_get, user_score_get, mal_score_get, mal_ranking_get,
                              user_status_get))
        # Update Loading Screen
        progress_var += 1
        progress_load.configure(value=((progress_var / database_load_max) * 100))

        # Load Video Game Database
        vg_database = []
        os.chdir(vg_database_directory)
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
            type_get = str(content).split("6D656469615F747970653A3A60")
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
            vg_database.append(VG("1", panel_left_image_temp_2_img, image_hex_get, title_get, type_get, season_get,
                                  members_get, user_score_get, mal_score_get, user_status_get))
    # Sort Scores and Frame Creation
    database = sorted(database, key=operator.attrgetter('score'), reverse=True)
    for item in database:
        item.ranking = database.index(item) + 1
        item.label_creation()
        item.ranking_creation()
        item.title_creation()
        item.score_creation()
        item.mal_score_creation()
        item.status_creation()
        item.panel_creation()

def raise_top_frame(panel):
    global scroll
    scroll = 233
    set_scroll(scroll)
    panel.tkraise()
    primary_button_frame.tkraise()

def raise_home_frame():
    place_frames()
    root_panel_right.tkraise()
    root_panel_left.tkraise()

def mouse_wheel(event, panel):
    global scroll
    if event.num == 5 or event.delta == -120:
        scroll_height = (panel_top_anime.winfo_rooty() + panel_top_anime.winfo_height())
        #  1040
        if scroll_height >= 1040 + 30:
            scroll -= 30  # Frame Moves Up; View Moves Down with Wheel
            set_scroll(scroll)
        elif scroll_height < 1040 + 30:
            scroll -= scroll_height - 1040
            set_scroll(scroll)
    if event.num == 4 or event.delta == 120:
        scroll_height = panel_top_anime.winfo_rooty()
        if scroll_height <= 256 - 30:
            scroll += 30  # Frame Moves Down; View Moves Up with Wheel
            set_scroll(scroll)
        elif scroll_height > 256 - 30:
            scroll += 256 - scroll_height
            set_scroll(scroll)

def set_scroll(scroll_var):
    panel_top_anime.place(x=550, y=scroll_var)

def scrape():
    try:
        shutil.rmtree(temp_directory)
    except FileNotFoundError:
        pass
    os.mkdir(temp_directory)
    try:  # Prevents Crashing Script
        global search_var, top_anime_count
        mal_id = int(primary_button_searchbar.get())
        raw_data = jikan.anime(mal_id)  # Scrapes MAL Data From User Input ID
        data = []
        # Get Japanese Title
        try:
            data_title_jp = str(raw_data).split("'title': '")
            data_title_jp = data_title_jp[1].split("',")
        except IndexError:  # Prevents a formatting issue from raw data
            data_title_jp = str(raw_data).split("'title':" + ' "')
            data_title_jp = data_title_jp[1].split('",')
        data_title_jp = "jap_title::`" + data_title_jp[0] + "`(:x:)"
        data.append(data_title_jp)
        # Get English Title
        try:
            try:
                data_title_en = str(raw_data).split("'title_english': '")
                data_title_en = data_title_en[1].split("',")
            except IndexError:  # Prevents a formatting issue from raw data
                data_title_en = str(raw_data).split("'title_english':" + ' "')
                data_title_en = data_title_en[1].split('",')
            data_title_en = "eng_title::`" + data_title_en[0] + "`(:x:)"
            data.append(data_title_en)
        except IndexError:
            data_title_en = "eng_title::`N/A`(:x:)"
            data.append(data_title_en)
        # Get Anime Score
        data_score = str(raw_data).split("'score': ")
        data_score = data_score[1].split(",")
        data_score = "mal_score::`" + data_score[0] + "`(:x:)"
        data.append(data_score)
        # Get MAL Rank
        data_rank = str(raw_data).split("'rank': ")
        data_rank = data_rank[1].split(",")
        data_rank = "mal_rank::`" + data_rank[0] + "`(:x:)"
        data.append(data_rank)
        # Get Anime Popularity
        data_popularity = str(raw_data).split("'popularity': ")
        data_popularity = data_popularity[1].split(",")
        data_popularity = "mal_popularity::`" + data_popularity[0] + "`(:x:)"
        data.append(data_popularity)
        # Get Anime Type
        try:
            data_type = str(raw_data).split("'type': '")
            data_type = data_type[1].split("',")
        except IndexError:  # Prevents a formatting issue from raw data
            data_type = str(raw_data).split("'type':" + ' "')
            data_type = data_type[1].split('",')
        data_type = "media_type::`" + data_type[0] + "`(:x:)"
        data.append(data_type)
        # Get Anime Source
        try:
            data_source = str(raw_data).split("'source': '")
            data_source = data_source[1].split("',")
        except IndexError:  # Prevents a formatting issue from raw data
            data_source = str(raw_data).split("'season':" + ' "')
            data_source = data_source[1].split('",')
        data_source = "media_source::`" + data_source[0] + "`(:x:)"
        data.append(data_source)
        # Get Episode Count
        try:
            data_episode_count = str(raw_data).split("'episodes': ")
            data_episode_count = data_episode_count[1].split(",")
        except IndexError:  # Prevents a formatting issue from raw data
            data_episode_count = str(raw_data).split("'season':" + ' "')
            data_episode_count = data_episode_count[1].split('",')
        data_episode_count = "media_count::`" + data_episode_count[0] + "`(:x:)"
        data.append(data_episode_count)
        # Get Anime Status
        try:
            data_status = str(raw_data).split("'status': '")
            data_status = data_status[1].split("',")
        except IndexError:  # Prevents a formatting issue from raw data
            data_status = str(raw_data).split("'status':" + ' "')
            data_status = data_status[1].split('",')
        data_status = "media_status::`" + data_status[0] + "`(:x:)"
        data.append(data_status)
        # Get Season Aired
        try:
            try:
                data_season = str(raw_data).split("'premiered': '")
                data_season = data_season[1].split("',")
            except IndexError:  # Prevents a formatting issue from raw data
                data_season = str(raw_data).split("'premiered':" + ' "')
                data_season = data_season[1].split('",')
            data_season = "media_season::`" + data_season[0] + "`(:x:)"
            data.append(data_season)
        except IndexError:
            data_season = "media_season::`N/A`(:x:)"
            data.append(data_season)
        # Get Members
        data_members = str(raw_data).split("'members': ")
        data_members = data_members[1].split(",")
        data_members = "mal_members::`" + data_members[0] + "`(:x:)"
        data.append(data_members)
        # Get User Score
        data_user_score = askstring('Score', 'Input Score:')
        data_user_score = "user_score::`" + data_user_score + "`(:x:)"
        data.append(data_user_score)
        # Get User Status
        data_user_status = askstring('Status', 'Input Status:')
        data_user_status = "user_status::`" + data_user_status + "`(:x:)"
        data.append(data_user_status)
        # Get Anime Synopsis
        try:
            data_synopsis = str(raw_data).split("'synopsis': '")
            data_synopsis = data_synopsis[1].split("',")
        except IndexError:  # Prevents a formatting issue from raw data
            data_synopsis = str(raw_data).split("'synopsis':" + ' "')
            data_synopsis = data_synopsis[1].split('",')
        data_synopsis = "media_synopsis::`" + data_synopsis[0].replace("\'", "'") + "`(:x:)"
        data.append(data_synopsis)
        # Get Anime Boxart
        try:
            data_image = str(raw_data).split("'image_url': '")
            data_image = data_image[1].split("',")
        except IndexError:  # Prevents a formatting issue from raw data
            data_image = str(raw_data).split("'image_url':" + ' "')
            data_image = data_image[1].split('",')
        data_image = data_image[0]
        # Convert to HEX
        build_database = ""
        for item in data:
            build_database += item
        build_database += "image::`"
        build_database = build_database.encode("utf-8").hex().upper()
        database_end = "`(:x:)".encode("utf-8").hex().upper()
        # Get Image
        wget.download(data_image, (temp_directory + "image.jpg"))
        image = Image.open(temp_directory + "image.jpg")
        image_png = temp_directory + "image.png"
        image.save(image_png)
        # Image HEX
        with open(image_png, 'rb') as f:
            content = f.read()
        image_hex = binascii.hexlify(content).upper()
        image_hex = image_hex.decode("ASCII")
        build_database += (image_hex + database_end)
        # Build File
        data_file = anime_database_directory + str(mal_id) + ".mal"
        with open(data_file, "wb") as f:
            f.write(binascii.unhexlify(build_database))
        refresh_var = messagebox.askquestion("Database", "Do you want to refresh?")
        if refresh_var == 'yes':
            for item in database:
                item.panel.destroy()
                top_anime_count = 0
            load_database()
    except jikan_error.exceptions.APIException:  # If Jikan Fails
        print("Error 404")

# Define Primary Button Images
primary_button_home_img = ImageTk.PhotoImage(Image.open(resource_directory + "button_home.png"))
primary_button_anime_img = ImageTk.PhotoImage(Image.open(resource_directory + "button_anime.png"))
primary_button_manga_img = ImageTk.PhotoImage(Image.open(resource_directory + "button_manga.png"))
primary_button_vn_img = ImageTk.PhotoImage(Image.open(resource_directory + "button_vn.png"))
primary_button_vg_img = ImageTk.PhotoImage(Image.open(resource_directory + "button_vg.png"))
primary_button_search_img = ImageTk.PhotoImage(Image.open(resource_directory + "button_search.png"))

# Define Primary Buttons
primary_button_frame = Frame(root, background="#2e51a2", width=1060, height=234,
                             highlightbackground="#2e51a2", highlightthickness=1)
logo_image = Label(primary_button_frame, image=logo_img, background="black",
                   highlightbackground="black")
primary_button_home = Button(primary_button_frame, command=raise_home_frame,
                             image=primary_button_home_img, bd=0, background="#2e51a2", cursor="hand2")
primary_button_anime = Button(primary_button_frame, command=lambda: raise_top_frame(panel_top_anime),
                              image=primary_button_anime_img, bd=0, background="#2e51a2", cursor="hand2")
primary_button_manga = Button(primary_button_frame, command=lambda: raise_top_frame(panel_top_anime),
                              image=primary_button_manga_img, bd=0, background="#2e51a2", cursor="hand2")
primary_button_vn = Button(primary_button_frame, image=primary_button_vn_img, bd=0,
                           background="#2e51a2", cursor="hand2")
primary_button_vg = Button(primary_button_frame, command=lambda: raise_top_frame(panel_top_vg),
                           image=primary_button_vg_img, bd=0, background="#2e51a2", cursor="hand2")
primary_button_searchbar = Entry(primary_button_frame, textvariable=search_var,
                                 font=('arial', 10, 'normal'), width=74)
primary_button_search = Button(primary_button_frame, image=primary_button_search_img,
                               command=scrape, bd=0, background="#2e51a2", cursor="hand2")

# Define Images
image_top_anime_star = ImageTk.PhotoImage(Image.open(resource_directory + "star.png"))
#   Define Right Temp Images
panel_right_image_temp_1 = ImageTk.PhotoImage(Image.open(resource_directory + "\\vndb\\Box Art\\Clannad {Clannad}.png"))
panel_right_image_temp_2 = ImageTk.PhotoImage(
    Image.open(resource_directory + "\\vndb\\Box Art\\Clannad {Clannad Side Stories}.png"))
panel_right_image_temp_3 = ImageTk.PhotoImage(
    Image.open(resource_directory + "\\vndb\\Box Art\\Clannad {Tomoyo After, It's a Wonderful Life}.png"))
panel_right_image_temp_4 = ImageTk.PhotoImage(
    Image.open(resource_directory + "\\vndb\\Box Art\\Ciconia When They Cry {Ciconia CH1}.png"))
panel_right_image_temp_5 = ImageTk.PhotoImage(
    Image.open(resource_directory + "\\vndb\\Box Art\\Corpse Party {Corpse Party Book of Shadows}.png"))
#   Define Left Temp Images
panel_left_image_temp_1_img = ImageTk.PhotoImage(
    Image.open(resource_directory + "\\myanimelist\\Code Geass {Code Geass}.png"))
panel_left_image_temp_2_img = (ImageTk.PhotoImage(
    Image.open(resource_directory + "\\myanimelist\\Tokyo Ghoul {Tokyo Ghoul}.png").resize((72, 100), Image.ANTIALIAS)))

# Define Right Panel Frames
root_panel_right = Frame(root, background="#1f2024", width=322, height=784,
                         highlightbackground="#2e51a2", highlightthickness=1)
panel_right_vn_1 = Frame(root_panel_right, background="#1f2024", width=276, height=130)
panel_right_vn_2 = Frame(root_panel_right, background="#1f2024", width=276, height=130)
panel_right_vn_3 = Frame(root_panel_right, background="#1f2024", width=276, height=130)
panel_right_vn_4 = Frame(root_panel_right, background="#1f2024", width=276, height=130)
panel_right_vn_5 = Frame(root_panel_right, background="#1f2024", width=276, height=130)
#   Define Right Panel Image Labels
panel_right_label_temp_1_img = Label(panel_right_vn_1, image=panel_right_image_temp_1)
panel_right_label_temp_2_img = Label(panel_right_vn_2, image=panel_right_image_temp_2)
panel_right_label_temp_3_img = Label(panel_right_vn_3, image=panel_right_image_temp_3)
panel_right_label_temp_4_img = Label(panel_right_vn_4, image=panel_right_image_temp_4)
panel_right_label_temp_5_img = Label(panel_right_vn_5, image=panel_right_image_temp_5)

# Define Left Panel Frames
root_panel_left = Frame(root, background="#1f2024", width=739, height=784,
                        highlightbackground="#2e51a2", highlightthickness=1)
panel_left_frame_1 = Frame(root_panel_left, background="#1f2024", width=739, height=290,
                           highlightbackground="#2e51a2", highlightthickness=1)  # Section 1
panel_left_frame_2 = Frame(root_panel_left, background="#1f2024", width=739, height=290,
                           highlightbackground="#2e51a2", highlightthickness=1)  # Section 2
panel_left_frame_3 = Frame(root_panel_left, background="#1f2024", width=739, height=290,
                           highlightbackground="#2e51a2", highlightthickness=1)  # Section 3
panel_left_anime_1 = Frame(root_panel_left, background="#1f2024", width=165, height=250)
# Define Left Panel Image Labels
panel_left_label_temp_1 = Label(panel_left_anime_1, image=panel_left_image_temp_1_img)  # Code Geass

# Define Top Anime 100 Panel Frames
panel_top_anime = Frame(root, background="#1f2024", width=1060, height=784,
                        highlightbackground="#2e51a2", highlightthickness=1)
root.bind("<MouseWheel>", mouse_wheel)
frame_top_anime_label = Frame(panel_top_anime, background="#1853d9", width=1020, height=26,
                              highlightbackground="#2e51a2", highlightthickness=1)
frame_top_anime_ranking = Frame(frame_top_anime_label, background="#1853d9", width=76, height=115,
                                highlightbackground="#1853d9", highlightthickness=1)
label_top_anime_ranking = Label(frame_top_anime_ranking, text="Rank", font=("Verdana", 10, 'bold'),
                                fg='white', background="#1853d9", highlightbackground="#2e51a2")
frame_top_anime_title = Frame(frame_top_anime_label, background="#1853d9", width=656, height=115,
                              highlightbackground="#2e51a2", highlightthickness=1)
label_top_anime_title = Label(frame_top_anime_title, text="Title", font=("Verdana", 10, 'bold'),
                              fg='white', background="#1853d9", highlightbackground="#2e51a2")
frame_top_anime_score = Frame(frame_top_anime_label, background="#1853d9", width=98, height=115,
                              highlightbackground="#2e51a2", highlightthickness=1)
label_top_anime_score = Label(frame_top_anime_score, text="Score", font=("Verdana", 10, 'bold'),
                              fg='white', background="#1853d9", highlightbackground="#2e51a2")
frame_top_anime_mal_score = Frame(frame_top_anime_label, background="#1853d9", width=98, height=115,
                                  highlightbackground="#2e51a2", highlightthickness=1)
label_top_anime_mal_score = Label(frame_top_anime_mal_score, text="MAL", font=("Verdana", 10, 'bold'),
                                  fg='white', background="#1853d9", highlightbackground="#2e51a2")
frame_top_anime_status = Frame(frame_top_anime_label, background="#1853d9", width=98, height=115,
                               highlightbackground="#2e51a2", highlightthickness=1)
label_top_anime_status = Label(frame_top_anime_status, text="Status", font=("Verdana", 10, 'bold'),
                               fg='white', background="#1853d9", highlightbackground="#2e51a2")
image_top_anime_status = ImageTk.PhotoImage(Image.open(resource_directory + "status.png"))

# Define Top 100 VG Panel Frames
panel_top_vg = Frame(root, background="#1f2024", width=1060, height=784,
                        highlightbackground="#2e51a2", highlightthickness=1)
root.bind("<MouseWheel>", mouse_wheel)
frame_top_vg_label = Frame(panel_top_vg, background="#1853d9", width=1020, height=26,
                              highlightbackground="#2e51a2", highlightthickness=1)
frame_top_vg_ranking = Frame(frame_top_vg_label, background="#1853d9", width=76, height=115,
                                highlightbackground="#1853d9", highlightthickness=1)
label_top_vg_ranking = Label(frame_top_vg_ranking, text="Rank", font=("Verdana", 10, 'bold'),
                                fg='white', background="#1853d9", highlightbackground="#2e51a2")
frame_top_vg_title = Frame(frame_top_vg_label, background="#1853d9", width=656, height=115,
                              highlightbackground="#2e51a2", highlightthickness=1)
label_top_vg_title = Label(frame_top_vg_title, text="Title", font=("Verdana", 10, 'bold'),
                              fg='white', background="#1853d9", highlightbackground="#2e51a2")
frame_top_vg_score = Frame(frame_top_vg_label, background="#1853d9", width=98, height=115,
                              highlightbackground="#2e51a2", highlightthickness=1)
label_top_vg_score = Label(frame_top_vg_score, text="Score", font=("Verdana", 10, 'bold'),
                              fg='white', background="#1853d9", highlightbackground="#2e51a2")
frame_top_vg_mal_score = Frame(frame_top_vg_label, background="#1853d9", width=98, height=115,
                                  highlightbackground="#2e51a2", highlightthickness=1)
label_top_vg_mal_score = Label(frame_top_vg_mal_score, text="MAL", font=("Verdana", 10, 'bold'),
                                  fg='white', background="#1853d9", highlightbackground="#2e51a2")
frame_top_vg_status = Frame(frame_top_vg_label, background="#1853d9", width=98, height=115,
                               highlightbackground="#2e51a2", highlightthickness=1)
label_top_vg_status = Label(frame_top_vg_status, text="Status", font=("Verdana", 10, 'bold'),
                               fg='white', background="#1853d9", highlightbackground="#2e51a2")
image_top_vg_status = ImageTk.PhotoImage(Image.open(resource_directory + "status.png"))

# Define Loading Screen
panel_load = Frame(root, background="#1f2024", width=1060, height=784,
                   highlightbackground="#2e51a2", highlightthickness=1)
progress_load = ttk.Progressbar(panel_load, orient=HORIZONTAL, length=800, mode='determinate', value=progress_var)
button = Button(panel_load)

# Anime Objects
class Anime:

    def __init__(self, ranking, image, image_hex, title, media_type, media_count,
                 season, members, score, mal_score, mal_ranking, status):

        global top_anime_count
        self.ranking = ranking
        self.ranking_x = 6
        self.image = image
        self.image_hex = image_hex
        self.title = title
        self.media_type = media_type
        self.media_count = media_count
        self.season = season
        self.members = members
        self.score = score
        self.mal_score = mal_score
        self.mal_ranking = mal_ranking
        self.status = status

        # Update Image
        data_file = temp_directory + str(self.score) + ".png"
        with open(data_file, "wb") as f:
            f.write(binascii.unhexlify(self.image_hex))
        self.image = ImageTk.PhotoImage((Image.open(data_file).resize((72, 100), Image.ANTIALIAS)))
        self.page_image = ImageTk.PhotoImage((Image.open(data_file).resize((226, 320), Image.ANTIALIAS)))

        # Define Frames
        self.panel = Frame(panel_top_anime, background="#1f2024", width=1020, height=115,
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
        self.type_label = Label(self.title_frame, text=(self.media_type + " (" + self.media_count + " eps)"),
                                font=("Verdana", 8, 'bold'), fg='grey',
                                background="#1f2024", highlightbackground="#2e51a2")
        self.season_label = Label(self.title_frame, text=self.season, font=("Verdana", 8, 'bold'),
                                  fg='grey', background="#1f2024", highlightbackground="#2e51a2")
        self.members_label = Label(self.title_frame, text=(locale.format_string("%d", int(self.members), grouping=True)
                                                           + " members"), font=("Verdana", 8, 'bold'), fg='grey',
                                   background="#1f2024", highlightbackground="#2e51a2")
        self.score_label = Label(self.score_frame, text=self.score, font=("Verdana", 11),
                                 fg='white', background="#1f2024", highlightbackground="#2e51a2")
        self.image_star = Label(self.score_frame, image=image_top_anime_star, background="#1f2024")
        self.mal_score_label = Label(self.mal_score_frame, text=self.mal_score, font=("Verdana", 11),
                                     fg='white', background="#1f2024", highlightbackground="#2e51a2")
        self.image_mal_star = Label(self.mal_score_frame, image=image_top_anime_star, background="#1f2024")
        self.image_status = Label(self.status_frame, image=image_top_anime_status, background="#1f2024")
        self.status_label = Label(self.status_frame, text=self.status, font=("Avenir", 8), fg='#1853d9',
                                  background="#1f2024", highlightbackground="#2e51a2", cursor="hand2")

        # Define Anime Page
        self.page = Frame(root, background="#1f2024", width=1060, height=784,
                          highlightbackground="#2e51a2", highlightthickness=1)
        self.page_frame_title = Frame(self.page, background="#041846", width=1060, height=32,
                                      highlightbackground="#2e51a2", highlightthickness=1)
        self.page_label_title = Label(self.page_frame_title, background="#041846", text=self.title,
                                      font=("Verdana", 11, "bold"), fg='white', highlightbackground="#041846")
        self.page_frame_image = Frame(self.page, background="#1f2024", width=246, height=753,
                                      highlightbackground="#2e51a2", highlightthickness=1)
        self.page_label_image = Label(self.page_frame_image, background="#1f2024", width=226, height=320,
                                      highlightbackground="#2e51a2", highlightthickness=1, image=self.page_image)
        self.page_frame_score = Frame(self.page, background="#1f2024", width=815, height=753,
                                      highlightbackground="#2e51a2", highlightthickness=1)

    def label_creation(self):
        def callback():
            self.page_label_title.place(x=9, y=3)
            self.page_frame_title.place(x=(-1), y=(-1))
            self.page_label_image.place(x=6, y=6)
            self.page_frame_image.place(x=(-1), y=30)
            self.page_frame_score.place(x=244, y=30)
            self.page.place(x=550, y=233)
            self.page.tkraise()

        # Set Ranking
        if int(self.ranking) < 10:
            self.ranking_x = 21

        # Place Labels
        self.ranking_label.configure(text=self.ranking)
        self.image_label.place(x=8, y=4)
        self.ranking_label.place(x=self.ranking_x, y=26)
        self.title_label.place(x=90, y=10)
        self.title_label.bind("<Button-1>", lambda e: callback())
        self.type_label.place(x=90, y=32)
        self.season_label.place(x=90, y=50)
        self.members_label.place(x=90, y=68)
        self.score_label.place(x=35, y=44)
        self.image_star.place(x=15, y=46)
        self.mal_score_label.place(x=35, y=44)
        self.image_mal_star.place(x=15, y=46)
        self.image_status.place(x=6, y=42)
        self.status_label.place(x=20, y=47)

    def ranking_creation(self):
        self.ranking_frame.place(x=(-1), y=(-1))

    def title_creation(self):
        self.title_frame.place(x=74, y=(-1))

    def score_creation(self):
        self.score_frame.place(x=729, y=(-1))

    def mal_score_creation(self):
        self.mal_score_frame.place(x=825, y=(-1))

    def status_creation(self):
        self.status_frame.place(x=921, y=(-1))

    def panel_creation(self):
        global top_anime_count, anime_panel_height

        # Place Panels
        self.panel.place(x=19, y=(45 + (top_anime_count * 114)))
        anime_panel_height = ((45 + (top_anime_count * 114)) + 115)
        panel_top_anime.configure(height=(anime_panel_height + 21))  # +1
        top_anime_count += 1

# VG Objects
class VG:
    def __init__(self, ranking, image, image_hex, title, media_type,
                 season, members, score, mal_score, status):
        global top_vg_count
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
        self.page_image = ImageTk.PhotoImage((Image.open(data_file).resize((226, 320), Image.ANTIALIAS)))

        # Define Frames
        self.panel = Frame(panel_top_vg, background="#1f2024", width=1020, height=115,
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
        self.members_label = Label(self.title_frame, text=(locale.format_string("%d", int(self.members), grouping=True)
                                                           + " members"), font=("Verdana", 8, 'bold'), fg='grey',
                                   background="#1f2024", highlightbackground="#2e51a2")
        self.score_label = Label(self.score_frame, text=self.score, font=("Verdana", 11),
                                 fg='white', background="#1f2024", highlightbackground="#2e51a2")
        self.image_star = Label(self.score_frame, image=image_top_anime_star, background="#1f2024")
        self.mal_score_label = Label(self.mal_score_frame, text=self.mal_score, font=("Verdana", 11),
                                     fg='white', background="#1f2024", highlightbackground="#2e51a2")
        self.image_mal_star = Label(self.mal_score_frame, image=image_top_anime_star, background="#1f2024")
        self.image_status = Label(self.status_frame, image=image_top_anime_status, background="#1f2024")
        self.status_label = Label(self.status_frame, text=self.status, font=("Avenir", 8), fg='#1853d9',
                                  background="#1f2024", highlightbackground="#2e51a2", cursor="hand2")

        # Define VG Page
        self.page = Frame(root, background="#1f2024", width=1060, height=784,
                          highlightbackground="#2e51a2", highlightthickness=1)
        self.page_frame_title = Frame(self.page, background="#041846", width=1060, height=32,
                                      highlightbackground="#2e51a2", highlightthickness=1)
        self.page_label_title = Label(self.page_frame_title, background="#041846", text=self.title,
                                      font=("Verdana", 11, "bold"), fg='white', highlightbackground="#041846")
        self.page_frame_image = Frame(self.page, background="#1f2024", width=246, height=753,
                                      highlightbackground="#2e51a2", highlightthickness=1)
        self.page_label_image = Label(self.page_frame_image, background="#1f2024", width=226, height=320,
                                      highlightbackground="#2e51a2", highlightthickness=1, image=self.page_image)
        self.page_frame_score = Frame(self.page, background="#1f2024", width=815, height=753,
                                      highlightbackground="#2e51a2", highlightthickness=1)

    def label_creation(self):
        def callback():
            self.page_label_title.place(x=9, y=3)
            self.page_frame_title.place(x=(-1), y=(-1))
            self.page_label_image.place(x=6, y=6)
            self.page_frame_image.place(x=(-1), y=30)
            self.page_frame_score.place(x=244, y=30)
            self.page.place(x=550, y=233)
            self.page.tkraise()

        # Set Ranking
        if int(self.ranking) < 10:
            self.ranking_x = 21

        # Place Labels
        self.ranking_label.configure(text=self.ranking)
        self.image_label.place(x=8, y=4)
        self.ranking_label.place(x=self.ranking_x, y=26)
        self.title_label.place(x=90, y=10)
        self.title_label.bind("<Button-1>", lambda e: callback())
        self.type_label.place(x=90, y=32)
        self.season_label.place(x=90, y=50)
        self.members_label.place(x=90, y=68)
        self.score_label.place(x=35, y=44)
        self.image_star.place(x=15, y=46)
        self.mal_score_label.place(x=35, y=44)
        self.image_mal_star.place(x=15, y=46)
        self.image_status.place(x=6, y=42)
        self.status_label.place(x=20, y=47)

    def ranking_creation(self):
        self.ranking_frame.place(x=(-1), y=(-1))

    def title_creation(self):
        self.title_frame.place(x=74, y=(-1))

    def score_creation(self):
        self.score_frame.place(x=729, y=(-1))

    def mal_score_creation(self):
        self.mal_score_frame.place(x=825, y=(-1))

    def status_creation(self):
        self.status_frame.place(x=921, y=(-1))

    def panel_creation(self):
        global top_vg_count, vg_panel_height

        # Place Panels
        self.panel.place(x=19, y=(45 + (top_vg_count * 114)))
        vg_panel_height = ((45 + (top_vg_count * 114)) + 115)
        panel_top_vg.configure(height=(vg_panel_height + 21))  # +1
        top_vg_count += 1

def place_frames():

    # Place Primary Buttons
    primary_button_home.place(x=0, y=200)
    primary_button_anime.place(x=80, y=200)
    primary_button_manga.place(x=163, y=200)
    primary_button_vn.place(x=246, y=200)
    primary_button_vg.place(x=309, y=200)
    primary_button_searchbar.place(x=500, y=207)
    primary_button_search.place(x=1022, y=206)
    logo_image.place(x=(-3), y=(-5))
    primary_button_frame.place(x=550, y=0)

    # Place Left Panel Frames
    panel_left_frame_1.place(x=-1, y=-1)
    panel_left_frame_2.place(x=-1, y=288)
    panel_left_anime_1.place(x=20, y=20)  # Row 1 Anime 1 Frame
    panel_left_label_temp_1.place(x=0, y=0, relwidth=1, relheight=1)  # Temp Anime 1
    root_panel_left.place(x=550, y=233)  # Left Panel

    # Place Right Panel Frames
    panel_right_label_temp_1_img.place(x=0, y=0, relwidth=1, relheight=1)
    panel_right_label_temp_2_img.place(x=0, y=0, relwidth=1, relheight=1)
    panel_right_label_temp_3_img.place(x=0, y=0, relwidth=1, relheight=1)
    panel_right_label_temp_4_img.place(x=0, y=0, relwidth=1, relheight=1)
    panel_right_label_temp_5_img.place(x=0, y=0, relwidth=1, relheight=1)
    panel_right_vn_1.place(x=23, y=33)
    panel_right_vn_2.place(x=23, y=179)
    panel_right_vn_3.place(x=23, y=325)
    panel_right_vn_4.place(x=23, y=471)
    panel_right_vn_5.place(x=23, y=617)
    root_panel_right.place(x=1288, y=233)

    # Place Top Anime Frames
    frame_top_anime_label.place(x=19, y=19)
    frame_top_anime_ranking.place(x=15, y=1)
    label_top_anime_ranking.place(x=1, y=(-1))
    frame_top_anime_title.place(x=74, y=(-1))
    label_top_anime_title.place(x=300, y=1)
    frame_top_anime_score.place(x=729, y=(-1))
    label_top_anime_score.place(x=24, y=1)
    frame_top_anime_mal_score.place(x=825, y=(-1))
    label_top_anime_mal_score.place(x=30, y=1)
    frame_top_anime_status.place(x=921, y=(-1))
    label_top_anime_status.place(x=22, y=1)
    panel_top_anime.place(x=550, y=scroll)  # Top 100 Anime (Tied to Anime Button)

# Place Loading Frames
progress_load.place(x=130, y=320)
panel_load.place(x=550, y=233)
panel_load.tkraise()

# Start Program
load_database()
raise_home_frame()
root.mainloop()
