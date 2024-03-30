### Abstract 

A lexer (lexical analyzer) is a component in compilers and interpreters that processes input source code and breaks it down into a series of tokens. The lexer reads the source code character by character and groups these characters into tokens based on the syntax of the language. Token represents things like keywords, literals, identifiers, operators, and symbols. 

### Invariants
- Does not modify token's characters
- Reads the entire file
- Supports Unicode

### API
```rust
pub struct Lexer {
	input: Vec<char>, // Source code
	position: usize, // Current position in source code
	current: char, // Current character being read
}

pub fn lex(input: &str) -> Result<Vec<Token>, Vec<ErrorType>>

use crate::frontend::lexer::lexer_core::Lexer;
```

### Reading
Dragon book 42-60, 128-134

Last Edited: 2024-03-21 20:50:15 -0400
