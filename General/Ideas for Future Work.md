
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

#[traits{pass-by: ownership}]
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

- Store functions in variables, passed as arguments, returned form other functions