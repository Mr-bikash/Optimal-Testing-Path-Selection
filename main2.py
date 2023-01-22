'''
USING THE PY2CFG LIBRARY TO DRAW THE CONTROL FLOW GRAPH
STORED AS PDF FORMAT
'''

from py2cfg import CFGBuilder

cfg = CFGbuilder().build_from_file('test','test.py')
cfg.build_visual('test','pdf)
