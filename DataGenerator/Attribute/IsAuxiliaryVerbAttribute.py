from Classification.Attribute.BinaryAttribute import BinaryAttribute
from MorphologicalAnalysis.MorphologicalParse import MorphologicalParse


class IsAuxiliaryVerbAttribute(BinaryAttribute):

    """
    Binary attribute for a given word. If the word is an auxiliary verb, the attribute will have
    the value "true", otherwise "false".

    PARAMETERS
    ----------
    parse : MorphologicalParse
        Morphological parse of the word.
    """
    def __init__(self, parse: MorphologicalParse):
        super().__init__(parse.isAuxiliary() and parse.isVerb())