### Abstract

Semantic analysis in compilers and interpreters is the process of checking AST's for semantic correctness according to the rules of the language. This involves verifying that the use of Tokens in the code aligns with their definitions and complies with the language's semantics. Semantic analysis includes type checking, scope resolution, and identifying usage errors that are not syntactically incorrect but are semantically invalid.

### Invariants
- After semantic analysis, all AST's are well formed or there exists a vector of errors
- Well formed includes:
	- Type safe
	- Identifiers are declared before use
	- Primitives and variables are immutable by default
	- Scopes are enforced

### Public API

```rust
pub struct SemAnalysis {
    input: Module,
    current_sym_table_stack: Option<Arc<Mutex<SymbolTableStack>>>,
    rules: RulesConfig,
    current_table_index: i64,
}

pub fn sem_analysis(input: Module, rules: RulesConfig) -> Vec<ErrorType>;

use crate::frontend::analysis::sem_analysis::SemAnalysis;
```

### Reading
Dragon book 109-113

Last Edited: 2024-03-30 14:39:41 -0400
