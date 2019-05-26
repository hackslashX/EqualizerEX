import sys
import os
from mutagen.flac import FLAC, Picture
from mutagen import File
from tinytag import TinyTag
from scipy import io
import numpy as np
import datetime

dt = datetime.datetime.now()
ext=os.path.splitext(sys.argv[1])[1]
tag = TinyTag.get(sys.argv[1])
dict = {'album':'','disc':'','track':'','year':'','genre':'','tt':''}
dict['album']=np.array([tag.album])
dict['disc']=np.array([tag.disc])
dict['genre']=np.array([tag.genre])
dict['track']=np.array([tag.track])
dict['year']=np.array([tag.year])
dict['tt']=np.array(dt.strftime('%Y %m %d %H %M %S'))
if not tag.genre:
    dict['genre']=np.array('None')
if not tag.album:
    dict['album']=np.array('None')
if not tag.disc:
    dict['disc']=np.array('None')
if not tag.year:
    dict['year']=np.array('None')
if ext == '.flac':
    tag=FLAC(sys.argv[1])
    tag=tag.pictures
    for p in tag:
        if p.type == 3:
            with open(np.array2string(dict['tt'])+'.jpg', "wb") as f:
                f.write(p.data)
if ext == '.mp3':
    file=File(sys.argv[1])
    pic=file.tags['APIC:'].data
    with open(np.array2string(dict['tt'])+'.jpg', "wb") as f:
        f.write(pic)

io.savemat('info.mat',dict)
