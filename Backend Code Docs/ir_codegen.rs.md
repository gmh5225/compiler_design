### Abstract 

### Public API
```rust
pub struct IRGenerator {
	context: LLVMContextRef,
	module: LLVMModuleRef,
	builder: LLVMBuilderRef,
	named_values: HashMap<String, LLVMValueRef>
}
pub fn generate_ir(ast: &AST) -> LLVMModuleRef

/// to import into a file
use crate::backend::codegen::ir_codegen::IRGenerator;
```

### Reading