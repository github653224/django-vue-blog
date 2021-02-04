from mutagen import File
import os

# afile = File('some.mp3')  # mutagen can automatically detect format and type of tags
# artwork = afile.tags['APIC:e'].data  # access APIC frame and grab the image
# with open('image.jpg', 'wb') as img:
#     img.write(artwork)  # write artwork to new image

root = '/root/'
file_list = os.listdir(root)
music_list = [i for i in file_list if i.endswith('mp3')]
for i in music_list:
    afile = File(root+'/'+i)
    artwork = afile.tags['APIC:'].data
    with open('%s.jpg' % i.split('.')[0], 'wb') as f:
        f.write(artwork)