
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from visdom import Visdom
import numpy as np
import math
import os.path
import getpass
from sys import platform as _platform
from six.moves import urllib
import numpy as np

import pylab as plt
import numpy as np
from PIL import Image
import torchvision.transforms as transforms

viz = Visdom()

try:
    # video demo: download video from http://media.w3.org/2010/05/sintel/trailer.ogv
    #video_url = 'http://media.w3.org/2010/05/sintel/trailer.ogv'
    # linux
    if _platform == "linux" or _platform == "linux2":
        videofile = '/workspace/visdom/trailer.ogv' 
    ## MAC OS X
    #elif _platform == "darwin":
    #    videofile = '/Users/%s/trailer.ogv' % getpass.getuser()
    # download video
    #urllib.request.urlretrieve(video_url, videofile)

    if os.path.isfile(videofile):
        viz.video(videofile=videofile)
except ImportError:
    print('Skipped video example')


#assert viz.check_connection()
#viz.close()


# image demo
image = Image.open('/workspace/visdom/rnet_faces.png')
image = transforms.ToTensor()(image)
viz.image(img=image, win='image', opts={'title': 'show image'})

