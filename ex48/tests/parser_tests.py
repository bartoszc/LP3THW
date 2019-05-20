from nose.tools import *
from ex48 import parser


def test_parse_sentence():
	result = parser.parse_sentence([('verb', 'run'), ('direction', 'north')])
	assert_equal(result, parser.Sentence('player', 'run', 'north'))


def test_parse_sentence2():
	result = parser.parse_sentence([('noun', 'bear'), ('verb', 'eat'), ('stop', 'the'), ('noun', 'honey')])
	assert_equal(result, parser.Sentence(subject='bear', verb='eat', obj='honey'))


def test_parse_sentence3():
	word_list = lexicon.scan("run north")
	result = parser.parse_sentence(word_list)
	assert_equal(result, parser.Sentence('player', 'run', 'north'))


def test_parse_sentence4():
	word_list = lexicon.scan("bear eat the honey")
	result = parser.parse_sentence(word_list)
	assert_equal(result, parser.Sentence(subject='bear', verb='eat', obj='honey'))


def test_bad():
	word_list = lexicon.scan("the bear honey")
	with assert_raises(parser.ParserError) as cm:
		parser.parse_sentence(word_list)
	assert_equal(cm.exception.message, "Expected a verb next.")
