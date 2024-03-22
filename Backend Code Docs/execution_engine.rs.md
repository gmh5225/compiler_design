### Abstract 

### Public API
```rust
pub struct ExecutionEngine {
	engine: LLVMExecutionEngineRef,
	context: LLVMContextRef,
}

pub fn execute_ir(file_path: &str, function_name: &str, args: &[i64])

/// to import into a file
use crate::backend::execute::execution_engine::ExecutionEngine;
```

### Invariants
### Reading

Last Edited: 2024-02-29 22:57:55 -0500
