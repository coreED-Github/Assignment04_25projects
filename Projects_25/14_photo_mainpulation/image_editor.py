from PIL import Image
import filters
import os

class ImageEditor:
    def __init__(self, path):
        if not os.path.exists(path):
            raise FileNotFoundError("Image path not found. Please check the path and try again.")

        try:
            self.original = Image.open(path)
            self.edited = self.original.copy()
        except Exception as e:
            raise Exception(f"Unable to open the image. Error: {e}")

    def apply(self, filter_name, *args):
        if hasattr(filters, filter_name):
            func = getattr(filters, filter_name)
            self.edited = func(self.edited, *args)
        else:
            print(f"Filter '{filter_name}' not found.")

    def save(self, path):
        self.edited.save(path)

    def show(self):
        self.edited.show()
# from PIL import Image
# import filters

# class ImageEditor:
#     def __init__(self, path):
#         self.original = Image.open(path)
#         self.edited = self.original.copy()

#     def apply(self, filter_name, *args):
#         if hasattr(filters, filter_name):
#             func = getattr(filters, filter_name)
#             self.edited = func(self.edited, *args)
#         else:
#             print(f"Filter '{filter_name}' not found.")

#     def save(self, path):
#         self.edited.save(path)

#     def show(self):
#         self.edited.show()