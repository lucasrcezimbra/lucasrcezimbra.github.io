---
title: ast-grep by example
date: 2024-09-30
lastmod: 2024-10-07
---

- [ast-grep](https://github.com/ast-grep/ast-grep)


## Add a new argument to all self methods
```yaml
id: new-args-to-all-methods
language: python
rule:
    kind: parameters
    pattern: $$$ARGS
transform:
  INNER_ARGS:
    substring:
        source: $ARGS
        startChar: 1
        endChar: -1
  NEW_INNER_ARGS:
    replace:
      replace: 'self,?'
      by: 'self, <new_arg1>, <new_arg2>,'
      source: $INNER_ARGS
fix: '($NEW_INNER_ARGS)'
```

```diff
 def func1():
     ...

 def func2(args):
     ...

 class MyClass:
-    def method1(self):
+    def method1(self, <new_arg1>, <new_arg2>,):
         ...

-    def method2(self, args):
+    def method2(self, <new_arg1>, <new_arg2>, args):
         ...

     @classmethod
     def cls_method(cls):
         ...

     @staticmethod
     def static_method(cls):
         ...
```


## Alias import and replace identifiers
```yaml
id: replace-non-import-identifiers
language: python
rule:
    kind: identifier
    pattern: 'MyIdentifier'
    not:
      inside:
          kind: dotted_name
          inside:
              kind: import_from_statement
fix: 'MyNewIdentifier'
---
id: alias-import
language: python
rule:
    pattern: 'MyIdentifier'
    kind: identifier
    inside:
        kind: dotted_name
        inside:
            pattern: 'from x import $$$'
            kind: import_from_statement
fix: 'MyIdentifier as MyNewIdentifier'
```

```diff
-from x import MyIdentifier
+from x import MyIdentifier as MyNewIdentifier

-MyIdentifier.ABC
+MyNewIdentifier.ABC

 s = 'The MyIdentifier inside strings will not be changed.'
```


## Append to the body of a function
```yaml
id: append-to-function-body
language: python
rule:
    pattern: 'def user($$$ARGS): $$$BODY'
fix: |
    def user($$$ARGS):
        $$$BODY
        yield
        tear_down()
```

```diff
 @pytest.fixture
 def user():
     create_user()
+    yield
+    tear_down()
```


## Change function calls
```yaml
id: change-function-calls
language: python
rule:
    pattern: 'my_func'
    kind: identifier
    inside:
        kind: call
fix: 'my_new_func'
```

```diff
 from x import my_func

 my_func.X = ''
 s = 'my_func inside string will not be changed'

-my_func()
+my_new_func()
```
