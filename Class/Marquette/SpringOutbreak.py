def spring_outbreak():
    closest = []
    cases = int(input())
    for case in range(cases):
        holes = int(input())
        coords = []
        for hole in range(holes):
            coords.append(input().split(" "))
        print("")
        
        closest_dist = 0
        closest_dist_coords = [0, 0, 0, 0]
        for i in range(len(coords)):
            for j in range(i+1, len(coords)):
                dist = abs(int(coords[i][0]) - int(coords[j][0])) + abs(int(coords[i][1]) - int(coords[j][1]))
                if dist < closest_dist or i == 0 and j == 1:
                    closest_dist = dist
                    closest_dist_coords = [int(coords[i][0]), int(coords[j][0]), int(coords[i][1]), int(coords[j][1])]

        closest.append(str(int((closest_dist_coords[0] + closest_dist_coords[1])/2)) + " " + str(int((closest_dist_coords[2] + closest_dist_coords[3])/2)))

    for val in closest:
        print(val)

spring_outbreak()