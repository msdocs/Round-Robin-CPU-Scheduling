###########################################################
##     Mahmoud Saleh                                     ##
##     Operating Systems : Round Robin CPU Scheduling    ##
##     CSCI-330 NYIT                                     ##
###########################################################

import queue,csv


class Process: # Definining Process
    def __init__(self,id,a,b):
        self.id = id
        self.a = a
        self.b = b
    def __str__(self):
        return 'ID: {:3d}   Arrival Time: {:3d}    Burst Time: {:3d}'.format(self.id,self.a,self.b)

class Simulator: # Building Simulator
    def __init__(self, tq=2):
        self.tq=tq # Time Quantum
        self.clock=0
        self.plist = []
        self.q=queue.Queue()

        #self.timer=0 # A second clock for manipulation souldn't be needed
    def addProcess(self,id,a,b):
        p = Process(id,a,b)
        self.plist.append(p)
    def schedule(self): # Adding to Schedule
        while self.clock < 100 :
            # enqueue incoming process
            for p in self.plist:
                if p.a == self.clock :
                        self.q.put(p)
                        #print('Adding Process',p.id,' to Queue at',self.clock,': 00 ')
            # run process
            if not self.q.empty():
                p = self.q.get()
                print(p)
                p.b=p.b-self.tq
                if not p.b <= 0 :
                    self.q.put(p)

            self.clock=self.clock+1


########### MAIN ##############

sim = Simulator()

with open('process.csv', newline='') as csvfile:
    process = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(process)
    for row in process:
            pid=int(row[0])
            arrival = int(row[1])
            burst = int(row[2])
            sim.addProcess(pid,arrival,burst)

    print('Process List\n+=============================================+')
    for p in sim.plist:
        print(p)

print('+=============================================+\n Simulating \n+=============================================+')
#sim.clock()
sim.schedule()
