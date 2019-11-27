# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 23:52:05 2019

@author: Wei Huajing
@company: Nanjing University
@e-mail: jerryweihuajing@126.com

@title：Module-High Performance Calculation of Integral Analysis in a progress
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

import Path as Pa

import HPC_AnimationPlot as HPC_AP
import HPC_IndividualPlot as HPC_IP

#------------------------------------------------------------------------------
"""
Plot integral analysis of a progress

Args:
    output_folder: folder to contain result
    which_progress: progress object
    mode: 'standard' 'all'
    with_farcture: (bool) plot fracture and interface or not 

Returns:
    Figure path
"""
def SingleIntegralAnalysisInProgress(output_folder,
                                     which_progress,
                                     mode='standard',
                                     with_fracture=False):
    
    print('')
    print('Single Integral Analysis In Progress')

    #title font
    title_font=fm.FontProperties(fname=r"C:\Windows\Fonts\GILI____.ttf",size=13)
    
    #annotation font
    annotation_font=fm.FontProperties(fname="C:\Windows\Fonts\GIL_____.ttf",size=13)
    
    #global shape of progress or integral analysis
    global_shape=which_progress.shape
    
    if mode=='standard':
    
        list_post_fix=['Structural Deformation',
                       'Mean Normal Stress',
                       'Maximal Shear Stress',
                       'Periodical Volumetric Strain',
                       'Periodical Distortional Strain']
        
        #new picture and ax
        #100-1000
        if global_shape==(100,1000):
            
            figure=plt.subplots(figsize=(13,10))[0]
            
        #100-500
        if global_shape==(100,500):
        
            figure=plt.subplots(figsize=(7,10))[0]
    
    if mode=='all':
        
        list_post_fix=['Structural Deformation',
                       'Mean Normal Stress',
                       'Maximal Shear Stress',
                       'Periodical Volumetric Strain',
                       'Periodical Distortional Strain',
                       'Cumulative Volumetric Strain',
                       'Cumulative Distortional Strain']
    
        #new picture and ax
        #100-1000
        if global_shape==(100,1000):
            
            figure=plt.subplots(figsize=(13,14))[0]
        
        #100-500
        if global_shape==(100,500):
            
            figure=plt.subplots(figsize=(7,14))[0]
     
    #shape of this img
    this_shape=np.shape(which_progress.fracture)
    
    #subplot index
    index=0
    
    for this_post_fix in list_post_fix:
        
        #iter
        index+=1
        
        this_ax=plt.subplot(len(list_post_fix),1,index)
        
        if this_post_fix=='Structural Deformation':
            
            #structural deformation
            HPC_IP.IndividualStructuralDeformationInProgress(which_progress,this_ax)

        else:
                  
            #stress and strain
            HPC_IP.IndividualStressOrStrainInProgress(which_progress,this_post_fix,this_ax)    
            
        this_ax.axis([0,global_shape[1]*1.1,0,global_shape[0]])
        
        #sub annotation
        this_ax.annotate(which_progress.percentage,
                         xy=(0,0),
                         xytext=(1.01*this_shape[1],0.23*this_shape[0]),
                         fontproperties=annotation_font)
    
        #sub title
        this_ax.annotate(this_post_fix,
                         xy=(0,0),
                         xytext=(0,1.023*global_shape[0]),
                         fontproperties=title_font)
        
        this_ax.axis([0,global_shape[1]*1.13,0,global_shape[0]])
     
    #figure name
    fig_name=which_progress.percentage

    #re-name
    if with_fracture:
        
        fig_name+=' with fracture'
        
    integral_analysis_folder=output_folder+'\\integral analysis\\'
    
    #generate folder
    Pa.GenerateFolder(integral_analysis_folder)
    
    #figure path
    fig_path=integral_analysis_folder+fig_name+' ('+mode+').png'
    
    #save this fig
    figure.savefig(fig_path,dpi=300,bbox_inches='tight')
        
    plt.close()
    
    return fig_path

#------------------------------------------------------------------------------
"""
Plot all integral analysis

Args:
    output_folder: folder to contain result
    which_case: case object to be proccessed
    with_fracture: (bool) plot fracture or not 
    
Returns:
    None
"""   
def IntegralAnalysisAll(output_folder,
                        which_case,
                        with_fracture=False):
    
    print('')
    print('--Integral Analysis Plot')
    
    #integral analysis
    list_mode=['standard','all']
    
    for this_mode in list_mode:
        
        HPC_AP.AnimationIntegralAnalysis(output_folder,which_case,this_mode,with_fracture)