# Sex-recognition
> The program recognizes the gender of the person by sample of voice.

## General info
The program gets a sample with a voice as input. Then uses function wavile.read() from scipy libary, to get voice as signal-list. We will verify gender by the average frequency of the sound.  
To get the frequency we have to use Fast Fourier Transform.
If frequency is below 172.5 that's man. 
Otherwise it's a woman.

## Technologies
* scipy - version 1.5.4
* numpy - version 1.19.4

## Results
I ran tests on 93 files. Accuracy of program is about 80%.
