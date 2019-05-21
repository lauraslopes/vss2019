#!/bin/bash


#v4l2-ctl -d /dev/video0 --all
# USB 3.0: 1280x960 @45fps, 1280x720 @60fps, 640x480 @80fps, 320x240 @160fps
# USB 2.0: 1280x960 @22.5fps, 1280x720 @30fps, 640x480 @80fps, 320x240 @160fps
### result:
###    white_balance_red_component (int)    : min=0 max=250 step=1 default=64 value=128
###   white_balance_blue_component (int)    : min=0 max=250 step=1 default=64 value=100
###                           gain (int)    : min=0 max=255 step=1 default=64 value=160
###              exposure_absolute (int)    : min=1 max=625 step=1 default=128 value=128



v4l2-ctl -d /dev/video0 -c white_balance_red_component=150 -c white_balance_blue_component=140 -c gain=160 -c exposure_absolute=60

