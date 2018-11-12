import SoundexAlgorithm

def test_WhenTheWordIsEmptyReturn0000():
    soundex = SoundexAlgorithm.SoundexAlgorithm()
    encodeword = soundex.Encode("")
    assert encodeword == "0000"

def test_WhenTheWordIsNoneReturn0000():
    soundex = SoundexAlgorithm.SoundexAlgorithm()
    encodeword = soundex.Encode(None)
    assert encodeword == "0000"

def test_WhenTheWordHaveOneCharThenFillTheWordBy0():
    soundex = SoundexAlgorithm.SoundexAlgorithm()
    encodeword = soundex.Encode("w")
    assert encodeword == "w000"

def test_WhenTheWordHaveUpperCaseThenChancgeToLowerCase():
    soundex = SoundexAlgorithm.SoundexAlgorithm()
    encodeword = soundex.Encode("WASD")
    assert encodeword == "w230"

def test_WhenTheWordHaveFourCharsWithDifferentNumbersThenReturnEncodedWord():
    soundex = SoundexAlgorithm.SoundexAlgorithm()
    encodeword = soundex.Encode("bcdm")
    assert encodeword == "b235"

def test_WhenTheWordHaveMoreThanOneCharAndLessThanFourCharsThenAdd0():
    soundex = SoundexAlgorithm.SoundexAlgorithm()
    encodeword = soundex.Encode("an")
    assert encodeword == "a500"

def test_WhenTheWordHaveMoreThanFourCharsThenRemoveRedundantChars():
    soundex = SoundexAlgorithm.SoundexAlgorithm()
    encodeword = soundex.Encode("anrtzv")
    assert encodeword == "a563"

def test_WhenTheWordHaveNeighboringCharsWithTheSameNumberThenRemoveAllThisCharsWitchoutFirst():
    soundex = SoundexAlgorithm.SoundexAlgorithm()
    encodeword = soundex.Encode("accb")
    assert encodeword == "a210"

def test_WhenTheWordHaveCharsWhichDoNotExistInDictionaryThenRemoveThisChars():
    soundex = SoundexAlgorithm.SoundexAlgorithm()
    encodeword = soundex.Encode("acob")
    assert encodeword == "a210"

def test_WhenTheWordHaveSpecialCharsThenReplaceThisCharsTo0():
    soundex = SoundexAlgorithm.SoundexAlgorithm()
    encodeword = soundex.Encode("!%#&")
    assert encodeword == "0000"

def test_WhenInTheWordTwoLettersWithTheSameNumberAreSeparatedByWThenEncodeLikeOneNumber():
    soundex = SoundexAlgorithm.SoundexAlgorithm()
    encodeword = soundex.Encode("bgwjlm")
    assert encodeword == "b245"

def test_WhenInTheWordTwoLettersWithTheSameNumberAreSeparatedByHThenEncodeLikeOneNumber():
    soundex = SoundexAlgorithm.SoundexAlgorithm()
    encodeword = soundex.Encode("bghjlm")
    assert encodeword == "b245"

def test_WhenInTheWordTwoLettersWithTheSameNumberAreSeparatedByVowelThenEncodeTwice():
    soundex = SoundexAlgorithm.SoundexAlgorithm()
    encodeword = soundex.Encode("bditv")
    assert encodeword == "b331"

def test_WhentTheWordIsRobertThenReturnR163():
    soundex = SoundexAlgorithm.SoundexAlgorithm()
    encodeword = soundex.Encode("Robert")
    assert encodeword == "r163"

def test_WhentTheWordIsRupertThenReturnR163():
    soundex = SoundexAlgorithm.SoundexAlgorithm()
    encodeword = soundex.Encode("Rupert")
    assert encodeword == "r163"

def test_WhentTheWordIsRubinThenReturnR150():
    soundex = SoundexAlgorithm.SoundexAlgorithm()
    encodeword = soundex.Encode("Rubin")
    assert encodeword == "r150"

def test_WhentTheWordIsAshcraftThenReturnA261():
    soundex = SoundexAlgorithm.SoundexAlgorithm()
    encodeword = soundex.Encode("Ashcraft")
    assert encodeword == "a261"

def test_WhentTheWordIsAshcroftThenReturnA261():
    soundex = SoundexAlgorithm.SoundexAlgorithm()
    encodeword = soundex.Encode("Ashcroft")
    assert encodeword == "a261"

def test_WhentTheWordIsTymczakThenReturnT522():
    soundex = SoundexAlgorithm.SoundexAlgorithm()
    encodeword = soundex.Encode("Tymczak")
    assert encodeword == "t522"

def test_WhentTheWordIsPfisterThenReturnP123():
    soundex = SoundexAlgorithm.SoundexAlgorithm()
    encodeword = soundex.Encode("Pfister")
    assert encodeword == "p123"

def test_WhentTheWordIsHoneymanThenReturnH555():
    soundex = SoundexAlgorithm.SoundexAlgorithm()
    encodeword = soundex.Encode("Honeyman")
    assert encodeword == "h555"