"""
Unit tests for scripts/data_loader.py
"""

import unittest
import xml.etree.ElementTree as ET
from scripts import data_loader as dl

class TestParse(unittest.TestCase):
	def test_parse_tree(self):
		self.assertRaises(FileNotFoundError, dl.parse_tree, "/data/imaginary.xml")
		self.assertRaises(IOError, dl.parse_tree, "/data/broken.xml")

	def test_return_default_text(self):
		xml_string = "<note><to>Tove</to><body><emph> this </emph></body></note>"
		sample_tree = ET.fromstring(xml_string)
		self.assertEqual(dl._return_default_text(sample_tree), "")
		self.assertEqual(dl._return_default_text(sample_tree.find(".//to")), "Tove")
		self.assertEqual(dl._return_default_text(sample_tree.find(".//body")), "")
		self.assertEqual(dl._return_default_text(sample_tree.find(".//emph")), " this ")

	def test_parse_pmid(self): # also same principle as ArticleTitle, AbstractText, JournalMeta and also Subject, Keyword (only add string concat step)
		xml_string = "<note><PMID>Tove</PMID><body><emph> this </emph></body></note>"
		sample_tree = ET.fromstring(xml_string)
		self.assertEqual(dl.parse_pmid(sample_tree), {"pmid": "Tove"})

		xml_string = "<note><to>Tove</to><body><PMID> this </PMID></body></note>"
		sample_tree = ET.fromstring(xml_string)
		self.assertEqual(dl.parse_pmid(sample_tree), {"pmid": " this "})

		xml_string = "<note><to>Tove</to><body><emph> this </emph></body></note>"
		sample_tree = ET.fromstring(xml_string)
		self.assertEqual(dl.parse_pmid(sample_tree), {"pmid": ""})

	def test_parse_article_meta(self):
		xml_string = "<note><PubmedData><ArticleIdList><ArticleId IdType='xxx'>aaa</ArticleId></ArticleIdList></PubmedData></note>"
		sample_tree = ET.fromstring(xml_string)
		self.assertEqual(dl.parse_article_meta(sample_tree), {"xxx": "aaa"})

		xml_string = "<note><PubmedData><ArticleIdList><ArticleId IdType='xxx'>aaa</ArticleId><ArticleId IdType='yyy'>bbb</ArticleId></ArticleIdList></PubmedData></note>"
		sample_tree = ET.fromstring(xml_string)
		self.assertEqual(dl.parse_article_meta(sample_tree), {"xxx": "aaa", "yyy": "bbb"})

		xml_string = "<note><PubmedData><ArticleIdList><ArticleIdFake IdType='xxx'>aaa</ArticleIdFake><ArticleId IdType='yyy'>bbb</ArticleId></ArticleIdList></PubmedData></note>"
		sample_tree = ET.fromstring(xml_string)
		self.assertEqual(dl.parse_article_meta(sample_tree), {"yyy": "bbb"})

	# can add more unit tests...
	# e.g., for parsing single tree, all tree, create df, query df



if __name__ == '__main__':
    unittest.main()