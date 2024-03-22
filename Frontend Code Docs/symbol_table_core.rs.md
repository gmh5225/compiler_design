#### Abstract
The symbol table stack  manages symbol information throughout the compilation process. It ensures that each identifier's scope and details are tracked.

### Invariants
- SymbolTableStack maintains a hierarchical scope structure
- SymbolTable uniquely identifies symbols within a single scope

### API
``` rust
pub struct SymbolTableStack {
	elements: Vec<Arc<Mutex<SymbolTable>>>,
}

pub struct SymbolTable {
	values: HashMap<String, SymbolInfo>,
}

pub fn gen_sym_table_stack(ast: AST) -> Result<(AST, SymbolTableStack), Vec<ErrorType>> 

use crate::frontend::symbol_table::symbol_table_struct::SymbolTableStack;
```

### Reading
Dragon book 85-91
Last Edited: 2024-03-21 20:15:39 -0400
