import argparse
import csv

HTML_TEMPLATE = "template.html"
GALLERY_TOKEN = "[GALLERY_HERE]"

def buildHtmlGallery(reader):
    cols = 3
    htmlGallery = ''
    htmlGalleryRow = ''

    lineCount = 0
    for row in reader:
        lineCount += 1
        htmlGalleryRow += '\t<div class="col-md-4">\n'
        htmlGalleryRow += f'\t\t<input class="form-check-input" type="checkbox" value="" id="include-{lineCount}" checked>\n'
        htmlGalleryRow += f'\t\t<label class="form-check-label" for="include-{lineCount}">Include</label><br />\n'
        htmlGalleryRow += f'\t\t<img src="{row[0]}" id="image-{lineCount}" width="70%" />\n'
        htmlGalleryRow += '\t</div>\n'
        
        if lineCount % cols == 0:
            if htmlGalleryRow != '':
                htmlGallery += f'<div class="row mb-3">\n{htmlGalleryRow}</div>\n'
                htmlGalleryRow = ''

    if lineCount % cols == 2:
        htmlGallery += f'<div class="row mb-3">\n{htmlGalleryRow}\t<div class="col-md-4"></div>\n</div>\n'
    elif lineCount % cols == 1:
        htmlGallery += f'<div class="row mb-3">\n{htmlGalleryRow}\t<div class="col-md-4"></div>\n\t<div class="col-md-4"></div>\n</div>\n'

    return htmlGallery

def main(args):
    with open(args.input, mode='r', encoding='utf-8') as fd:
        reader = csv.reader(fd, delimiter='\t')
        htmlGallery = buildHtmlGallery(reader)

    with open(HTML_TEMPLATE, mode='r', encoding='utf-8') as fd:
        template = fd.read()
        contents = template.replace(GALLERY_TOKEN, htmlGallery)
    
    with open(args.output, mode='w', encoding='utf-8') as fd:
        fd.write(contents)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=str, default="in.csv")
    parser.add_argument("-o", "--output", type=str, default="out.html")
    args = parser.parse_args()
    main(args)