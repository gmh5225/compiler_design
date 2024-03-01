#FutureIdeas
```rust
/// Structs having custom pass-by traits
[#traits{pass-by: value}]
struct foo {}
```

```rust
/// Inherit block (can only be inherited, not initialized)
inherit foo {
	let el = "abc"
	pub fn foo(): String {
		"abcd"
	}
}

[#traits{pass-by: ownership}]
struct bar inherits[foo] {}

fn foobar(): String {
	print(bar.el); // prints "abc"
	bar.foo() // returns "abcd"
}
```

```rust
/// polymorphic structs
struct foo {
	el: str,
}

struct foo {
	el: str,
	next_el: str,
}
```

```rust
/// enums that can have variants of different types
enum foo {
	bar: String,
	foobar: int,
}

// can be assigned like this:
let a: foo = foo::bar("hello");
let b: foo = foo::foobar(123);
```

```rust
/// recursion block for simple recursive patterns

fn factorial(n: int): int {
	let result: int = 1;
	recurse {
		result *= n
		n -= 1
	} until {
		n <= 1
	}
	return result
}
```
- VSCode extension for syntax highlighting