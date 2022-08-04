# Generated from qasm3Parser.g4 by ANTLR 4.10.1
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by qasm3Parser.

class qasm3ParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by qasm3Parser#program.
    def visitProgram(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#version.
    def visitVersion(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#statement.
    def visitStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#annotation.
    def visitAnnotation(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#scope.
    def visitScope(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#pragma.
    def visitPragma(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#statementOrScope.
    def visitStatementOrScope(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#calibrationGrammarStatement.
    def visitCalibrationGrammarStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#includeStatement.
    def visitIncludeStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#breakStatement.
    def visitBreakStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#continueStatement.
    def visitContinueStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#endStatement.
    def visitEndStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#forStatement.
    def visitForStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#ifStatement.
    def visitIfStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#returnStatement.
    def visitReturnStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#whileStatement.
    def visitWhileStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#barrierStatement.
    def visitBarrierStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#boxStatement.
    def visitBoxStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#delayStatement.
    def visitDelayStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#gateCallStatement.
    def visitGateCallStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#measureArrowAssignmentStatement.
    def visitMeasureArrowAssignmentStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#resetStatement.
    def visitResetStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#aliasDeclarationStatement.
    def visitAliasDeclarationStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#classicalDeclarationStatement.
    def visitClassicalDeclarationStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#constDeclarationStatement.
    def visitConstDeclarationStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#ioDeclarationStatement.
    def visitIoDeclarationStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#oldStyleDeclarationStatement.
    def visitOldStyleDeclarationStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#quantumDeclarationStatement.
    def visitQuantumDeclarationStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#defStatement.
    def visitDefStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#externStatement.
    def visitExternStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#gateStatement.
    def visitGateStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#assignmentStatement.
    def visitAssignmentStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#expressionStatement.
    def visitExpressionStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#calStatement.
    def visitCalStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#defcalStatement.
    def visitDefcalStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#bitwiseXorExpression.
    def visitBitwiseXorExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#additiveExpression.
    def visitAdditiveExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#durationofExpression.
    def visitDurationofExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#parenthesisExpression.
    def visitParenthesisExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#comparisonExpression.
    def visitComparisonExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#logicalOrExpression.
    def visitLogicalOrExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#castExpression.
    def visitCastExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#powerExpression.
    def visitPowerExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#bitwiseOrExpression.
    def visitBitwiseOrExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#callExpression.
    def visitCallExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#bitshiftExpression.
    def visitBitshiftExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#bitwiseAndExpression.
    def visitBitwiseAndExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#equalityExpression.
    def visitEqualityExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#logicalAndExpression.
    def visitLogicalAndExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#indexExpression.
    def visitIndexExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#unaryExpression.
    def visitUnaryExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#literalExpression.
    def visitLiteralExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#aliasExpression.
    def visitAliasExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#declarationExpression.
    def visitDeclarationExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#measureExpression.
    def visitMeasureExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#rangeExpression.
    def visitRangeExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#setExpression.
    def visitSetExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#arrayLiteral.
    def visitArrayLiteral(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#indexOperator.
    def visitIndexOperator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#indexedIdentifier.
    def visitIndexedIdentifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#returnSignature.
    def visitReturnSignature(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#gateModifier.
    def visitGateModifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#scalarType.
    def visitScalarType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#qubitType.
    def visitQubitType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#arrayType.
    def visitArrayType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#arrayReferenceType.
    def visitArrayReferenceType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#designator.
    def visitDesignator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#defcalTarget.
    def visitDefcalTarget(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#defcalArgumentDefinition.
    def visitDefcalArgumentDefinition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#defcalOperand.
    def visitDefcalOperand(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#gateOperand.
    def visitGateOperand(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#externArgument.
    def visitExternArgument(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#argumentDefinition.
    def visitArgumentDefinition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#argumentDefinitionList.
    def visitArgumentDefinitionList(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#defcalArgumentDefinitionList.
    def visitDefcalArgumentDefinitionList(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#defcalOperandList.
    def visitDefcalOperandList(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#expressionList.
    def visitExpressionList(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#identifierList.
    def visitIdentifierList(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#gateOperandList.
    def visitGateOperandList(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by qasm3Parser#externArgumentList.
    def visitExternArgumentList(self, ctx):
        return self.visitChildren(ctx)


