# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 20:58:59 2020

@author: Wei Huajing
@company: Nanjing University
@e-mail: jerryweihuajing@126.com

@title：Module-name of postfix list
"""

flag_all=False

#list post fix in individual
list_standard=['Structural Deformation',
               'Mean Normal Stress',
               'Maximal Shear Stress',
               'Volumetric Strain-Cumulative',
               'Distortional Strain-Cumulative']

list_extra=['Volumetric Strain-Periodical',
            'Distortional Strain-Periodical',
            'Volumetric Strain-Instantaneous',
            'Distortional Strain-Instantaneous',
            'X Velocity',
            'Y Velocity',
            'X Displacement-Cumulative',
            'Y Displacement-Cumulative']

list_title=list_standard+list_extra

#list post fix in integral analysis
map_post_fix_list={}

map_post_fix_list['dynamics']=['Structural Deformation',
                               'Mean Normal Stress',
                               'Maximal Shear Stress',
                               'Volumetric Strain-Cumulative',
                               'Distortional Strain-Cumulative']
            
map_post_fix_list['kinematics']=['Structural Deformation',
                                 'X Velocity',
                                 'Y Velocity',
                                 'X Displacement-Cumulative',
                                 'Y Displacement-Cumulative']

map_post_fix_list['strain-cumulative']=['Volumetric Strain-Cumulative',
                                        'Distortional Strain-Cumulative']
        
map_post_fix_list['strain-periodical']=['Volumetric Strain-Periodical',
                                        'Distortional Strain-Periodical']
    
map_post_fix_list['strain-periodical']=['Volumetric Strain-Periodical',
                                        'Distortional Strain-Periodical']