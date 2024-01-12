### Abstract

Semantic analysis in compilers and interpreters is the process of checking a source code's Abstract Syntax Tree (AST) for semantic correctness according to the rules of the programming language. This involves verifying that the use of variables, functions, types, and other constructs in the code aligns with their definitions and complies with the language's semantics. Semantic analysis typically includes type checking, scope resolution, and identifying usage errors that are not syntactically incorrect but are semantically invalid.

### Public API

```rust
pub struct SemAnalysis {
    input: AST,
    scope_stack: SymbolTableStack,
}

pub fn sem_analysis(input: AST) -> Vec<ErrorType>;

// to import into a file
use crate::frontend::analysis::sem_analysis::SemAnalysis;
```

### Reading

