from nose.tools import *
from ex49 import parser


def test_parse_sentence():
	result = parser.parse_sentence([('verb', 'run'), ('direction', 'north')])
	assert_equal(result, parser.Sentence('player', 'run', 'north'))


def test_parse_sentence2():
	result = parser.parse_sentence([('noun', 'bear'), ('verb', 'eat'), ('stop', 'the'), ('noun', 'honey')])
	assert_equal(result, parser.Sentence(subject='bear', verb='eat', obj='honey'))
