def pathReduc(ls):
    needless_paths = [["NORTH", "SOUTH"], ["SOUTH", "NORTH"], ["EAST", "WEST"], ["WEST", "EAST"]]

    ix = 0
    while ix < len(ls)-1: #we don't need to check the last item in the list as it will be checked with the item before it
        if ls[ix] == ls[ix+1]:
            ix+=1
        else:
            if [ls[ix], ls[ix+1]] in needless_paths:
                ls.pop(ix+1)
                ls.pop(ix)
                if(ix!=0):
                    ix-=1
            else:
                ix+=1

    return ls