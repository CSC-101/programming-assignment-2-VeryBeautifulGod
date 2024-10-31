import data
from data import Point, Rectangle, Duration, Song
import hw2
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_rectangle_1(self):
        input1 = Point(2, 2)
        input2 = Point(10, 10)
        result = hw2.create_rectangle(input1, input2)
        expected = Rectangle(Point(2, 10), Point(10, 2))
        self.assertEqual(expected, result)

    def test_create_rectangle_2(self):
        input1 = Point(-5, -5)
        input2 = Point(5, 5)
        result = hw2.create_rectangle(input1, input2)
        expected = Rectangle(Point(-5, 5), Point(5, -5))
        self.assertEqual(expected, result)

    # Part 2
    def test_shorter_duration_than_1(self):
        input1 = Duration(1, 30)
        input2 = Duration(2, 0)
        result = hw2.shorter_duration_than(input1, input2)
        expected = True
        self.assertEqual(expected, result)

    def test_shorter_duration_than_2(self):
        input1 = Duration(3, 45)
        input2 = Duration(3, 30)
        result = hw2.shorter_duration_than(input1, input2)
        expected = False
        self.assertEqual(expected, result)

    # Part 3
    def test_song_shorter_than_1(self):
        song1 = Song("Artist A", "Song A", Duration(2, 30))
        song2 = Song("Artist B", "Song B", Duration(3, 15))
        song3 = Song("Artist C", "Song C", Duration(4, 0))
        songs = [song1, song2, song3]
        max_duration = Duration(3, 0)
        result = hw2.song_shorter_than(songs, max_duration)
        expected = [song1]
        self.assertEqual(expected, result)

    def test_song_shorter_than_2(self):
        song1 = Song("Artist D", "Song D", Duration(5, 0))
        song2 = Song("Artist E", "Song E", Duration(4, 45))
        songs = [song1, song2]
        max_duration = Duration(4, 30)
        result = hw2.song_shorter_than(songs, max_duration)
        expected = []
        self.assertEqual(expected, result)

    # Part 4
    def test_running_time_1(self):
        song1 = Song("Decemberists", "June Hymn", Duration(4, 30))
        song2 = Song("Broken Bells", "October", Duration(3, 40))
        song3 = Song("Kansas", "Dust in the Wind", Duration(3, 29))
        song4 = Song("Local Natives", "Airplanes", Duration(3, 58))
        songs = [song1, song2, song3, song4]
        playlist = [0, 2, 1, 3, 0]
        result = hw2.running_time(songs, playlist)
        expected = Duration(20, 7)
        self.assertEqual(expected, result)

    def test_running_time_2(self):
        song1 = Song("Artist A", "Song A", Duration(2, 15))
        song2 = Song("Artist B", "Song B", Duration(3, 30))
        song3 = Song("Artist C", "Song C", Duration(4, 50))
        songs = [song1, song2, song3]
        playlist = [1, 0, 3, -1]
        result = hw2.running_time(songs, playlist)
        expected = Duration(5, 45)
        self.assertEqual(expected, result)

    # Part 5
    def test_validate_route_1(self):
        city_links = [
            ['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston']
        ]
        route = ['san luis obispo', 'santa margarita', 'atascadero']
        result = hw2.validate_route(city_links, route)
        self.assertTrue(result)

    def test_validate_route_2(self):
        city_links = [
            ['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston']
        ]
        route = ['san luis obispo', 'atascadero']
        result = hw2.validate_route(city_links, route)
        self.assertFalse(result)

    # Part 6
    def test_longest_repetition_1(self):
        result = hw2.longest_repetition([1, 1, 2, 2, 1, 1, 1, 3])
        self.assertEqual(result, 4)

    def test_longest_repetition_2(self):
        result = hw2.longest_repetition([5, 5, 5, 1, 1, 1, 2, 2, 2, 2])
        self.assertEqual(result, 6)




if __name__ == '__main__':
    unittest.main()
