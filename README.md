# Miniature Calendar Installer

This is a python script which downloads the latest image from [miniature-calendar.com](http://miniature-calendar.com/) and sets it as your desktop background image. **Currently only works on Mac**.

## Install

To install, clone this git repo

```
git clone https://github.com/jmbeach/miniature-calendar-desktop-setter
```

Then from inside the project's root directory, install the project's requirements

```
sudo pip install -r requirements.txt 
```

## Usage

This downloads the image and sets your background:

```
python main.py
```

### Run daily automatically

To have this run daily automatically, we can setup a [cron job](https://en.wikipedia.org/wiki/Cron). 

To set this up, first, we need to modify the text in crontab\_job. Change the value of "MINIATURE\_CALENDAR" to point to the directory where you cloned the project. See below for example:

```
MINIATURE_CALENDAR=/your/path/to/miniature-calendar
```

Next, if you have a crontab file already, just add the contents of "crontab\_job" into your crontab file.

If not, run the following command:

```
crontab crontab_job
```

Now, you should get your walpaper set to the latest miniature calendar image every day!

If you ever want to stop this, just remove the line from you crontab file or run `crontab -r` to get rid of your crontab file completely

## Roadmap

* Unfortunately, at 1500x1500 pixels, these images don't really make great wallpapers.
  * Enhance by super-imposing image on blurred version of image or on gradient color (using image's predominant color and scale so it fits nicely on 1920x1080). A little drop-shadow could be nice too.
* Make the script work on linux (and maybe Windows)