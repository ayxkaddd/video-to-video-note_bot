import os


class Resize:

	""""that is so easy, i just use ffmpeg
	 and search at google how to resize video with ffmpeg lol"""

	def __init__(self, path_from, path_to):
		self.path_from = path_from
		self.path_to = path_to


	def res_video(self):
		command = f'ffmpeg -i {self.path_from} -vf scale=460:460 {self.path_to}'
		os.system(f'{command}')
		os.system(f'rm {self.path_from}')
