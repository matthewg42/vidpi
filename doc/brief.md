Artist Jo Fairfax wants two video projection systems for running demos:

# System 1

-   RPi with HDMI display
-   Up to 30 videos on supplied on a USB key formatted FAT
-   Motion sensor (ultrasonic or PIR) connected to GPIO pin - digital input.  Trigger on rising edge
-   Blank screen to start, on trigger shows a random video from the USB key files

# System 2
-   RPi with HDMI display
-   Up to 30 videos on supplied on a USB key formatted FAT
-   Motion sensor (ultrasonic or PIR) connected to GPIO pin - digital input.  Trigger on rising edge
-   When not triggered, keeps playing a specific file (blank.mp4)
-   On trigger shows a random video from the USB key files (but not blank.mp4)

- Set up to be able to plug in wifi (extra)
- settings.ini on flash with delay config
- Trigger -> play whole video -> after end some delay (configurable) -> repeat
- Use HDMI
- optimised boot time
- try pi 2 and 3
- reduce lag as much as possible

Deliverables:
- 2 x Pi with s/w installed
- with enclosures
- document .ini file options
- document video formats which can be used
