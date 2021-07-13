import json
def read_json_file():
    input_file_ptr = open('songs.json', "r")
    outer_dic = json.load(input_file_ptr)
    value = outer_dic.get("songlist")
    input_file_ptr.close()
    return value

def user_choose(list_of_all_songs):
    playlist = []
    while True:
        print("Here are your song options:\n")
        c = 1
        for song in list_of_all_songs:
           title = song.get("title")
           artist = song.get("artist")
           print(f"{c}. {title} by {artist}")
           c += 1

        print("\nChoose a song a song to add to your playlist")
        num_chosen = int(input("Enter the song number\n>"))
        song_dict_chosen =  list_of_all_songs[num_chosen - 1]
        song_id = song_dict_chosen.get("id")
        title = song_dict_chosen.get("title")
        artist = song_dict_chosen.get("artist")
        year = song_dict_chosen.get("year")
        genre = song_dict_chosen.get("genre")

        inner_list = list()
        inner_list.append(song_id)
        inner_list.append(title)
        inner_list.append(artist)
        inner_list.append(year)
        inner_list.append(genre)
        playlist.append(inner_list)

        choose_again = input("\nDo you want to choose another song? Y or N \n>").upper()
        if choose_again == 'N':
            break
    return playlist

def write(two_d_structure):
    output_file_ptr = open("playlist.csv", "w")
    output_file_ptr.write("Number,Song Title,Artist,Year,Genre\n")
    for song_inner_list in two_d_structure:
        song_id = song_inner_list[0]
        title = song_inner_list[1]
        artist = song_inner_list[2]
        year = song_inner_list[3]
        genre = song_inner_list[4]
        output_file_ptr.write(str(song_id) + "," + title + "," + artist + "," + str(year) + "," + genre + "\n")
    output_file_ptr.close()




def main():
    list_of_all_songs = read_json_file()
    two_d_structure_of_songs = user_choose(list_of_all_songs)
    write(two_d_structure_of_songs)

main()
