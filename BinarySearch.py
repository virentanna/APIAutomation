# Binary Search Program

def BinarySearch(xlist,element):
    left = 0
    right = len(xlist) - 1
    midElement = (int)((left+right)/2)
    xlist.sort()
    print(xlist)
    found=False

    while left <= right:
        if xlist[midElement] == element:
            print(f'Element {element} found...')
            found=True
            break

        if element < xlist[midElement]:
            right = midElement - 1
        else:
            left = midElement + 1

        midElement = (int)((left+right)/2)

    if not found:
        print(f'Element {element} NOT found...')

BinarySearch([5,3,1,7,9,8,11,55,21],211)





