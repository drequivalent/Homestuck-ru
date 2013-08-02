from django.conf import settings
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.template import RequestContext
from glob import glob
import re
from os.path import join, basename

path_to_files = settings.HOMESTUCK_STORYFILES_DIR
start_page = "001901"

def parse_txt(page_number):
    txt_file = glob(join(path_to_files, "*", str(page_number)+".txt")) or \
               glob(join(path_to_files, "*", "*", str(page_number)+".txt"))

    contents = ""
    if txt_file:
        contents = file(txt_file[0]).read()
    else:
        raise ValueError, "No such page: " + page_number

    result = contents.split("###")
    result[5] = result[5].rstrip("\nX ").lstrip("\n")
    m = re.match(r"^\n\|(.*?)\|(.*)$", result[4], re.DOTALL)
    if(m):
        result[4] = render_to_string("log.html", { 'name': m.group(1), 'text' : m.group(2).lstrip("\n").replace("\n", "\n<br />\n") })
    return result

def display_page(request, page_number = start_page):
    title, wtf, wth, bogus_link, text, next_page_number = parse_txt(page_number)
    storyfiles = map(lambda x : join("storyfiles", basename(x)), bogus_link.split())
    try:
        next_page_title = parse_txt(next_page_number)[0]
    except ValueError:
        next_page_title = None
    return render_to_response(
        'display_page.html',
        { "title" : title, "text" : text, "next_page_title" : next_page_title, "next_page_number" : next_page_number,
	"prev_page" : str(int(page_number)-1).zfill(6) if page_number != start_page else "", "start_page" : start_page,
	"storyfiles" : storyfiles },
        context_instance=RequestContext(request)
    )
