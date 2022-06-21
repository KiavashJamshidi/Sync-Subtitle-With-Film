import os
def makeSubtitlesFilmsList(subtitles,films,subDir,filmDir):

    os.chdir(subDir)
    for file in os.listdir():
        if os.path.splitext(file)[1].lower() == ".srt":
            subtitles.append(os.path.splitext(file)[0])

    os.chdir(filmDir)
    for file in os.listdir():
        if os.path.splitext(file)[1].lower() == ".mkv":
            films.append(os.path.splitext(file)[0])

def renameFiles(subtitles,films):
    for sub in range(len(films)):
        os.rename(subtitles[sub] + ".srt",films[sub] + ".srt")
            
if __name__ == '__main__':
    subtitles , films = [] , []
    filmDir = input("Enter the film directory name: ").strip()
    subDir = input("Enter the subtitles directory name: ").strip()
    makeSubtitlesFilmsList(subtitles,films,subDir,filmDir)
    renameFiles(subtitles,films)
    print()
    print("Done ;)")
    print()