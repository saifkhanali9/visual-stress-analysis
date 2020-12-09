import os
import numpy


class Utils:
    """
        A class for common misc. functions
    """

    @staticmethod
    def file_slection(path: str):
        """
        Prompts the user to select a file from the ones present in path
        :param path:
        :return: None
        """
        files = os.listdir(path)
        print("Select a file:")
        for i in range(len(files)):
            print(f"[{i}]: {files[i]}")
        return int(input())

    @staticmethod
    def get_range_indeces(data: numpy.ndarray, min_val: float, max_val: float):
        """
        Returns the indices of data s.t. data[min_index:max_index] returns the range [min_val, max_val] of values in
        data.
        :param data: A 1D numpy array
        :param min_val:
        :param max_val:
        :return:
        """
        min_index = data.shape[0]
        found_smallest = False
        max_index = 0
        for index in range(data.shape[0]):
            if min_val < data[index] and not found_smallest:
                min_index = index
                found_smallest = True
            if max_val > data[index]:
                max_index = index
        return min_index, min(max_index+1, data.shape[0]-1)

