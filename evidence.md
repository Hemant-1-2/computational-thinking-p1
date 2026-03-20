Old Hash: (8890103da2ff0dae736a36e3e2b4fcd060a6cb4a)

New Hash: (b4c76947efc6ba0da41a2e515fae4391456109eb)

Explanation:
When we modified the commit message using the command `git commit --amend`, 
the commit hash changed.

This happened because Git does not allow modification of an existing commit. 
Instead, it creates a new commit with a new hash.

The commit hash depends on the commit content, message, and timestamp. 
Since the message was changed, a new hash was generated.

This proves that Git commits are immutable (cannot be changed once created).