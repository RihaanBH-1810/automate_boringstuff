def validatechess(chess_dict):
    key_list = list(chess_dict.keys())
    value_list = list(chess_dict.values())

    piece_count = {'bking' :1, 'wking' : 1, 'bpawn' : 8, 'wpawn': 8, 'wbishop': 2, 'wknight':2, 'wrook':2,'wqueen':1, 'bbishop': 2, 'bknight':2, 'brook':2,'bqueen':1 } 
    for piece in value_list:
        if piece in piece_count:
            if value_list.count(piece) > piece_count[piece]:
                return False
        else:return False
    
    for pos in key_list:
        if int(pos[0]) > 8:
            return False
        elif pos[1] > 'h':
            return False
    
    return True
    
ch = {'1h': 'bking', '6c': 'wqueen',
'2g': 'bishop', '5h': 'bqueen', '3e': 'wking'}


print(validatechess(ch))