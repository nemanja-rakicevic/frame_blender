
"""
Author:         Nemanja Rakicevic
Date:           November 2020
Description:
                Create an image of blended frames.
                Frames can e extracted from video files, .gif files or loaded
                from a directory with images.

                It is possible to select the "skip_rate".

                The transparency of each frame is based on the number of images.
"""

import os
import cv2
import glob
import imageio
import argparse


def get_args():
    """Extract script arguments."""
    parser = argparse.ArgumentParser()

    parser.add_argument('-v', '--load_video',
                        default=None,
                        help="Path to the video file.")

    parser.add_argument('-g', '--load_gif',
                        default=None,
                        help="Path to the .gif file.")

    parser.add_argument('-d', '--load_dir',
                        default=None,
                        help="Path to the directory containing image files.")

    parser.add_argument('-it', '--img_type',
                        default='png',
                        help="tye of images in the directory.")

    parser.add_argument('-save', '--save_path',
                        default=None,
                        help="Path to where to save the blended image.")

    parser.add_argument('-sf', '--skip_frames',
                        default=None, type=int,
                        help="Select the frame skip rate.")

    parser.add_argument('-mf', '--max_frames',
                        default=None, type=int,
                        help="Select the frame skip rate.")

    return parser.parse_args()


def load_from_video(load_video, max_frames, skip_frames, **kwargs):
    """Load image frames from a video file."""
    video_frames = cv2.VideoCapture(load_video)
    n_frames = int(video_frames.get(cv2.CAP_PROP_FRAME_COUNT))
    max_frames = n_frames if max_frames is None else max_frames
    skip_frames = skip_frames if skip_frames is not None \
        and skip_frames < min(n_frames, max_frames) else 1
    img_sequence = []
    for frame in range(0, min(n_frames, max_frames)):
        success, image = video_frames.read()
        if success:
            if frame % skip_frames == 0:
                img_sequence.append(image)
        else:
            break
    return img_sequence


def load_from_gif(load_gif, max_frames, skip_frames, **kwargs):
    """Load image frames from a gif file."""
    gif_frames = imageio.mimread(load_gif, memtest=False)
    n_frames = len(gif_frames)
    max_frames = n_frames if max_frames is None else max_frames
    skip_frames = skip_frames if skip_frames is not None \
        and skip_frames < min(n_frames, max_frames) else 1
    img_sequence = gif_frames[:max_frames]
    img_sequence = img_sequence[::skip_frames]
    img_sequence = [
        cv2.cvtColor(img, cv2.COLOR_RGB2BGR) for img in img_sequence]
    return img_sequence


def load_from_directory(load_dir, img_type, max_frames, skip_frames, **kwargs):
    """Load image frames from a directory of images."""
    file_list = sorted(
        glob.glob(os.path.join(load_dir, '*.{}'.format(img_type))))
    n_frames = len(file_list)
    max_frames = n_frames if max_frames is None else max_frames
    skip_frames = skip_frames if skip_frames is not None \
        and skip_frames < min(n_frames, max_frames) else 1
    file_list = file_list[:max_frames]
    file_list = file_list[::skip_frames]
    img_sequence = [cv2.imread(img) for img in file_list]
    return img_sequence


def overlay_images(img_sequence, save_path, **kwargs):
    """Take the image sequence and blend the images with equal weight."""
    save_path = '.' if save_path is None else save_path
    w = 1. / len(img_sequence)
    blended_img = sum([w * img for img in img_sequence])
    cv2.imwrite(os.path.join(save_path, "blended_image.png"), blended_img)


if __name__ == "__main__":
    args = get_args()
    if args.load_video is not None:
        img_sequence = load_from_video(**vars(args))
        source = args.load_video
    elif args.load_gif is not None:
        img_sequence = load_from_gif(**vars(args))
        source = args.load_gif
    elif args.load_dir is not None:
        img_sequence = load_from_directory(**vars(args))
        source = args.load_dir + ' directory'
    else:
        raise AttributeError("No file given!")
    overlay_images(img_sequence, **vars(args))
    print("\n\n>>> DONE. Blended image created from: '{}'\n".format(source))
