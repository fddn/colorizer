
# Colorizer  
[![Build Status](https://travis-ci.com/fddn/colorizer.svg?branch=master)](https://travis-ci.com/fddn/colorizer)

This little program is using DeepAI API to colorize black and white pictures.  
  
##  Installation

    git clone https://github.com/fddn/colorizer.git
    cd colorizer
    pip install -r requirements.txt

## Usage
First of all, you need to register an account on [DeepAPI](https://deepai.org/) and fill secrets.py.
Set API_KEY to you secret key:

    API_KEY = '<changeme>' --> API_KEY = 'something_secret_key_provided_by_DeepAI'

Now you can run without any parameter, the program uses the source folder to store the black and white images and uses result to store the colorized images.

    $ python main.py -h
	usage: main.py [-h] [-s SOURCE] [-d DESTINATION]

	optional arguments:
	  -h, --help            				show this help message and exit
	  -s SOURCE, --source SOURCE			Source folder
	  -d DESTINATION, --dest DESTINATION	Destination folder

### Example printout:
Using default folders:
		
	$ python main.py
	Colorizing 2 images
	Uploading: test1.jpg - 1/2
	Downloading: test1.jpg - 1/2
	Uploading: test2.jpg - 2/2
	Downloading: test2.jpg - 2/2

Passing source and destination folder as parameter

	$ python main.py -s /home/<username>/source_images/ -d /home/<username>/result_images/
	Colorizing 2 images
	Uploading: test1.jpg - 1/2
	Downloading: test1.jpg - 1/2
	Uploading: test2.jpg - 2/2
	Downloading: test2.jpg - 2/2
	
### Future work:
- Need some more refactoring, this code currently little spaghetti
- Parallel update might be handy and speed up the process a bit
- Maybe a GUI would be nice
- Any other idea?