from scipy import misc
import numpy as np
import glob
import sys

if __name__ == "__main__":
	data_folder = sys.argv[1]
	data_array = []
	labels_array = []
	class_number = 0
	for dr in glob.glob(data_folder + "*"):
		print dr
		for path in glob.glob(dr + "/*.png"):
			data_array.append(misc.imread(path,mode='RGB'))
			labels_array.append(class_number)
		class_number += 1
	data_array = np.array(data_array)
	labels_array = np.array(labels_array)
	print data_array.shape, labels_array.shape
	np.save(data_folder + sys.argv[2], data_array)
	np.save(data_folder + sys.argv[2] + '_labels', labels_array)