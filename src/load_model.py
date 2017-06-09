import numpy as np
import tensorflow as tf
import sys

def load_model(filename):
	f = tf.gfile.FastGFile(filename)
	graph_def = tf.GraphDef()
	graph_def.ParseFromString(f.read())
	tf.import_graph_def(graph_def, name='')
	return graph_def


if __name__ == '__main__':
	graph_def = load_model(sys.argv[1])