### Abstract 

A lexer (lexical analyzer) is a component in compilers and interpreters that processes input source code and breaks it down into a series of tokens. The lexer reads the source code character by character and groups these characters into meaningful sequences (tokens) based on predefined rules. Each token represents things like an atomic element of the language, such as keywords, literals, identifiers, operators, and symbols. These tokens are fundamental building blocks for the parser to understand and construct an abstract syntax tree from the source file.

### Public API

```rust
pub struct Lexer {
	input: Vec<char>, // Source code
	position: usize, // Current position in source code
	current: char, // Current character being read
}

pub fn lex(input: &str) -> Result<Vec<Token>, Vec<ErrorType>>

// to import into a file
use crate::frontend::syntax::lexer::Lexer;
```

### Pseudocode

1. **Initialization**: `Lexer::new` initializes the `Lexer` with the input string converted into a vector of characters. The current position is set to 0, and the current character is initially set to a placeholder representing the end of file (EOF). The (EOF) token will be appended once to the output, after reading each token.

2. **Tokenization Process**: `Lexer::lex` is the public method that tokenizes the entire input string. It repeatedly calls `next_token` to process the input and accumulate tokens until the end of the input is reached.

3. **Handling Individual Tokens**: The `next_token` method skips whitespace and then, based on the current character, determines the appropriate token. It handles different categories like operators, brackets, identifiers, integers, etc. 

4. **Error Handling**: If an unrecognized character is encountered, an error token is generated, indicating an unrecognized token. It is then added to the final output, which will now be a vector of errors, and not a vector of tokens.
### Reading
https://ieeexplore.ieee.org/document/7755127