# SAT Solver

A simple SAT solver that checks the validity of a first-order logic formula using the **Davis-Putnam method**.

---

## Input Format

The input to the `davis_putnam` function is a **list of lists of integers**, where:
- **Integers represent literals**:
  - Positive integers represent variables.
  - Negative integers represent negated variables.
- **Inner lists represent clauses (disjunctions)**:
  - Each inner list is a disjunction of literals.
- **The outer list represents the CNF formula (a conjunction of clauses)**:
