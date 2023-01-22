'''
USING THE STATICFG LIBRARY TO DRAW THE CONTROL FLOW GRAPH
Stored in png format
'''

from staticfg import CFGBuilder

cfg = CFGBuilder().build_from_file('test','test.py')  #builds the diagraph, stored as test
cfg.build_visual('test','png')                        #builds the visual representation of the diagraph, stored as test.png
