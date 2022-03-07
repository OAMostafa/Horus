import unittest

from YTVidResearcher import VidResearcher


# Overview of this test class should be able to test out the vidResearcher python file

"""
future tests should include:
    testing how many Yt vid links are returned whenever we search.

    sanity check of YT algorithm i.e when we search a music vid, the search text should at least be reflected somewhere in the vid info


Current list ranking:
<
    "https://www.youtube.com/watch?v=UYXa2yBF5ms",
    "https://www.youtube.com/watch?v=xyfoyugCB8Y",
    "https://www.youtube.com/watch?v=CUK_6iJgJpU"
>
"""

links_rankings = ["https://www.youtube.com/watch?v=UYXa2yBF5ms", 
                  "https://www.youtube.com/watch?v=xyfoyugCB8Y", 
                  "https://www.youtube.com/watch?v=CUK_6iJgJpU"]

class TestResearcher(unittest.TestCase):
    
    """
        The purpose of this test is to make sure the <search()> method returns the default ranking
        which is the first one (number 0). This test can be a bit inconsistent since it depends on the 
        youtube algorithm, but the whole bot is based on it so \../.
    """
    def test_search_default_ranking_parameter(self):
        vr = VidResearcher()
        
        test_search_text = ("Kanye west I wonder")
        
        link = vr.search(test_search_text)
        
        self.assertEqual(link, links_rankings[0], "The search functionality returned a 1st-linked link different than before")
    
    """
        The purpose of this test is to make sure the <search()> method returns the correct ranking
        passed to it.
    """
    def test_search_custom_ranking_parameter(self):
        vr = VidResearcher()
        
        test_search_text = ("Kanye west I wonder")
        
        link = vr.search(test_search_text, 1)
        
        self.assertEqual(link, links_rankings[1], "The search functionality returned a 2nd-linked link different than before")
        
        link = vr.search(test_search_text, 2)
        
        self.assertEqual(link, links_rankings[2], "The search functionality returned a 3rd-linked link different than before")
    