# IPIP

In this small experiment, we apply the the algorithm of Elena Facco, Maria d’Errico, Alex Rodriguez, and Alessandro Laio, following in the paper:  https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5610237/ to the IPIP120 and IPIP300 data sets.  

The IPIP data is a series of questions  (120 or 300 )with values 1,2,3,4,5.  We used the Euclidean distance in 120 and 300 dimensional Euclidean space,  and the algorithm above more or less out of the box, although we did experiment with adding a small amount of noise.  

Some experiments are with men, some with women, and some with the data set mixed. 

The "table.csv" lists the experiments and the dimension estimation for each when discarding 5,10,15,20% of the farthest out data.   The above paper suggests using 90%.   If you look at some of the pictures, there is a distinct change in slope of the curves that happens around 90% or so.   

In short, the dimensionality of the IPIP300 data is estimated to be about 62 for men and women combined, and roughly 58 and 61 for men and women respectively.  For the IPIP120 set the total dimensionality is about 47, 44.5 and 46 (roughly) respectively.  

