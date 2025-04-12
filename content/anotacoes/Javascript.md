---
title: "Javascript"
date: 2023-08-15
lastmod: 2025-04-12
---

## JavaScript for Pythonistas

### `dict.items()`
```javascript
for (const [key, value] of Object.entries(obj)) {
  console.log(key, value);
}
```


### `getattr`
```javascript
const value = obj[key];
```


### Transform a list of lists with key-values into a object
```javascript
const entries = [
  ['a', 1],
  ['b', 2],
];

const obj = Object.fromEntries(entries);

console.log(obj);
// Output: { a: 1, b: 2 }

```

### Use the value of a variable (instead of the variable name) as the key in an object
```javascript
const x = 'abc';

const obj = {
  [x]: '<whatever>'
};

console.log(obj);
// Output: { abc: '<whatever>' }

```

## TypeScript
### ReferenceError: ts is not defined at (...)
```typescript
import * as ts from 'typescript';
```
