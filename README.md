# Raspberry Pi 2 Video Player

## Brief

Video projection systems for running two slightly different demos: 

### System 1

*   RPi with HDMI display
*   Up to 30 videos on supplied on a USB key
*   Motion sensor (ultrasonic or PIR) connected to GPIO pin - digital input
*   Blank screen to start, on trigger shows a random video from the USB key files

### System 2

*   RPi with HDMI display
*   Up to 30 videos on supplied on a USB key formatted FAT
*   Motion sensor (ultrasonic or PIR) connected to GPIO pin - digital input
*   When not triggered, keeps playing a specific file (blank.mp4)
*   On trigger shows a random video from the USB key files (but not blank.mp4)

## USB Key Format

*   USB keys should be fomatted with a FAT filesystem in an MSDOS partition table
*   All media files to be played should be in the root directory of the USB key
*   Settings may be sent to the player software using a file named *vidpi.ini* in the root directory of the USB key

## INI File Options

If a USB key contains a file named *vidpi.ini*, it will be read when the USB key is inserted. The INI file should contain a section *[vidpi]* which contains settings for the player software. 

### Example vidpi.ini File

    [vidpi]
    blank = some.mp4
    delay_between_videos = 0
    debug = true
    retrigger = false

### Values In The vidpi Section

#### blank

If defined, this should be the name of a media file to play instead of having a blank screen between other media being played (i.e when there is no GPIO trigger).

#### delay_between_videos

This is the number of seconds to wait between checking for GPIO triggers between videos. The default is *0*.

#### debug

If set to *true*, debugging information will be displayed while videos are playing, and a message saying if there is no video being played will indicate that state.  The default is *false*.

#### retrigger

If set to *false*, videos will only be triggered if the GPIO pin has returned to 0 before rising to 1.  If *true*, videos will be triggered when the GPIO pin is 1, regardless of whether or not it had returned to 0 after the last video ended.  The default is *true*.

## Video Format

The best tested video format is as follows:

+ Container: MP4
+ Resolution: 720p or lower recommended (1080p might lead to frame dropping, and the projector type which is to be used with the system only has a native resolution of 854x480 anyway)
+ Frame rate: 24 fps
+ Video Codec: H.264
+ Audio codec: PCM 

The codec interpretation is done using ofxOmxplayer, which supports many other formats, but this is best tested / known to work well.

