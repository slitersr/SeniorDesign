class Positions:
    # A1 x x x x x x A8
    # B1 x x x x x x B8
    # C1 x x x x x x C8
    # D1 x x x x x x D8
    # E1 x x x x x x E8
    # F1 x x x x x x F8
    # G1 x x x x x x G8
    # H1 x x x x x x H8
    
    joint1_table = [[265, 0, 0, 0, 0, 0, 0, 0],
                    [330, 0, 0, 0, 0, 0, 0, 0],
                    [420, 0, 0, 0, 0, 0, 0, 0],
                    [500, 0, 0, 0, 0, 0, 0, 0],
                    [570, 0, 0, 0, 0, 0, 0, 0],
                    [660, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0]]

    joint2_table = [[1023, 0, 0, 0, 0, 0, 0, 0],
                    [930, 0, 0, 0, 0, 0, 0, 0],
                    [848, 0, 0, 0, 0, 0, 0, 0],
                    [780, 0, 0, 0, 0, 0, 0, 0],
                    [720, 0, 0, 0, 0, 0, 0, 0],
                    [670, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0]]
    
    # Higher offset is for when magnet is too close to ground
    height_offset = [[0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0]]