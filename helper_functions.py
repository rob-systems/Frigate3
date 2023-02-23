from shapely import affinity
import math

####################################################################
    #HELPER FUNCTIONS
####################################################################

def get_list_from_polygon(polygon):
    #because I can't seem to directly iterate over shapely's polygons
    #it seems really convuluted
    l = []
    xx, yy = polygon.exterior.coords.xy
    newxcoords, newycoords = [], []
    for x in xx:
        newxcoords.append(x)
    for y in yy:
        newycoords.append(y)
    for i, x in enumerate(newxcoords):
        l.append((newxcoords[i], newycoords[i]))
    return l

def get_polygon_centre(points):
    totalx, totaly = 0, 0
    for point in points:
        totalx += point[0]
        totaly += point[1]
    return (totalx/len(points), totaly/len(points))

def get_centre_of_shapely_polygon(polygon):
    coords = get_list_from_polygon(polygon)
    return get_polygon_centre(coords)

def rotate_polygon(polygon, rotation):
    new_triangle = affinity.rotate(polygon, rotation, get_polygon_centre(get_list_from_polygon(polygon)))
    xx, yy = new_triangle.exterior.coords.xy
    l = []
    for i, x in enumerate(xx):
        l.append((xx[i], yy[i]))
    return l

def move_polygon(poly, movement_tuple):
    new_poly = []
    for coord in poly:
        new_poly.append((coord[0] + movement_tuple[0], coord[1] + movement_tuple[1]))
    return new_poly

def get_vector_length(x, y):
    return math.sqrt(x*x + y*y)

def normalize_vector(x, y):
    norm = get_vector_length(x, y)
    if norm != 0:
        return x/norm, y/norm
    else:
        return x, y
