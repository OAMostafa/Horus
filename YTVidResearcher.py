"""
YTVidResearcher.py

Module to search and retrieve youtube video links
"""

from youtubesearchpython import VideosSearch

class VidResearcher:
    def __init__(self):
        """
        Simple initializer method for the class.
        """
    
    def search(self, search_text, result_ranking=0):
        """
        Method to search for the desired music video to listen to.
        
        IMPORTANT: This class contains much more vid information if needed
        
        Parameters
        ----------
        search_text: str
            The text that contains the search terms for the music video
        result_ranking: int (default: 0)
            The int that represents which vid we want to play depending on search ranking

        Returns
        -------
        str
            A <str> made up of the YT link to the desired music video
        """
        videosSearch = VideosSearch(search_text)

        vid_link = videosSearch.result()['result'][result_ranking]['link']

        return vid_link


def main():
    vr = VideosSearch("kanye west i wonder")
    
    links = []
    
    for x in range(0,3):
        print("going")
        links.append(vr.result()['result'][x]['link'])
    
    print(links)

if __name__ == "__main__":
    main()

"""
{
    "result": [
        {
            "type": "video",
            "id": "E07s5ZYygMg",
            "title": "Harry Styles - Watermelon Sugar (Official Video)",
            "publishedTime": "6 months ago",
            "duration": "3:09",
            "viewCount": {
                "text": "162,235,006 views",
                "short": "162M views"
                    },
            "thumbnails": [
                {
                    "url": "https://i.ytimg.com/vi/E07s5ZYygMg/hq720.jpg?sqp=-oaymwEjCOgCEMoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLAOWBTE1SDrtrDQ1aWNzpDZ7YiMIw",
                    "width": 360,
                    "height": 202
                },
                {
                    "url": "https://i.ytimg.com/vi/E07s5ZYygMg/hq720.jpg?sqp=-oaymwEXCNAFEJQDSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLD7U54pGZLPKTuMP-J3kpm4LIDPVg",
                    "width": 720,
                    "height": 404
                }
            ],
            "descriptionSnippet": [
                {
                    "text": "This video is dedicated to touching. Listen to Harry Styles' new album 'Fine Line' now: https://HStyles.lnk.to/FineLineAY Follow ..."
                }
            ],
            "channel": {
                "name": "Harry Styles",
                "id": "UCZFWPqqPkFlNwIxcpsLOwew",
                "thumbnails": [
                    {
                        "url": "https://yt3.ggpht.com/a-/AOh14GgNUvHxwlnz4RpHamcGnZF1px13VHj01TPksw=s68-c-k-c0x00ffffff-no-rj-mo",
                        "width": 68,
                        "height": 68
                    }
                ],
                "link": "https://www.youtube.com/channel/UCZFWPqqPkFlNwIxcpsLOwew"
            },
            "accessibility": {
                "title": "Harry Styles - Watermelon Sugar (Official Video) by Harry Styles 6 months ago 3 minutes, 9 seconds 162,235,006 views",
                "duration": "3 minutes, 9 seconds"
            },
            "link": "https://www.youtube.com/watch?v=E07s5ZYygMg",
            "shelfTitle": null
        }
    ]
}

videosSearch = VideosSearch('Kanye west I wonder', limit = 2)

dummy = videosSearch.result()['result'][0]

print(videosSearch.result())
"""