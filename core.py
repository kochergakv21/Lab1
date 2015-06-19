
from playlistcreator import PlaylistCreator
import time


def main():

    conf_file = open('run.conf', "r")
    param = conf_file.readline()
    depth = conf_file.readline()
    genre = conf_file.readline()
    print 'Program mode: ', param, 'Depth: ', depth, 'Genre: ', genre

    scrappy = PlaylistCreator(input_path='urls.xml', output_path='res.xml', given_depth=depth, genre=genre)
    urls = scrappy.get_urls_from_xml()
    tags = scrappy.get_tags_from_xml()

    if param == 'gevent\n':
        scrappy.multitask_scrapper(urls)
        scrappy.write_xml()
    elif param == 'non-gevent\n':
        for url in urls:
            scrappy.scrapper(url)
        scrappy.write_xml()
    else:
        raise RuntimeError("Unexpected or no mode selected. Check run.conf and select mod: 'gevent' or 'non-gevent'")

start_time = time.time()
main()
print '--- %s seconds ---' % (time.time() - start_time)

