import re

# Define token categories
KEYWORDS = {'if', 'else', 'while', 'return', 'for', 'int', 'float', 'char', 'break', 'continue', 'double', 'void', 'include'}
OPERATORS = {'+', '-', '*', '/', '%', '==', '!=', '>', '<', '>=', '<=', '&&', '||', '!', '=', '++', '--'}
DELIMITERS = {';', '(', ')', '{', '}', '[', ']', ',', '#'}
LITERALS = re.compile(r'(".*?"|\'.*?\'|\d+\.\d+|\d+)')

# Identify token type
def classify_token(token):
    if token in KEYWORDS:
        return 'Keyword'
    elif re.match(r'[a-zA-Z_][a-zA-Z0-9_]*', token):
        return 'Identifier'
    elif re.match(LITERALS, token):
        return 'Literal'
    elif token in OPERATORS:
        return 'Operator'
    elif token in DELIMITERS:
        return 'Delimiter'
    else:
        return 'Unknown'

# Tokenizer function
def tokenize(program):
    # Regular expression for token patterns
    token_pattern = r'\w+|\".*?\"|\'.*?\'|[+\-*/%]=?|==|!=|[><]=?|&&|\|\||[{}();,]|#'
   
    # Find all tokens using the pattern
    tokens = re.findall(token_pattern, program)
   
    # Classify each token
    classified_tokens = [(token, classify_token(token)) for token in tokens]
   
    return classified_tokens

# Example input program
program_code = """
#include <stdio.h>
int main() {
    int a = 10;
    float b = 20.5;
    if (a > b) {
        printf("a is greater than b");
    } else {
        printf("b is greater than or equal to a");
    }
    return 0;
}
"""

# Tokenize the input program
tokens = tokenize(program_code)

# Print tokens and their types
for token, token_type in tokens:
    print(f"Token: {token}, Type: {token_type}")
