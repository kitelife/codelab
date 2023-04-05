def merge(L1, L2):
    
    newL = []
    i1 = 0
    i2 = 0
    
    while i1 != len(L1) and i2 != len(L2):
        if L1[i1] <= L2[i2]:
            newL.append(L1[i1])
            i1 += 1
        else:
            newL.append(L2[i2])
            i2 += 1
            
    # Gather any leftover items from the two sections.
    # Note that one of them will be empty because of the loop conditiion.
    newL.extend(L1[i1:])
    newL.extend(L2[i2:])
    
    return newL

def mergesort(L):
    
    # make a list of 1-item lists so that we can start merging.
    workspace = []
    for i in range(len(L)):
        workspace.append([L[i]])
    
    # The next two lists to merge are workspace[i] and workspace[i + 1]
    i = 0
    
    # As long as there are at least two more lists to merge, merge them.
    while i < len(workspace) - 1:
        L1 = workspace[i]
        L2 = workspace[i + 1]
        newL = merge(L1, L2)
        workspace.append(newL)
        i += 2
    
    # Copy the result  back into L.
    if len(workspace) != 0:
        L[:] = workspace[-1][:]
        
if __name__ == "__main__":
    testL = [100,2,121,0,5,32,23,40,100,10000,54,11]
    mergesort(testL)
    print testL