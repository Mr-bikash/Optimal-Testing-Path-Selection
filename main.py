from staticfg import CFGBuilder

cfg = CFGBuilder().build_from_file('test','test.py')
cfg.build_visual('test','png')
