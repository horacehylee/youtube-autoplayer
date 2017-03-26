import vlc


def playAll(file_paths):
    "Play all file_paths"
    vlc_instance = vlc.Instance()

    media_list = vlc_instance.media_list_new()
    for file_path in file_paths:
        media_list.add_media(vlc_instance.media_new(file_path))

    vlc_player = vlc_instance.media_list_player_new()
    vlc_player.set_media_list(media_list)

    vlc_player.play()
