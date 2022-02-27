from utils import get_an_image, get_upper_frame


class ImageProcessor:
    """This class processes ASC-II images.

    An object is initiated with a URL.
    """
    def __init__(self, url: str):
        """
        Initiate an Image object with a URL.
        :param url: a URL pointing to an ASC-II image.
        """
        self.url = url
        self.data = get_an_image(url)

    def print(self):
        """A method to print the ASC-II image with a frame around it,"""
        data_array_with_frame = ['|' + data + '|' for data in self.data]
        tight_frame_border = get_upper_frame(self.data)
        data_to_print = (
                [tight_frame_border] +
                data_array_with_frame +
                [tight_frame_border]
        )
        for data_point in data_to_print:
            print(data_point + "\n")

    def crop(self):
        """
        Crop the image, i.e. shrink the image down to the smallest
        rectangular area.

        Basically, it takes a few steps:
        1. Get the first and last line in which the string is not pure space.
        2. Get the most left and most right position indices.
        3. Crop based on the four indices.
        """
        data_to_process = self.data
        indexes_list = [[(i, s) for i, s in enumerate(sss) if s.strip()]
                        for sss in data_to_process]

        first_indices = []
        last_indices = []
        for i, array_ in enumerate(indexes_list[:-1]):
            if not array_ and indexes_list[i+1]:
                first_indices.append(i)
            if array_ and not indexes_list[i+1]:
                last_indices.append(i)
        first_index = first_indices[0]
        last_index = last_indices[-1]
        new_data = data_to_process[first_index:last_index+1]
        new_indexes_list = indexes_list[first_index:last_index+1]
        leftist_indexes = [array_[0][0] for array_ in new_indexes_list if array_]
        rightist_indexes = [array_[-1][0] for array_ in new_indexes_list if array_]
        leftist_index = min(leftist_indexes)
        rightist_index = max(rightist_indexes)
        self.data = [data[leftist_index:rightist_index+1] for data in new_data]

    def fill(self, x, y, fill_char):
        # ran out of time
        pass
