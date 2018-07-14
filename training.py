from glob import glob
import pandas as pd
import numpy as np
import cv2
from model import *
from util import *

n_epochs = 350
learning_rate_val = 0.0003
weight_decay_rate =  0.00001
momentum = 0.9
batch_size = 500
lambda_recon = 0.9
lambda_adv = 0.1

overlap_size = 7
hiding_size = 64

dataset_path =" "
result_path = ""

