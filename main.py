from typing import List
import cv2
import numpy as np
import pyautogui
from mss import mss
from yeelight import SmartBulb

bulb = SmartBulb('192.168.1.26')

screen_size = pyautogui.size()
mon = {'top': int(
	screen_size[1] / 2), 'left': int(screen_size[0] / 2), 'width': 1, 'height': 1}

sct = mss()


def bulb_set_rgb(rgb: List):
	bulb.set_rgb(int(rgb[0]), int(rgb[1]), int(rgb[2]))


prev_rgb = np.array([0, 0, 0])

while True:
	sct_img = sct.grab(mon)

	img = np.array(sct_img)
	img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)[0][0]

	if (prev_rgb == img_rgb).all():
		continue

	prev_rgb = img_rgb
	bulb_set_rgb(img_rgb)

	print(img_rgb)

	cv2.waitKey(750)

	# print(img_rgb)

	# cv2.namedWindow('Screen Point', cv2.WINDOW_KEEPRATIO)
	# cv2.imshow('Screen Point', img)

	# if cv2.waitKey(1000) & 0xFF == ord('q'):
	# 	cv2.destroyAllWindows()
	# 	break
