#  x = 1
#  
#  def foo():
#      if False:
#          x = 2
#      global x
#      x = 3
#      print x
#  
#  foo()

(____,) = (False,)
_ = 1

def __():
    if ____:
        _ = 2
    global _
    _ = 3
    print _
__()