
# Colorizer  
This little program is using DeepAI API to colorize black and white pictures.  
  
##  Installation

    git clone https://github.com/fddn/colorizer.git
    cd colorizer
    pip install -r requirements.txt

## Usage
Without any parameter, the program uses the source folder to store the black and white images and uses result to store the colorized images.

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