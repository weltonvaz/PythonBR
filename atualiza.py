import time 
 
def gera(valorInicio, valorFim, valorPasso):
    while valorInicio <= valorFim:
        yield valorInicio
        valorInicio += valorPasso
        
def update(atual, novo, var):
    print "var:", var, "  id(var):", id(var)        
    if (novo >= atual):
        atual = novo
        var = atual
    print "var:", var, "  id(var):", id(var)        
 
        
def run(valorInicio, valorFim, valorPasso, var):
    
    atual = 0
    print "id(var):", id(var)  
    for x in gera(valorInicio, valorFim, valorPasso):
        time.sleep(0.1)
        update(atual, x, var)        
        print "\n", x
    print "id(var):", id(var)  
    print "var:", var
