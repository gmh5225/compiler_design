### Abstract 

A lexer (lexical analyzer) is a component in compilers and interpreters that processes input source code and breaks it down into a series of tokens. The lexer reads the source code character by character and groups these characters into meaningful sequences (tokens) based on predefined rules. Each token represents things like an atomic element of the language, such as keywords, literals, identifiers, operators, and symbols. These tokens are fundamental building blocks for the parser to understand and construct an abstract syntax tree from the source file.

### Invariants

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

### Reading
https://ieeexplore.ieee.org/document/7755127

Last Edited: 2024-02-29 22:35:40 -0500
