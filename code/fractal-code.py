#
# Draw a simple fractal
# GPL-3.0-or-later
# license explained at 
# https://www.gnu.org/licenses/
#
import numpy as np
import matplotlib.pyplot as plt
def f(z):
    return (z*z+.2323-.5345j)

def fractal(f, xmin,ymin,xmax,ymax,BIG,FARAWAY,maxpix=250):
    M=np.zeros([maxpix,maxpix])
    xvals = np.linspace(xmin,xmax,maxpix)
    yvals = np.linspace(ymin,ymax,maxpix)
    i=0
    for x in xvals:
        j=0
        for y in yvals:
            z = x+(1j)*y
            k=0
            while True:
                z=f(z)
                k+=1
                if k > BIG:
                    M[j][i]=0
                    break
                absz=np.absolute(z)
                if absz > FARAWAY:
                    M[j][i]=k          
                    break
            j+=1
        i+=1
    return(M)
#
# make maxpix bigger, say to 1500 to 
# to get a high res image
# larger values will take longer to run
#

F=fractal(f,0.175,0.125, .225, .175,150,20,maxpix=500)

plt.matshow(F,cmap="rainbow")
plt.axis("off") # removes frame and ticks and labels
fig=plt.gcf()
#
# uncomment the following to save to a file
# change file type to save to to other formats, 
# such as png, pdf, svg, etc.
#
#plt.gcf().savefig("my-fractal-image.jpg", dpi=500)
#
# show on screen
#
plt.show() 
