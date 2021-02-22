# a point is inside a polygon if, for any ray from this point, 
# there is an odd number of crossings of the ray with the polygon's edges
# reference: http://erich.realtimerendering.com/ptinpoly/
# here I find intersection point with the edge and the right direction ray

import numpy as np

poly = [[4, 3],
        [2, 6],
        [3, 12],
        [2, 17],
        [5, 20],
        [9, 21],
        [14, 19],
        [20, 14],
        [18, 3],
        [11, 7]]

points = [[7, 11],
        [10 ,14],
        [11, 4],
        [12 ,21],
        [16, 3],
        [16 ,10],
        [17, 4],
        [18, 7],
        [18 ,17],
        [20, 7]]

# verification = np.zeros((25,25),dtype=np.int8)
# for i,point in enumerate(poly):
#     verification[point[0]-1,point[1]-1] = 2
# for i,point in enumerate(points):
#     verification[point[0]-1,point[1]-1] = 1
# print(verification)

# this method can't handle vertical edges
def insidePoly(point, poly):

    pointx, pointy = point
    flag = False
    # if there's a intersection, flag flips  
    for i, polyCorner in enumerate(poly):
        if i + 1 < len(poly):
            j = i + 1
        else:
            j = 0
        x1, y1 = polyCorner
        x2, y2 = poly[j]
        # if point is on the conrner
        if (pointx == x1 and pointy == y1) or (pointx == x2 and pointy == y2):  
            flag = True
            break
        # if y=pointy and edge has an intersection point (x,y), 
        # then (x-x1)*((y2-y1)/x2-x1)=y-y1=pointy-y1
        if min(y1,y2) < pointy <= max(y1,y2):  
            x = x1 + (pointy-y1) * (x2-x1) / (y2-y1)
            # if point is on the edge
            if x == pointx:  
                flag = True
                break
            # if point is on the left side of the edge
            elif pointx < x:  
                flag = not flag
    return flag

# f = open('output_question_6','w')
for i in range(len(points)):
    # sstring = ''
    if insidePoly(points[i], poly):
        print(str(points[i]).replace('[','').replace(',','').replace(']',''), 'inside')
        # sstring = (str(points[i]).replace('[','').replace(',','').replace(']',''))
        # f.write(sstring+' inside')
    else:
        print(str(points[i]).replace('[','').replace(',','').replace(']',''), "outside")
    #     sstring = (str(points[i]).replace('[','').replace(',','').replace(']',''))
    #     f.write(sstring+' outside')
    # f.write('\n')
# f.close()
