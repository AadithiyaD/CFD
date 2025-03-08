My MSc thesis at Cranfield dealt with the analysis of wind flow around a built environment, and its subsequent effects on vehicle stability

This project was carried out in Ansys Fluent, and is a part of a bigger "product" that i see being of use to racing teams

The ideal vision is to develop a workflow that would allow one to look at a corner on a race track, see if it warrants deeper investigation, carry out said investigation, and then ultimately conclude whether or not vehicle stability is of concern, thus giving drivers more information.

Another potential use case if for racetrack designers. Steps can be taken to minimize the impact of winds

At the end of the thesis, I compiled a list of uncertainties that had to be addressed before moving further with this work. One of these uncertainties was with regard to maintaining a homogeneous Atmospheric Boundary Layer (ABL)

In order to do this, custom boundary conditions, and wall functions are to be implemented. The implementation of these methods was convoluted in Fluent and I did not have the time to work out a suitable implementation

OpenFoam not only has some models for ABL simulation, it is also much easier to implement custom formulations, which is what this folder is about. 

The final hope is that should someone be interested in such an analysis, this would serve as a repository for getting a finalized setup that can be used to run a steady RANS simulation on a corner, which would serve as the basis for their study.