from ipywidgets import interact
#Jupyter
@interact(left=100, top=100, right=200, bottom=200)
def out(left, top, right, bottom):
    print(left, top, right, bottom)
