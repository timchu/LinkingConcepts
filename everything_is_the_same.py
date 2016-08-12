def IsTheSameAs(a, b):
    return a + " is the same as " + b

def ExplainSameness(a, b):
    print IsTheSameAs(a, b)
    raw_input("because.... \n")
    print "congratulations! " + IsTheSameAs(a, b) + "!" 

a = raw_input("type in a first item \n");
b = raw_input("type in a second item \n");

ExplainSameness(a, b)

