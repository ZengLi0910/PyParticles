# PyParticles : Particles simulation in python
# Copyright (C) 2012  Simone Riva
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import numpy as np
import sys

class Force(object):
    def __init__(self , size , dim , m=None , Conts=1.0 ):
        NotImplementedError(" %s : is virtual and must be overridden." % sys._getframe().f_code.co_name )
    
        
    def set_masses( self , m ):
        NotImplementedError(" %s : is virtual and must be overridden." % sys._getframe().f_code.co_name )
    
    def update_force( self , p_set , sub_forces=False , main_force=None ):
        NotImplementedError(" %s : is virtual and must be overridden." % sys._getframe().f_code.co_name )
            
    def getA(self):
        NotImplementedError(" %s : is virtual and must be overridden." % sys._getframe().f_code.co_name )
        
    A = property( getA )
        
    def getF(self):
        NotImplementedError(" %s : is virtual and must be overridden." % sys._getframe().f_code.co_name )
    
    F = property( getF )
    
    
    def get_shape(self):
        NotImplementedError(" %s : is virtual and must be overridden." % sys._getframe().f_code.co_name )
        
    shape = property( get_shape )
    
    
    def add_sub_force( self , sub_force ):
        print( "Sub force not yet supported" )