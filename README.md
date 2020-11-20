
<img src="examples/example_gif.gif" alt='Example gif' width="400"/>  <img src="blended_image.png" alt='Blended Image' width="400"/> 
<br>
<br>

__Blend video frames, or images, to make nice visualisations!__
<br>
<br>

## Try it:

__step 1)__ Download repo:
<br>
`git clone https://github.com/nemanja-rakicevic/frame_blender.git; cd frame_blender`

__step 2)__ Prerequisites:
<br>
`pip install -r requirements.txt`

__step 3)__ Run!
<br>
`python blend_frames.py --load_gif examples/example_gif.gif -sf 5`
<br>
<br>

## Description

Scripts for manipulating the open browser tabs:

__blend_frames.py__:
<br>
Create an image of blended frames, from various sources:
<br>
`-v, --load_video`: pass a path to the video file.
<br>
`-g, --load_gif`: pass a path to the .gif file.
<br>
`-d, --load_dir`: pass a path to the directory containing a sequence of images.
<br>
It is necessary that the images are the same size, and would be useful to also pass the image type: 
<br>
`-it, --image_type`: the default is `'png'`.

It is possible to limit the number of frames used:
<br>
`-mf, --max_frames`: by default all frame are used.
<br>
In order to skip several frames, pass:
<br>
`-sf, --skip_frames`: the default is tu use all frames.


__(TODO) make_gif.py__:
<br>
Make a gif either from a video file or a sequence of images.
<br>
<br>

__(TODO) make_image_sequence.py__:
<br>
Make a sequence of images either from a video file or gif.
<br>
<br>


NOTE: Large files require a lot of memory, use with caution!
<br>
(TODO) Rewrite as iterators to better manage the memory.
