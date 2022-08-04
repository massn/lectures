
// Generated from qasm3Lexer.g4 by ANTLR 4.10.1

#pragma once


#include "antlr4-runtime.h"




class  qasm3Lexer : public antlr4::Lexer {
public:
  enum {
    OPENQASM = 1, INCLUDE = 2, DEFCALGRAMMAR = 3, DEF = 4, CAL = 5, DEFCAL = 6, 
    GATE = 7, EXTERN = 8, BOX = 9, LET = 10, BREAK = 11, CONTINUE = 12, 
    IF = 13, ELSE = 14, END = 15, RETURN = 16, FOR = 17, WHILE = 18, IN = 19, 
    PRAGMA = 20, AnnotationKeyword = 21, INPUT = 22, OUTPUT = 23, CONST = 24, 
    MUTABLE = 25, QREG = 26, QUBIT = 27, CREG = 28, BOOL = 29, BIT = 30, 
    INT = 31, UINT = 32, FLOAT = 33, ANGLE = 34, COMPLEX = 35, ARRAY = 36, 
    DURATION = 37, STRETCH = 38, GPHASE = 39, INV = 40, POW = 41, CTRL = 42, 
    NEGCTRL = 43, DIM = 44, DURATIONOF = 45, DELAY = 46, RESET = 47, MEASURE = 48, 
    BARRIER = 49, BooleanLiteral = 50, LBRACKET = 51, RBRACKET = 52, LBRACE = 53, 
    RBRACE = 54, LPAREN = 55, RPAREN = 56, COLON = 57, SEMICOLON = 58, DOT = 59, 
    COMMA = 60, EQUALS = 61, ARROW = 62, PLUS = 63, DOUBLE_PLUS = 64, MINUS = 65, 
    ASTERISK = 66, DOUBLE_ASTERISK = 67, SLASH = 68, PERCENT = 69, PIPE = 70, 
    DOUBLE_PIPE = 71, AMPERSAND = 72, DOUBLE_AMPERSAND = 73, CARET = 74, 
    AT = 75, TILDE = 76, EXCLAMATION_POINT = 77, EqualityOperator = 78, 
    CompoundAssignmentOperator = 79, ComparisonOperator = 80, BitshiftOperator = 81, 
    IMAG = 82, ImaginaryLiteral = 83, BinaryIntegerLiteral = 84, OctalIntegerLiteral = 85, 
    DecimalIntegerLiteral = 86, HexIntegerLiteral = 87, Identifier = 88, 
    HardwareQubit = 89, FloatLiteral = 90, TimingLiteral = 91, BitstringLiteral = 92, 
    StringLiteral = 93, Whitespace = 94, Newline = 95, LineComment = 96, 
    BlockComment = 97, VERSION_IDENTIFER_WHITESPACE = 98, VersionSpecifier = 99, 
    EAT_INITIAL_SPACE = 100, EAT_LINE_END = 101, RemainingLineContent = 102, 
    CAL_PRELUDE_WHITESPACE = 103, CAL_PRELUDE_COMMENT = 104, DEFCAL_PRELUDE_WHITESPACE = 105, 
    DEFCAL_PRELUDE_COMMENT = 106, CalibrationBlock = 107
  };

  enum {
    VERSION_IDENTIFIER = 1, EAT_TO_LINE_END = 2, CAL_PRELUDE = 3, DEFCAL_PRELUDE = 4, 
    CAL_BLOCK = 5
  };

  explicit qasm3Lexer(antlr4::CharStream *input);

  ~qasm3Lexer() override;


  std::string getGrammarFileName() const override;

  const std::vector<std::string>& getRuleNames() const override;

  const std::vector<std::string>& getChannelNames() const override;

  const std::vector<std::string>& getModeNames() const override;

  const antlr4::dfa::Vocabulary& getVocabulary() const override;

  antlr4::atn::SerializedATNView getSerializedATN() const override;

  const antlr4::atn::ATN& getATN() const override;

  // By default the static state used to implement the lexer is lazily initialized during the first
  // call to the constructor. You can call this function if you wish to initialize the static state
  // ahead of time.
  static void initialize();

private:

  // Individual action functions triggered by action() above.

  // Individual semantic predicate functions triggered by sempred() above.

};

