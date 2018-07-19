import csv
import os.path

class OutputFormatter(object):

    def __init__(self, dict_data, file_path="output/output.csv"):
        self.data = dict_data
        self.file_path = file_path

    def __file_exists(self):
        if os.path.exists(self.file_path):
            pass
        else:
            with open(self.file_path, "w", newline='') as outfile:
                writer = csv.writer(outfile)
                writer.writerow(self.data.keys())

    def __clean_data_for_export(self):
        cleaned = {}
        for i in self.data.keys():
            if isinstance(self.data[i], list):
                cleaned[i] = self.data[i]
            else:
                # workaround to zip all data from one
                # api call since the annual data isn't
                # an array
                cleaned[i] = [''] * 12
                cleaned[i][0] = self.data[i]
        return cleaned

    def write_csv(self):
        self.__file_exists()
        cleaned_data = self.__clean_data_for_export()
        with open(self.file_path, "a") as outfile:
            writer = csv.writer(outfile)
            writer.writerows(zip(*cleaned_data.values()))
        
