class Song(object):

    def __init__(self, lyrics, year, creator):
        self.lyrics = lyrics
        self.year = year
        self.creator = creator

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

    def info(self):
        print(f"The song was created on {self.year}.")
        print(f"It's from the band {self.creator}.")

# happy_bday = Song(["Happy birthday to you",
#                     "I don't want to get sued",
#                     "So I'll stop right there"])
#
# bulls_on_parade = Song(["They rally around tha family",
#                         "With pockets full of shells"])
#
# happy_bday.sing_me_a_song()
# bulls_on_parade.sing_me_a_song()
#
# print(happy_bday.lyrics)
# print(bulls_on_parade.lyrics)


# STUDY DRILL
message_to_you_rudy = Song(["Stop your messing around",
                       "Better think of your future",
                        "Time straigthen right out"], 1979, "The Specials")

son_of_my_father = Song(["Be just like your lad",
                    "Follow in the same tradition..."], 1972, "Chicory Tip")

son_of_my_father.sing_me_a_song()
son_of_my_father.info()

message_to_you_rudy.sing_me_a_song()
message_to_you_rudy.info()
