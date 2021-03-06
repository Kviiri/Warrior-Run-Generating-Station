# This is a file which defines the attributes of this agent.
# Please follow the example.
#
# NB! For determining the function name we are parsing the source code. Please
# do not put a spacebar between the function name and parenthesis.
# NNB! In the name (e.g. Phrase length (standard)), the suffix (standard) refers
# to the fact, that these are methods, which come with the original source.
# For your own methods not add anything to the parenthesis (e.g. the example of numberOfWords)
# NNB! Please add your first name and first letter of your last name in front of 
# the function name. This is for avoiding clashing of the attribute names.
#
<sampleattribute>
# This attribute is not included and is considered an example. This is included
# as a standard attribute below
<name>
number of words
</name>
<function>
def numberOfWords(phrase):
	return len(phrase.split)
	</function>
</sampleattribute>

<attribute>
<name>
phrase length (standard)
</name>
	<function>
def phraseLength(phrase):
	return len(phrase)
	</function>
</attribute>

<attribute>
<name>
phrase vowels (standard)
</name>
<function>
def phraseVowels(phrase):
	vowels = "aeiou"
	return len(filter(lambda x: x in vowels, phrase))
</function>
</attribute>

<attribute>
<name>
phrase consonants (standard)
</name>
<function>
def phraseConsonants(phrase):
	consonants = "bcdfghjklmnpqrstv"
	return len(filter(lambda x: x in consonants, phrase))
	</function>
</attribute>

<attribute>
# This attribute is not included and is considered an example.
<name>
number of words (standard)
</name>
<function>
def numberOfWords(phrase):
	return len(phrase.split())
	</function>
</attribute>

<attribute>
# This attribute is not included and is considered an example.
<name>
string length
</name>
<function>
def strLen(phrase):
	return len(phrase)
	</function>
</attribute>