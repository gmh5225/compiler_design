- C-like language
- Top level expressions:
	- Structs
	- Enums
	- Functions
	- Imports
- Other expressions:
	- if/elif/else
	- initialization/assignment of variables
	- match
	- while
	- for
	- do-while
- Ideas
	- Memory safety without garbage collection
	- Null safety
	- Variables immutable by default, unless specified as mutable
	- Type inference only for primitives?
	- Bake as little into the compiler as possible, let user decide their own usage

### Samples
```rust
pub fn foo(a: int, b: bool, c: str): bool {
	if (a == 0) {
		bar();
		return false;
	}
	elif (a == 1) {
		while (true) {
			break;
		}
	}
	else {
		match c {
			"abc" => {}
			"a" => {}
			_ => {}
		}
	}
	true
}

fn bar() {
	let mut x = 10;
	x = 15;
}

enum abc {
	some_type,
	some_other_type,
}
```