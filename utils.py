def HasRelation(keyword, a, b):
  return a  + " is " + keyword + " " + b

def ExplainRelation(keyword, a, b):
    print HasRelation(keyword, a, b)
    reason = raw_input("because.... \n")
    print "congratulations! " + HasRelation(keyword, a, b) + "! \n(....because " + reason + ")"

def EvinceRelation(keyword):
  a = raw_input("type in a first item \n");
  b = raw_input("type in a second item \n");
  ExplainRelation(keyword, a, b)


