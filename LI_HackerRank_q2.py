items = [['owjevtkuyv', '58584272', '62930912' ],['owjevtkuyv', '58584272', '62930912' ], ['dfbkasyqcn', '37469674', '46363902'],['owjevtkuyv', '58584272', '62930912' ]]

def fetchItemsToDisplay(items, sortParameter, sortOrder, itemsPerPage, pageNumber):
    # Write your code here
    items_sorted = sorted(items, key = lambda r:r[sortParameter], reverse=sortOrder)


    res = items_sorted[pageNumber:itemsPerPage + 1]

    # for row in res: 
    print(res)


fetchItemsToDisplay(items, 2, 1, 1, 1)