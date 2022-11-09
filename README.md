TOPHAT 🎩
=========


Notes
-----

* Resolution: 1080x2160



Raspberry Pi Install
--------------------

* If there is a problem installing grpcio, you may need to install an older version
  * https://stackoverflow.com/a/72485013
    ```
    pip uninstall grpcio
    pip uninstall grpcio-status
    pip install grpcio==1.44.0 --no-binary=grpcio
    pip install grpcio-tools==1.44.0 --no-binary=grpcio-tools
    ```

* If Pygame complains that the image format isn't .bmp, run:

```sudo apt install libsdl-gfx1.2-5 libsdl-image1.2 libsdl-kitchensink1 libsdl-mixer1.2 libsdl-sound1.2 libsdl-ttf2.0-0 libsdl1.2debian libsdl2-2.0-0 libsdl2-gfx-1.0-0 libsdl2-image-2.0-0 libsdl2-mixer-2.0-0 libsdl2-ttf-2.0-0```