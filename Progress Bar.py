import sys


from progressbar \
    import Bar,  ETA, ProgressBar, ReverseBar

def backwardsBar():
    widgets = [Bar('>'), ' ', ETA(), ' ', ReverseBar('<')]
    pbar = ProgressBar(widgets=widgets, maxval=10000000).start()
    for i in range(1000000):
        # do something
        pbar.update(10*i+1)
    pbar.finish()

backwardsBar()