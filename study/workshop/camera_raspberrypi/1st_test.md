$ mjpg_streamer --help
~~~
-----------------------------------------------------------------------
Usage: mjpg_streamer
  -i | --input "<input-plugin.so> [parameters]"
  -o | --output "<output-plugin.so> [parameters]"
 [-h | --help ]........: display this help
 [-v | --version ].....: display version information
 [-b | --background]...: fork to the background, daemon mode
-----------------------------------------------------------------------
Example #1:
 To open an UVC webcam "/dev/video1" and stream it via HTTP:
  mjpg_streamer -i "input_uvc.so -d /dev/video1" -o "output_http.so"
-----------------------------------------------------------------------
Example #2:
 To open an UVC webcam and stream via HTTP port 8090:
  mjpg_streamer -i "input_uvc.so" -o "output_http.so -p 8090"
-----------------------------------------------------------------------
Example #3:
 To get help for a certain input plugin:
  mjpg_streamer -i "input_uvc.so --help"
-----------------------------------------------------------------------
In case the modules (=plugins) can not be found:
 * Set the default search path for the modules with:
   export LD_LIBRARY_PATH=/path/to/plugins,
 * or put the plugins into the "/lib/" or "/usr/lib" folder,
 * or instead of just providing the plugin file name, use a complete
   path and filename:
   mjpg_streamer -i "/path/to/modules/input_uvc.so"
-----------------------------------------------------------------------
~~~
$ mjpg_streamer -i "input_uvc.so" -o "output_http.so -p 8080"
~~~
MJPG Streamer Version: git rev: 501f6362c5afddcfb41055f97ae484252c85c912
 i: Using V4L2 device.: /dev/video0
 i: Desired Resolution: 640 x 480
 i: Frames Per Second.: -1
 i: Format............: JPEG
 i: TV-Norm...........: DEFAULT
UVCIOC_CTRL_ADD - Error at Pan (relative): Inappropriate ioctl for device (25)
UVCIOC_CTRL_ADD - Error at Tilt (relative): Inappropriate ioctl for device (25)
UVCIOC_CTRL_ADD - Error at Pan Reset: Inappropriate ioctl for device (25)
UVCIOC_CTRL_ADD - Error at Tilt Reset: Inappropriate ioctl for device (25)
UVCIOC_CTRL_ADD - Error at Pan/tilt Reset: Inappropriate ioctl for device (25)
UVCIOC_CTRL_ADD - Error at Focus (absolute): Inappropriate ioctl for device (25)
UVCIOC_CTRL_MAP - Error at Pan (relative): Inappropriate ioctl for device (25)
UVCIOC_CTRL_MAP - Error at Tilt (relative): Inappropriate ioctl for device (25)
UVCIOC_CTRL_MAP - Error at Pan Reset: Inappropriate ioctl for device (25)
UVCIOC_CTRL_MAP - Error at Tilt Reset: Inappropriate ioctl for device (25)
UVCIOC_CTRL_MAP - Error at Pan/tilt Reset: Inappropriate ioctl for device (25)
UVCIOC_CTRL_MAP - Error at Focus (absolute): Inappropriate ioctl for device (25)
UVCIOC_CTRL_MAP - Error at LED1 Mode: Inappropriate ioctl for device (25)
UVCIOC_CTRL_MAP - Error at LED1 Frequency: Inappropriate ioctl for device (25)
UVCIOC_CTRL_MAP - Error at Disable video processing: Inappropriate ioctl for device (25)
UVCIOC_CTRL_MAP - Error at Raw bits per pixel: Inappropriate ioctl for device (25)
 o: www-folder-path......: disabled
 o: HTTP TCP port........: 8080
 o: HTTP Listen Address..: (null)
 o: username:password....: disabled
 o: commands.............: enabled
~~~
~~~
501: Not Implemented!
no www-folder configured
~~~
