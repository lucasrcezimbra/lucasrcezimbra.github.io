---
title: Simple Made Easy
date: 2025-01-09
lastmod: 2025-01-09
---

["Simple Made Easy" - Rich Hickey (2011)](https://www.youtube.com/watch?v=SxdOUGdseq4)

## TL;DR
- Simple vs. easy: simple means is not complex or entangled. Easy means
  familiar or near to our understanding.
- Construct vs. Artifact: construct is the codebase. Artifact is what we deliver
- We can make software simple by choosing constructs with simpler artifacts and
  avoiding constructs that have complex artifacts.
- Human limits: we can only keep a few things in our mind at a time
- The Complexity vs. Simplicity part was to abstract and doesn't have code
  examples


## Simple vs. Easy
### Simple
- one fold/braid: one role, one task, one concept
- but not: one instance, one operation
- about lack of interleaving, not cardinality
- objective

### Easy
- Near(by), at hand: on our hard drive, in our tool set, IDE, apt get, gem
  install, etc.
- Near to our understanding/skill set: familiar
- Near to our capabilities
- Easy is relative, unlike simple


## Construct vs Artifact
- Construct is the codebase
- Artifact is what we deliver
- We focus on experience of use of construct (programmer convenience and
  replaceability) rather than the long term results of use (software quality,
  correctness, maintenance, change)
- We must assess contructs by their artifacts


## Human Limits
- We can only hope to make reliable those things we can understand
- We can only consider (keep on our mind) a few things at a time
- Related to https://github.com/zakirullin/cognitive-load/


## Misc
> If you want everything to be familiar, you will never learn anything new,
> because it can't be significantly different from what you already know.

- Changes to software require analysis and decisions; What will be impacted?
  Where do changes need to be made?
- Debugging: all bugs pass the type checker and all the tests. All guard rails
  will fail
- Development Speed: emphasizing ease gives early speed, but ignoring
  complexity will slow you down over the long haul
- Software can be easy, but complex. Many complicating constructs are:
  succinctly described; familiar; available; easy to use.
- Benefits of Simplicity: ease understanding, changing, debugging, flexibility
- State is easy (in the at-hand and familiar senses), but it is never simple.
- There is the environmental complexity: shared resources, e.g. memory, CPU,
  etc. It's inherent (not your fault).
- Simplicity is a Choice: requires vigilance, sensibilities and care
- Information is Simple. Don't ruin it by hiding it behind micro-language (i.e.
  a class with information-specific methods). Represent data as data, no nned
  to write a class for every new data.
    - Missing examples


## Complexity vs. Simplicity
- Missing examples

| Complexity                    | Simplicity                    |
| ----------------------------- | ----------------------------- |
| State, Objects                | Values                        |
| Methods                       | Functions, Namespaces         |
| vars                          | Managed refs                  |
| Inheritance, switch, matching | Polymorphism a la carte       |
| Syntax                        | Data                          |
| Imperative loops, fold        | Set funcitons                 |
| Actors                        | Queues                        |
| ORM                           | Declarative data manipulation |
| Conditionals                  | Rules                         |
| Inconsistency                 | Consistency                   |


## The Complexity Toolkit
- Missing examples

| Construct              | Complects                      |
| ---------------------- | ------------------------------ |
| State                  | Everything that touches it     |
| Objects                | State, identity, value         |
| Methods                | Function and state, namespaces |
| Syntax                 | Meaning, order                 |
| Inheritance            | Types                          |
| Switch/matching        | Multiple who/what pairs        |
| var(iable)s            | Value, time                    |
| Imperative loops, fold | what/how                       |
| Actors                 | what/who                       |
| ORM                    | OMG                            |
| Conditionals           | Why, rest of program           |


## The Simplicity Toolkit
- Missing examples

| Construct                     | Get it via...                               |
| ----------------------------- | ------------------------------------------- |
| Values                        | final, persistent collections               |
| Functions                     | a.k.a. stateless methods                    |
| Namespaces                    | language support                            |
| Data                          | Maps, arrays, sets, XML, JSON, etc.         |
| Polymorphism a la carte       | (Clojure) Protocols, (Haskell) type classes |
| Managed refs                  | Clojure/Haskell refs                        |
| Set functions                 | Libraries                                   |
| Queues                        | Libraries                                   |
| Declarative data manipulation | SQL/LINQ/Datalog                            |
| Rules                         | Libraries, Prolog                           |
| Consistency                   | Transactions, Rules                         |


## Abstraction for Simplicity
- vs Abstraction as complexity hiding
- I don't know, I don't want to know
- Who, What, When, Where, Why and How
    - He lost me at that part


## Simplicity Made Easy
- Choose simple constructs over complexity-generating constructs
    - It's the artifacts, not the authoring
- Create abstractions with simplicity as a basis
- Simplify the problem space before you start
- Simplify often means making more things not fewer
