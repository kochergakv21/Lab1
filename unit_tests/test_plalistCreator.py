from unittest import TestCase
from playlistcreator import PlaylistCreator

__author__ = 'kn1m'


class TestPlaylistCreator(TestCase):
    def test_get_urls_from_xml(self):
        s = PlaylistCreator('test.xml', 'res.xml', 0, 'Test')
        self.assertEqual(s.get_urls_from_xml(), ['http://itc.ua'])

    def test_get_tags_from_xml(self):
        s = PlaylistCreator('test.xml', 'res.xml', 0, 'Test')
        self.assertEqual(s.get_tags_from_xml(), [[u'div', u'class', u'sad']])

    def test_scrapper(self):
        s = PlaylistCreator('test.xml', 'res.xml', 0, 'Test')
        self.assertEqual(s.scrapper('file:///home/m3sc4/Study/AK/Lab1/unit_tests/test.html'), None)

