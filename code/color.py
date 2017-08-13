# RGB
def color_code_to_rbg_tuple(color_code):
    """
    e.g. "#FF0000" => (255, 0, 0)
    """
    code_r = color_code[1:3]
    code_g = color_code[3:5]
    code_b = color_code[5:7]
    r = int(code_r, 16)
    g = int(code_g, 16)
    b = int(code_b, 16)
    return r, g, b


# BGR for cv2
def color_code_to_bgr_tuple(color_code):
    rgb = color_code_to_rbg_tuple(color_code)
    return rgb[2], rgb[1], rgb[0]


if __name__ == '__main__':
    col = color_code_to_rbg_tuple("#FF0000")
    print(col)