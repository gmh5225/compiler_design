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

### Pseudocode

1. **Initialization**: `SemAnalysis::new` initializes the `SemAnalysis` with the input AST. A `SymbolTableStack` is also initialized to keep track of variable and function scopes.

2. **Semantic Analysis Process**: `SemAnalysis::sem_analysis` is the public method that performs semantic analysis on the input AST. It starts by pushing a new `SymbolTable` onto the stack for the global scope.

3. **Node Analysis**: The `node_analysis` method recursively traverses each node in the AST, performing specific semantic checks based on the type of syntax element, `ModuleExpression`, `BinaryExpression`, `IfStatement`, `Assignment`, etc.

4. **Error Handling**: If semantic errors are detected (e.g., division by zero, undefined variables, invalid assignments), they are added to a vector of `ErrorType`. This vector is returned after the analysis is complete, if nonempty.

5. **Utility Functions**: Functions like `is_zero` check if a node represents a zero value, and `is_variable_defined` checks if a variable is defined in the current scope.

6. **Scope Management**: When entering new scopes (e.g., in `IfStatement` or function bodies), a new `SymbolTable` is pushed onto the stack, and popped when exiting the scope.

### Reading

