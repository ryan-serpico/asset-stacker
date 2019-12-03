## Introduction
This script will take image assets and stack them on top of each other to create one long infographic image. It is all done locally on your machine ... for now. 

## Requirements
* Pillow: `pip3 install Pillow`

## Instructions
1. Add the image assets you would like to stack to the `img` folder.
2. Rename the images in the order you would like to see them in. The header should always be `0.png`. The first image asset you would like to be should be renamed `1.png`, the second should be `2.png` and so on.
3. The script will save the resulting stacked image to the `img` folder. 

## Known Issues and Roadmap
With the way this code is written at the moment, it probably wouldn't be useful to anyone outside of my office. It expects all but one image asset to have the same width. Because that doesn't mater for my use case, I probably won't add code to support images with varying widths in the near future.

My next goal for this project is to turn it into a web app with either Flask or Django.

## Context
I began working on this project because:
1. I wanted to automate a task that I perform every other week for some of my coworkers in my office. 
2. I wanted to make a tool that would allow my coworkers to do this task themselves.
3. I wanted to learn more about the `Pillow` python library.