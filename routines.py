import matplotlib.pyplot as plt
import numpy as np


def plot_data(photo, FP, subplots = 2):
    
    #Determine xlim 
    
    lim_min = min(photo.t[0],FP.t[0])
    lim_max = max(photo.t[len(photo.t)-1],FP.t[len(FP.t)-1])
    plt.subplot(subplots,1,2)
    plt.plot(photo.t,photo.V, label ='Photometer')
    plt.legend()
    plt.ylabel('V')
    plt.xlabel('t')
    plt.xlim([lim_min,lim_max])
    
    ax = plt.subplot(subplots,1,1)
    plt.plot(FP.t,FP.V, label = 'Fabry-Perot',color = 'orange')
    plt.legend()
    plt.xlabel('t')
    plt.ylabel('V')
    plt.xlim([lim_min,lim_max])
    ax.set_xticks([])
    plt.xlabel("")

    return [lim_min,lim_max]


def gauss(x, N, mu, sig):
    return N*np.exp(-((x-mu)/sig)**2/2)

def four_gauss(x,N1,N2,N3,N4,mu1,mu2,mu3,mu4,sig1,sig2,sig3,sig4): # AAAAAARRGGGHHH
    return (gauss(x,N1,mu1,sig1)+gauss(x,N2,mu2,sig2)+gauss(x,N3,mu3,sig3)+gauss(x,N4,mu4,sig4))

def plot_interval(left, right, height , label, labelwidth,hw = .05 ):

    begin1 = left
    end1 = left +(right-left)/2 - labelwidth
    begin2 = end1 + 2* labelwidth
    end2 = right
    plt.annotate(label,[end1,height])
    plt.arrow(end1,height,begin1-end1,0,head_length = .00005, head_width = hw, fc='k', ec='k',length_includes_head = False)
    plt.arrow(begin2,height,end2-begin2,0, head_length = .00005, head_width = hw, fc='k', ec='k',length_includes_head = False) 

