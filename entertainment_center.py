import media
import fresh_tomatos
Zootopia=media.movies("Zootopia (2016)", "https://youtu.be/g9lmhBYB11U",
                 "https://image.tmdb.org/t/p/w600_and_h900_bestv2/sM33SANp9z6rXW8Itn7NnG1GOEs.jpg")

Minions=media.movies("Minions (2015)", "https://youtu.be/jc86EFjLFV4",
                     "https://image.tmdb.org/t/p/w600_and_h900_bestv2/q0R4crx2SehcEEQEkYObktdeFy.jpg")

Finding_Dory=media.movies("Finding Dory (2016)","https://youtu.be/JhvrQeY3doI",
                          "https://image.tmdb.org/t/p/w600_and_h900_bestv2/z09QAf8WbZncbitewNk6lKYMZsh.jpg")

School_Rock=media.movies("School of Rock (2003)","https://youtu.be/LqEszt5wG9I",
                         "https://image.tmdb.org/t/p/w600_and_h900_bestv2/cREN222Yw78zvSQ9bg17Y9QZS0c.jpg")

Maze_Runner=media.movies("The Maze Runner (2014)","https://youtu.be/64-iSYVmMVY",
                         "https://image.tmdb.org/t/p/w600_and_h900_bestv2/coss7RgL0NH6g4fC2s5atvf3dFO.jpg")


films=[Zootopia,Minions,Finding_Dory,School_Rock,Maze_Runner]
fresh_tomatos.open_movies_page(films)