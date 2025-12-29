# Day 9 of Advent of Code 2024: Movie Theatre
# https://adventofcode.com/2024/day/9
from collections import namedtuple, deque
from itertools import combinations, pairwise

Coord = namedtuple('Coord', ['x', 'y'])

def minmax(coordinates):
    min_x, max_x = 100000, 0
    min_y, max_y = 100000, 0
    for coord in coordinates:
        if coord.x < min_x:
            min_x = coord.x
        if coord.x > max_x:
            max_x = coord.x
        if coord.y < min_y:
            min_y = coord.y
        if coord.y > max_y:
            max_y = coord.y
    return min_x, max_x, min_y, max_y

def printTiles(coordinates, toFile=False):
    min_x, max_x, min_y, max_y = minmax(coordinates)
    tile_colors = borderTiles(coordinates)
    S = ""
    for y in range(min_y - 1, max_y + 2):
        for x in range(min_x - 1, max_x + 2):
            if Coord(x,y) not in tile_colors:
                S += ' '
            else:
                S += tile_colors[Coord(x,y)]
        S += '\n'
    if not toFile:
        print(S)
    else:
        with open("tiles.txt",'w') as f:
            f.write(S)


def borderTiles(coordinates):
    tile_colors = {}
    for tile1, tile2 in pairwise(coordinates + [coordinates[0]]):
        tile_colors[tile1], tile_colors[tile2] = 'R', 'R'
        if tile1.x == tile2.x:
            for i in range(min(tile1.y, tile2.y)+1, max(tile1.y, tile2.y)):
                tile_colors[Coord(tile1.x, i)] = 'G'
        else:
            for i in range(min(tile1.x, tile2.x)+1, max(tile1.x, tile2.x)):
                tile_colors[Coord(i, tile1.y)] = 'G'
    
    return tile_colors

def rectExtremas(rectangle):
    coordA, coordB = rectangle
    if coordA.x <= coordB.x and coordA.y <= coordB.y:
        return coordA, coordB
    elif coordA.x <= coordB.x:
        return Coord(coordA.x, coordB.y), Coord(coordB.x, coordA.y)
    elif coordA.y <= coordB.y:
        return Coord(coordB.x, coordA.y), Coord(coordA.x, coordB.y)
    else:
        return coordB, coordA

def within_shape_in_row(border, row):
    border_in_row = [(pos[0], col) for pos, col in border.items() if pos[1] == row]
    border_in_row.sort()
    border_in_row = deque(border_in_row)
    within = []
    stack = deque()
    while border_in_row:
        border_piece = border_in_row.popleft()
        if not stack and border_piece[1] == 'R':
            corner_type = 'UP' if Coord(border_piece[0],row-1) in border else 'DOWN'
            stack.append((border_piece[0], border_piece[1], corner_type))
            continue
        elif not stack:
            stack.append(border_piece)
            continue
        
        if stack[-1][1] == 'R' and border_piece[1] == 'G':
            continue
        if stack[-1][1] == 'G' and border_piece[1] == 'G':
            left = stack.pop()
            within.append((left[0], border_piece[0]))
        elif stack[-1][1] == 'R' and border_piece[1] == 'R':
            left_x, _, left_corner = stack.pop()
            right_x = border_piece[0]
            this_corner = 'UP' if Coord(right_x,row-1) in border else 'DOWN'
            if left_corner == this_corner and not stack:
                within.append((left_x, right_x))
            elif left_corner != this_corner and not stack:
                stack.append((left_x, 'G'))
            elif left_corner != this_corner and stack:
                left_left_x, _ = stack.pop()
                within.append((left_left_x, right_x))
        elif stack[-1][1] == 'G' and border_piece[1] == 'R':
            corner_type = 'UP' if Coord(border_piece[0],row-1) in border else 'DOWN'
            stack.append((border_piece[0], border_piece[1], corner_type))
    return within
        

    

def rectWithin(rectangle, border):        
    def within_row(left, right, row):
        in_ranges = within_shape_in_row(border, row)
        for x0, x1 in in_ranges:
            if x0 <= left and right <= x1:
                return True
            elif x0 <= left:
                return False
        return False
    
    topLeft, bottomRight = rectExtremas(rectangle)

    for row in range(topLeft.y, bottomRight.y + 1):
        if not within_row(topLeft.x, bottomRight.x, row):
            return False
    return True


def rectWithinOLD(rectangle, border):
    topLeft, bottomRight = rectExtremas(rectangle)
    for y in range(topLeft.y, bottomRight.y + 1):
        within = False
        first_corner_type, second_corner_type = None, None
        before_bend, passed_green = None, False
        # x = min(a for a,b in border.items() if b == y) - 1
        # if x > bottomRight.x:
        #     return False
        x = 1
        
        while x <= bottomRight.x:
            xy, prev = Coord(x,y), Coord(x-1,y)
            if xy in border and border[xy] == 'R':
                if prev not in border:
                    before_bend = within
                    within = True
                    first_corner_type = 'UP' if Coord(x,y-1) in border else 'DOWN'
                    passed_green = False
                else:
                    second_corner_type = 'UP' if Coord(x,y-1) in border else 'DOWN'
            elif xy in border:
                if prev not in border:
                    within = True
            else:
                if prev in border and border[prev] == 'R':
                    within = (first_corner_type==second_corner_type and before_bend) or (first_corner_type!=second_corner_type and not before_bend)
                    before_bend, first_corner_type, second_corner_type = None, None, None
                elif prev in border:
                    if passed_green:
                        within = False
                        passed_green = False
                    else:
                        within = True
                        passed_green = True

            if topLeft.x <= x and not within:
                return False
            x += 1
    return True



def area(coordA, coordB):
    return (abs(coordA.x - coordB.x) + 1)*(abs(coordA.y-coordB.y )+ 1)
# print(area(Coord(2,5),Coord(9,7)))
# print(area(Coord(7,3),Coord(2,3)))
# print(area(Coord(2,5),Coord(11,1)))


def sol(coordinates):
    border = borderTiles(coordinates)
    areas = [(area(cA, cB), cA, cB) for cA, cB in combinations(coordinates, 2)]
    areas.sort(reverse=True)
    res1 = max(areas)[0]
    for A, coord1, coord2 in areas:
        if rectWithin((coord1, coord2), border):
            res2 = A
            break
        print("not within")
    return res1, res2

def main():
    tiles = []
    f2 = open("day9_not_within.txt", 'w')
    with open("input9.txt") as file:
        for row in file:
            tiles.append(Coord(*map(int, row.strip().split(','))))
            x,y = tiles[-1]
            f2.write(str(round(x*0.002))+','+str(round(y*0.002))+'\n')
    
    f2.close()
    # res1, res2 = sol(tiles)
    res1, res2 = 0,0
    # printTiles(tiles)

    # for i in range(1,8):
    #     print(within_shape_in_row(borderTiles(tiles),i))



    

    print(f"Task 1: {res1}\nTask 2: {res2}")


if __name__ == '__main__':
    main()
