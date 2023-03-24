# simple crdt data structure for python

## Contains

OR-Set
OR-Set (Observable Remove Set) is a set data structure that supports add and remove operations. Each element in the set is assigned a unique identifier, and adding an element generates a new identifier. Removing an element adds the identifier to a tombstone set, and the element is not included in the set from then on. The OR-Set guarantees that the addition and removal of elements are commutative and associative, and that they can be independently applied on different replicas without creating conflicts.

2P-Set
2P-Set (Two-Phase Set) is a set data structure that also supports add and remove operations. It is similar to the OR-Set but uses two sets to implement the add and remove operations. Adding an element is performed by adding it to the add set, and removing an element is performed by adding it to the remove set. The 2P-Set guarantees that adding an element is idempotent, and that removing an element is commutative and idempotent.

G-Counter
G-Counter (Grow-Only Counter) is a counter data structure that supports increment operations. Each replica maintains a local counter that can be incremented by adding 1. The sum of all local counters is the value of the G-Counter. The G-Counter guarantees that increments are commutative and associative, and that the counter value only increases over time.

PN-Counter
PN-Counter (Positive-Negative Counter) is a counter data structure that supports both increment and decrement operations. Each replica maintains two local G-Counters: one for positive increments and one for negative decrements. The value of the PN-Counter is the difference between the positive and negative counters. The PN-Counter guarantees that increments and decrements are commutative and associative, and that the counter value only changes between its initial value and its final value.

G-Set
G-Set (Grow-Only Set) is a set data structure that only supports add operations. Each replica maintains a set of elements that have been added to it. The G-Set guarantees that adding an element is commutative and associative, and that the set only grows over time.