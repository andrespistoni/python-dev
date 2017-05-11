import multiprocessing

import imp
import os
os.system("start main.py servRun()")

class MyProcess(multiprocessing.Process):
    def __init__(self,thing):
        multiprocessing.Process.__init__(self)
        self.thing=thing

    def run(self):
        print('running...', self.thing())


if __name__=="__main__":
    module=imp.load_source('main', './main.py')
    thing=module.servRun
    print(thing)
    p=MyProcess(thing)
    p.start()
    time.sleep(3)
    p.terminate()

    # thing = module.salir
    # print(thing)
    # p=MyProcess(thing)
    # p.start() 