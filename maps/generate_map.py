# boundary =[xmin,xmax,ymin,ymax,zmin,zmax]
boundary = [0,0,0,9,9,9]

# main blocks with max height
# block = [xmin,xmax,ymin,ymax]
# main_color = [r,g,b]
blocks = [
    [0,1,8,9],
    [1,2,7,9],
    [1,2,1,6],
    [2,4,5,6],
    [3,4,6,8],
    [2,7,1,2],
    [3,6,3,4],
    [5,6,7,8],
    [7,8,7,8],
    [5,8,6,7],
    [5,8,4,5],
    [7,8,0,3],
    [7,9,4,5]
]
zmin = 0
zmax = 9
color = [200,200,50]

# height obstacle blocks 
# ob_block = [xmin,xmax,ymin,ymax,zmin,zmax]
# ob_color = [r,g,b]
ob_blocks = [
    [1,2,6,7,0,8],
    [3,4,8,9,1,9],
    [2,3,3,4,0,4],
    [2,3,3,4,6,9],
    [7,8,3,4,2,9]
]
ob_color = [50,200,200]

# start and end
startpoint = [0,1,0]
endpoint = [9,1,9]

# write in file
with open("map_maze.txt","w") as f:
    f.write("boundary")
    for v in boundary:
        f.write(" "+str(v))
    f.write("\n")
    for v in blocks:
        f.write("block")
        f.write(" "+str(v[0])+" "+str(v[2])+" "+str(zmin)+" "+str(v[1])+" "+str(v[3])+" "+str(zmax))
        for v in color:
            f.write(" "+str(v))
        f.write("\n")
    for v in ob_blocks:
        f.write("block ")
        f.write(str(v[0])+" "+str(v[2])+" "+str(v[4])+" "+str(v[1])+" "+str(v[3])+" "+str(v[5]))
        for v in ob_color:
            f.write(" "+str(v))
        f.write("\n")

