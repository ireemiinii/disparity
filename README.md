# disparity

QUESTION.1 )
I first introduced the pictures. I researched and tried the values of disparity 
parameters one by one and decided which photo looks better. As a result, I 
decided that my parameters should be block size = 5, minimum disparity = -1 
and number of disparity = 256. minimum disparity is minimum possible disparity 
value. number of disparity is maximum disparity minus minimum disparity and 
must be divisible 16. 

QUESTION.2)
Firstly I printed the dimensions of the picture I got the output from. Then I 
defined names for correct and incorrect pixels. I set the intervals to hover the 
height in the first for loop and to travel horizontally in the second for loop. I 
subtracted the number of disparity value from the width value because the non
overlapping part in the disparity picture is equal. I set a condition. In this 
condition, I re-conditioned the ground truth values that are not equal to zero. In 
the second condition I have specified false values with more than 1 inequality. I 
added the remaining pixels as correct pixels. Then I printed the values equal to 
zero in the unknown value. I learned that there is such an equation (goodPixels / 
((width-numDisp) * height) - unknown)) to find the percentage of correct pixels.


QUESTION.3)
With our disparity result we can calculate the depth but first, the pictures must 
match before we can calculate the depth. It has to be a pair of pictures because 
it is defined by an equation such as (depth = (baseline * focal length) / disparity). 
The reason for the picture pair comes from the definition of disparity. Disparity 
is the difference in the image position of the same 3D point when projected into 
two different cameras under perspective. The displacement between the 
positions of any two points on the scene visible in both cameras is called 
disparity.


