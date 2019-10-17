import cv2


class Rewind:
	def __init__(self, video):
		self.userFlag = True
		self.video = video


	def callback(self, value):
		if self.userFlag == True:
			self.video.set(cv2.CAP_PROP_POS_FRAMES, value)
		

	def scroll(self, windowName, trackbarName):
		totalFrames = int(self.video.get(cv2.CAP_PROP_FRAME_COUNT))
		cv2.namedWindow(windowName)
		cv2.createTrackbar(trackbarName, windowName, 0, totalFrames, self.callback)

		def wrapFunction(func):

			def run(frame):
				currentPos = int(self.video.get(cv2.CAP_PROP_POS_FRAMES))

				if (currentPos % 5 == 0):
					self.userFlag = False
					cv2.setTrackbarPos(trackbarName, windowName, currentPos)
				self.userFlag = True
				
				image = func(frame)
				cv2.imshow(windowName, image)

				return image

			return run
		return wrapFunction
