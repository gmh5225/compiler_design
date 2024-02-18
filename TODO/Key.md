All features and enhancements within our project are categorized using a unique identifier system designed to provide immediate insight into the scope, nature, and ownership of each task. This identifier is a keyword structured as follows, with dashes between fields (no field is optional):

1. **Domain Identifier**: Each task is first classified based on the primary area(s) it impacts:
    - `f` for frontend
    - `b` for backend
    - `m` for miscellaneous tasks that may not directly relate to the frontend or backend
    
    Tasks spanning multiple domains will include multiple identifiers in sequence (e.g., `fb` for tasks affecting both frontend and backend).
    
2. **Task Identifier**: A three-digit number uniquely identifying the task at a high level. 
    
3. **Feature Flag**: A single digit indicating whether the identifier refers to a new feature (`1`) or an enhancement/bug fix (`0`). This distinction helps in prioritizing and managing the development workflow.
    
4. **Subtask Identifier**: Following the high-level task identifier, a three-digit number provides specificity within the broader task category. This can be `000` to specify the user is taking all the subtasks of the larger task.
    
5. **Developer Identifier**: The identifier concludes with a two-digit code assigned to the developer responsible for the task.

### Example

Given this system, an identifier such as `fbm-001-1-000-07` can be broken down as follows:

- `fbm` indicates the task spans frontend, backend, and includes miscellaneous components.
- `001` is the high-level task identifier, suggesting a major area or feature within the project.
- `1` signifies that this is a new feature.
- `000` is the subtask identifier (all subtasks)
- `07` is the developer identifier, pointing to the specific team member responsible for overseeing or implementing this task.