from collections import namedtuple, deque
from itertools import combinations, pairwise

Coord = namedtuple('Coord', ['x', 'y'])

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

def area(coordA: Coord, coordB: Coord) -> int:
    return (abs(coordA.x - coordB.x) + 1)*(abs(coordA.y-coordB.y )+ 1)

def decompressed_area(coordA: Coord, coordB: Coord, decrompressor: dict[Coord, Coord]) -> int:
    actualA, actualB = decrompressor[coordA], decrompressor[coordB]
    return area(actualA, actualB)

def compress_shape(tiles: list[Coord]) -> tuple[list[Coord], dict[Coord, Coord]]:
    x_coords = {coord.x:i for i, coord in enumerate(sorted(tiles, key=lambda c: c.x))}
    y_coords = {coord.y:i for i, coord in enumerate(sorted(tiles, key=lambda c: c.y))}
    compressed_tiles, decrompressor = [], {}
    for coord in tiles:
        new_coord = Coord(x_coords[coord.x], y_coords[coord.y])
        compressed_tiles.append(new_coord)
        decrompressor[new_coord] = coord
    
    return compressed_tiles, decrompressor


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

def all_areas_and_part1(tiles: list[Coord], decompressor: dict[Coord, Coord]) -> tuple[list[tuple[int,Coord,Coord]], int]:
    areas: list[tuple[int,Coord,Coord]] = []
    for coordA, coordB in combinations(tiles, 2):
        areas.append((decompressed_area(coordA, coordB, decompressor), coordA, coordB))
    areas.sort(reverse=True)
    res1 = areas[0][0]
    return areas, res1


def solution_2(areas, border):
    for A, coord1, coord2 in areas:
        if rectWithin((coord1, coord2), border):
            return A

def main():
    tiles = []
    with open("input9.txt") as file:
        for row in file:
            tiles.append(Coord(*map(int, row.strip().split(','))))

    tiles, decompressor = compress_shape(tiles)
    areas, res1 = all_areas_and_part1(tiles, decompressor)
    border = borderTiles(tiles)

    res2 = solution_2(areas, border)

    print(f"Task 1: {res1}\nTask 2: {res2}")


if __name__ == '__main__':
    main()