import sys, getopt
from PIL import Image
from itertools import groupby


def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print ('image2HTML.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('image2HTML.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    
    # Read Image
    im = Image.open(inputfile).convert('RGB')
    width, height = im.size
    pixels = im.load()
    
    # Write file
    with open(outputfile,'w') as f:
        f.write(process(width, height, pixels))

# RGB to HEX color
def tup2hex(rgb_tup):
    t2h = '#%02x%02x%02x' % rgb_tup
    if t2h[1:].count(t2h[1]) == 6:
        return t2h[:4]
    else:
        return t2h

# Slice pixels into rows
def slice_it(hex_pixels, height):
    rows_list = []
    start = 0
    for i in range(height):
        stop = start + len(hex_pixels[i::height])
        rows_list.append(hex_pixels[start:stop])
        start = stop
    return rows_list

# Process image data -> html
def process(width, height, pixels):
    output = f'''<html><head></head><style>td{{height:1;padding:0;}}
              table{{border-spacing:0;width:{width}}}</style><center>
              <table><tr>'''

    # Convert all pixels to hex format
    hex_pixels = [tup2hex(pixels[x,y]) for y in range(height) for x in range(width)]
    
    # Group the consecutive pixels with
    # the same color in the same row into single html statement
    # e.g. instead of multiple <td width=1 bgcolor=#000 /> make
    # one with higher width <td width=100 bgcolor=#000 />
    output_list = []
    for l in slice_it(hex_pixels, height):
        tpl = [(k, sum(1 for i in g)) for k,g in groupby(l)]
        output_list.extend(tpl)
        
    # Convert to HTML
    count = 0
    for d in output_list:
        output += f'<td width={d[1]} bgcolor={d[0]} />'
        count += d[1]
        if count % width == 0:
            output += '</tr></table><table><tr>'
    output += '</tr></table></center></html>'
    return output

if __name__ == "__main__":
    main(sys.argv[1:])
