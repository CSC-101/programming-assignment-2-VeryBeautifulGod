import data

from data import Point, Rectangle, Duration, Song
from typing import Optional
# Write your functions for each part in the space below.

# Part 1
def create_rectangle(point1: Point, point2: Point) -> Rectangle:
    min_x = min(point1.x, point2.x)
    max_x = max(point1.x, point2.x)
    min_y = min(point1.y, point2.y)
    max_y = max(point1.y, point2.y)
    top_left = Point(min_x, max_y)
    bottom_right = Point(max_x, min_y)
    return Rectangle(top_left, bottom_right)


# Part 2
def shorter_duration_than(duration1: Duration, duration2: Duration) -> bool:
    total_seconds1 = duration1.minutes * 60 + duration1.seconds
    total_seconds2 = duration2.minutes * 60 + duration2.seconds
    return total_seconds1 < total_seconds2


# Part 3
def song_shorter_than(songs: list[Song], max_duration: Duration) -> list[Song]:
    max_duration_seconds = max_duration.minutes * 60 + max_duration.seconds
    result = []

    for song in songs:
        song_duration_seconds = song.duration.minutes * 60 + song.duration.seconds
        if song_duration_seconds < max_duration_seconds:
            result.append(song)

    return result

# Part 4
def running_time(songs: list[Song], playlist: list[int]) -> Duration:
    total_seconds = 0

    for song_index in playlist:
        if 0 <= song_index < len(songs):
            total_seconds += (songs[song_index].duration.minutes * 60 + songs[song_index].duration.seconds)

    total_minutes = total_seconds // 60
    total_seconds = total_seconds % 60

    return Duration(total_minutes, total_seconds)

# Part 5
def validate_route(city_links: list[list[str]], route: list[str]) -> bool:
    if len(route) <= 1:
        return True

    for i in range(len(route) - 1):
        current_city = route[i]
        next_city = route[i + 1]
        link_found = False

        for link in city_links:
            if (current_city == link[0] and next_city == link[1]) or (current_city == link[1] and next_city == link[0]):
                link_found = True
                break

        if not link_found:
            return False

    return True
# Part 6
def longest_repetition(numbers: list[int]) -> Optional[int]:
    if not numbers:
        return None

    max_length = 0
    max_index = None
    current_length = 1

    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i - 1]:
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
                max_index = i - current_length
            current_length = 1

    if current_length > max_length:
        max_index = len(numbers) - current_length

    return max_index