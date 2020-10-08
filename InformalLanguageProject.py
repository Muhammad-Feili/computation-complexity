class dfa():
    def __init__(self,initialState):
        self.States=[]
        self.FinalStates=[]
        self.Delta=[]
        self.Sigma=[]
        self.InitialState=initialState
        
    def addTransaction(self,transaction):
        if transaction not in self.Delta:
            self.Delta.append(transaction)
            
            if transaction[0] not in self.States:
                 self.States.append(transaction[0])
                    
            if transaction[2] not in self.States:
                self.States.append(transaction[2])
            
            if transaction[1] not in self.Sigma:
                self.Sigma.append(transaction[1])
            
            
            
    def printAutomata(self):
        print("\n","initialstate",28*"*","\n")
        print(self.InitialState)
        
        print("\n","states",34*"*","\n")
        for s in self.States:
            print(s)
            
        print("\n","finalstates",29*"*","\n")
        
        for fs in self.FinalStates:
            print(fs)
            
        print("\n","alphabets",31*"*","\n")
        
        for s in self.Sigma:
            print(s)
            
        print("\n","Delta",35*"*","\n")
        
        for t in self.Delta:
            print("delta[",t[0],",",t[1],"]=",t[2])
            
        print("\n",40*"*")
        
    
    def addFinalStates(self,finalstate):
        if finalstate not in self.FinalStates:
            self.FinalStates.append(finalstate)
        
        
    def outputs(self,state,alphabet):
        
        for d in self.Delta:
            if d[0]==state and d[1]==alphabet:
                return d[2]
               
                            
    
    def haveEntry(self,state):
        for i in self.Delta:
            if state==i[2]:
                return True
        
        for i in self.Delta:
            if state==i[0]:
                self.Delta.remove(i)
        return False
    
    
    
    def addState(self,state):
        self.States.append(state)
    
    
    def minimize(self):
        accessiblelist=[]
        accessiblelist.append(self.InitialState)
        li=[]
        li.append(self.InitialState)
        Lbar=[]
        
        while len(li)>0:
            s=li.pop()
            for ch in self.Sigma:
                d=self.outputs(s,ch)
                
                if d not in accessiblelist:
                    accessiblelist.append(d)
                if d not in Lbar:
                    li.append(d)
            Lbar.append(s)
            
        if self.InitialState not in self.States:
            self.States.append(self.InitialState)
            
        usualStates=[]
        for i in self.States:
            if i not in self.FinalStates:
                if i not in usualStates:
                    usualStates.append(i)
        
            
        
        
        
        
        
        classes=[]
        usualStates=set(usualStates)
        classes.append(usualStates)
        finalStates=set(self.FinalStates)
        classes.append(finalStates)
        
        uu=classes
        classes=[]
        while classes!=uu:
            classes=uu
            print("classes",classes)
            uu=[]
            
            for clas in classes:
                
                temp=clas.pop()
                clas.add(temp)
                
                distinguishable=set()
                distinguishable.add(temp)
                nondistinguishable=set()
                
                for state in clas:
                    for alpha in self.Sigma:
                        if state!=temp:
                            x=self.outputs(temp,alpha)
                            y=self.outputs(state,alpha)
                            
                            for cl in classes:
                                if x in cl:
                                    
                                    if y in cl and y not in distinguishable:
                                        
                                        distinguishable.add(state)
                                    if y not in cl and y not in nondistinguishable:
                                        
                                        nondistinguishable.add(state)
                                
                                
                                
                if distinguishable!=set() and distinguishable not in uu:
                    uu.append(distinguishable)
                if nondistinguishable!=set() and nondistinguishable not in uu:
                    uu.append(nondistinguishable)
            print("uu=",uu)
            print("classes",classes)
            
            
                            
        
        #set States
        self.States=classes
        
        fStates=[]
        #set finalStates
        for clas in classes:
            for state in clas:
                if state in self.FinalStates:
                    if clas not in fStates:
                        fStates.append(clas)
                        break
                    
        #set initialState
        """for clas in classes:
            if self.InitialState in clas:
                self.InitialState=clas
                break"""
            
        
        self.FinalStates=fStates
        
        #set delta
        s=[]
        for edge in self.Delta:
            initState=self.equivalclass(edge[0])
            finaState=self.equivalclass(edge[2])
            if (initState,edge[1],finaState) not in s:
                s.append((initState,edge[1],finaState))
            #print(s)
        self.Delta=s
        
    def equivalclass(self,state):
        for clas in self.States:
            cl=list(clas)
            if state in cl:
                return clas
class finiteAutomata():
    def __init__(self,states=set(),finalStates=set(),delta=set(),sigma=set(),initialState=("0")):
        self.States=states
        self.FinalStates=finalStates
        self.Delta=delta
        self.Sigma=sigma
        self.InitialState=initialState
        self.States.add(initialState)
        
    def addTransaction(self,transaction):
        if transaction not in self.Delta:
            self.Delta.add((transaction))
            
            if transaction[0] not in self.States:
                 self.States.add((transaction[0]))
            
            if transaction[2] not in self.States:
                self.States.add((transaction[2]))
            
            if transaction[1] not in self.Sigma:
                if transaction[1]!=' ':
                    self.Sigma.add((transaction[1]))
            
            
            
    def printAutomata(self):
        print("\n","initialstate",28*"*","\n")
        print(self.InitialState)
        
        print("\n","states",34*"*","\n")
        for s in self.States:
            print(s)
            
        print("\n","finalstates",29*"*","\n")
        
        for fs in self.FinalStates:
            print(fs)
            
        print("\n","alphabets",31*"*","\n")
        
        for s in self.Sigma:
            print(s)
            
        print("\n","Delta",35*"*","\n")
        
        for t in self.Delta:
            print("delta(",t[0],",",t[1],")=",t[2])
            
        print("\n",40*"*")
        
    
    def addFinalStates(self,finalstate):
        self.FinalStates.add(finalstate)
        
        
    def outputs(self,state,alphabet):
        out=set()
        for d in self.Delta:
            if d[0]==state and d[1]==alphabet:
                out.add(d[2])
                L=[]
                Lbar=[]
                L.append(d[2])
                while len(L)>0:
                    temp=L.pop()
                    Lbar.append(temp)
                    for i in self.Delta:
                        if temp==i[0] and i[1]==' ':
                            out.add(i[2])
                            if i[2] not in Lbar:
                                L.append(i[2])
                            
        return out
                        
                        
    def toDFA(self,dfa):
        
        qu=[]
        qbar=[]
        qu.append([dfa.InitialState])
        dfa.InitialState=tuple(dfa.InitialState)
        print("\n","state generation Steps",18*"*","\n")
        while len(qu) > 0:
            print(qu)#this is for testing
            s=[]
            s=qu.pop()
            qbar.append(s)
            
            for ch in self.Sigma:
                b=set()
                for i in s:
                    b |=self.outputs(i,ch)
                    
                
                b=list(b)
                b.sort()
                b=tuple(b)
                s.sort()
                s=tuple(s)
                
                if (s,ch,b) not in dfa.Delta:
                    dfa.addTransaction((s,ch,b))
                    
                s=list(s)
                if b not in dfa.States:
                    dfa.States.append(b)
                    
                b=list(b)
                b.sort()
                s.sort()
                if b!=s:
                    if b not in qu and b not in qbar:
                        qu.append(b)
        
        for state in dfa.States:
            for st in state:
                if st in self.FinalStates:
                    dfa.FinalStates.append(state)
                    break
                
            
        return dfa
if __name__=="__main__":  
    #example 1
    nfa=finiteAutomata()
    nfa.addTransaction(("0",'a',"1"))
    nfa.addTransaction(("1",'a',"1"))
    nfa.addTransaction(("1",' ',"2"))
    nfa.addTransaction(("2",'b',"0"))
    nfa.addFinalStates("1")
    FA=dfa("0")
    FA=nfa.toDFA(FA)
    FA.minimize()
    FA.printAutomata() 
    
    #example 1
    nfa1=finiteAutomata()
    nfa1.addTransaction(("0",0,"0"))
    nfa1.addTransaction(("0",0,"1"))
    nfa1.addTransaction(("1",0,"2"))
    nfa1.addTransaction(("1",1,"2"))
    nfa1.addTransaction(("2",1,"2"))
    nfa1.addTransaction(("0",1,"1"))
    nfa1.addFinalStates("1")
    F=dfa("0")
    F=nfa.toDFA(F)
    F.minimize()
    F.printAutomata()
