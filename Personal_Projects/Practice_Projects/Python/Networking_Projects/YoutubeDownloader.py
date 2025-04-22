from pytube import YouTube #importing pytube also imports pytube3


#asking user for input

#ask for link
def giveLink():
    link = input("Enter the link: ")

    #   This Youtube object takes a link argument
    return YouTube(link)    #  Returns a Youtube object

def revealVideoInfo(youtubeObj):

    #   Video Title
    print("Title: ", youtubeObj.title)

    #   Number of views of video
    print("Number of views: ", youtubeObj.views)

    #   Video Length
    print("Video lenght: ", youtubeObj.length, "seconds")

    #   Video's Description
    print("Description: ", youtubeObj.description)

    #   Rating
    print("Ratings: ", youtubeObj.rating)

    ##  More operations can be found in the official documentation of pytube3

def printStreamFilter(youtubeObj, audio, video, prog):
    if (audio):
        #   This filters only audio-only streams
        print(youtubeObj.streams.filter(only_audio=audio))
    elif(video):
        #   Filters only video streams
        print(youtubeObj.streams.filter(only_video=video))
    elif(prog):
        #   To filter progressive streams
        print(youtubeObj.streams.filter(progressive=prog))
    else:
        #   To see the different available streams
        #   There can be both audio and video streams
        #   One can filter either one wanted
        #   There are also progressive and Dash streams...
        print(youtubeObj.streams)

def Download(ytS, path=None):
    revealVideoInfo(ytS)
    if path == None:
        #   This will download the preferred stream and save to current directory
        ytS.download()
    else:
        #   Or can specify absolute path to store in system
        ytS.download(path)


def main():
    yt = giveLink()


    #   To get the highest resolution progressive stream
    ytStream = yt.streams.get_highest_resolution()

    ##  Can even choose the stream using its tag that was printed...
    ##  when listing the avialable streams using:
    #   ytStream = yt.streams.get_by_itag('22')   #

    Download(ytStream)


main()



