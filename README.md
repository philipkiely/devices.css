# devices.css
This repo was modified from [marvelapp/devices.css](https://github.com/marvelapp/devices.css). I took the same devices and made them resizable.

## How to use it

* Open `devices_new.scss` and set `$size_divisor` to the desired value. For half size, use 2.
* Run `sass devices_new.scss output_file.css`. A full-size devices file and half-size devices file are included with this repository, but you can generate any size.
* If you want to have a specific static size, include the file in the header of your HTML document. If you want the size to be responsive, use `@media` queries [as described here](https://www.w3schools.com/cssref/css3_pr_mediaquery.asp).

## How I made it

The original repository contains a ~2500 line scss file that I copied into `devices_old.scss`. I wrote `process.py` to rewrite the file with the `$size_divisor` variable and the correct `calc()` statements made and modified.

Read about it on [my blog](https://philipkiely.com/essays/first-open-source.html)
