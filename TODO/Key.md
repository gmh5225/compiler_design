All features and enhancements within our project are categorized using a unique identifier system designed to provide immediate insight into the scope and nature of each task. This identifier is a keyword structured as follows, with dashes between fields:

1. **Task Identifier**: A three-digit number uniquely identifying the task at a high level. 
    
2. **Feature Flag**: A single digit indicating whether the identifier refers to a new feature (`1`) or an enhancement/bug fix (`0`). 
    
3. **Subtask Identifier** (Optional): Following the high-level task identifier, a three-digit number provides specificity within the broader task category. This can be `000` to specify the user is taking all the subtasks of the larger task.

### Example

Given this system, an identifier such as `Tests-0-000` can be broken down as follows:

- `Tests` => The unique identifier of the overarching task
- `0` => The feature is an enhancement or bug fix, not something new
- `000` => The subtask identifier. If this were not provided, it would imply the developer is taking all subtasks for this task. 