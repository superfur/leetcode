# 3408. 设计任务管理器

## 题目描述

<p>一个任务管理器系统可以让用户管理他们的任务，每个任务有一个优先级。这个系统需要高效地处理添加、修改、执行和删除任务的操作。</p>

<p>请你设计一个&nbsp;<code>TaskManager</code>&nbsp;类：</p>

<ul>
	<li>
	<p><code>TaskManager(vector&lt;vector&lt;int&gt;&gt;&amp; tasks)</code>&nbsp;初始化任务管理器，初始化的数组格式为&nbsp;<code>[userId, taskId, priority]</code>&nbsp;，表示给 <code>userId</code>&nbsp;添加一个优先级为 <code>priority</code>&nbsp;的任务 <code>taskId</code>&nbsp;。</p>
	</li>
	<li>
	<p><code>void add(int userId, int taskId, int priority)</code>&nbsp;表示给用户 <code>userId</code>&nbsp;添加一个优先级为 <code>priority</code>&nbsp;的任务 <code>taskId</code>&nbsp;，输入 <strong>保证&nbsp;</strong><code>taskId</code>&nbsp;不在系统中。</p>
	</li>
	<li>
	<p><code>void edit(int taskId, int newPriority)</code>&nbsp;更新已经存在的任务&nbsp;<code>taskId</code>&nbsp;的优先级为&nbsp;<code>newPriority</code>&nbsp;。输入 <strong>保证</strong>&nbsp;<code>taskId</code>&nbsp;存在于系统中。</p>
	</li>
	<li>
	<p><code>void rmv(int taskId)</code>&nbsp;从系统中删除任务&nbsp;<code>taskId</code>&nbsp;。输入 <strong>保证</strong>&nbsp;<code>taskId</code>&nbsp;存在于系统中。</p>
	</li>
	<li>
	<p><code>int execTop()</code>&nbsp;执行所有用户的任务中优先级 <strong>最高</strong>&nbsp;的任务，如果有多个任务优先级相同且都为 <strong>最高</strong>&nbsp;，执行&nbsp;<code>taskId</code>&nbsp;最大的一个任务。执行完任务后，<code>taskId</code><strong>&nbsp;</strong>从系统中 <strong>删除</strong>&nbsp;。同时请你返回这个任务所属的用户&nbsp;<code>userId</code>&nbsp;。如果不存在任何任务，返回&nbsp;-1 。</p>
	</li>
</ul>

<p><strong>注意</strong> ，一个用户可能被安排多个任务。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><br />
<span class="example-io">["TaskManager", "add", "edit", "execTop", "rmv", "add", "execTop"]<br />
[[[[1, 101, 10], [2, 102, 20], [3, 103, 15]]], [4, 104, 5], [102, 8], [], [101], [5, 105, 15], []]</span></p>

<p><strong>输出：</strong><br />
<span class="example-io">[null, null, null, 3, null, null, 5] </span></p>

<p><strong>解释：</strong></p>
TaskManager taskManager = new TaskManager([[1, 101, 10], [2, 102, 20], [3, 103, 15]]); // 分别给用户 1 ，2 和 3 初始化一个任务。<br />
taskManager.add(4, 104, 5); // 给用户 4 添加优先级为 5 的任务 104 。<br />
taskManager.edit(102, 8); // 更新任务 102 的优先级为 8 。<br />
taskManager.execTop(); // 返回 3 。执行用户 3 的任务 103 。<br />
taskManager.rmv(101); // 将系统中的任务 101 删除。<br />
taskManager.add(5, 105, 15); // 给用户 5 添加优先级为 15 的任务 105 。<br />
taskManager.execTop(); // 返回 5 。执行用户 5 的任务 105 。</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= tasks.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= userId &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= taskId &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= priority &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= newPriority &lt;= 10<sup>9</sup></code></li>
	<li><code>add</code>&nbsp;，<code>edit</code>&nbsp;，<code>rmv</code>&nbsp;和&nbsp;<code>execTop</code>&nbsp;的总操作次数 <strong>加起来</strong>&nbsp;不超过&nbsp;<code>2 * 10<sup>5</sup></code> 次。</li>
	<li>输入保证&nbsp;<code>taskId</code> 是合法的。</li>
</ul>


## 难度

Medium

## 标签

- 设计
- 哈希表
- 有序集合
- 堆（优先队列）

## 示例

```
["TaskManager","add","edit","execTop","rmv","add","execTop"]
[[[[1,101,10],[2,102,20],[3,103,15]]],[4,104,5],[102,8],[],[101],[5,105,15],[]]
```

## 示例代码

### C++

```cpp
class TaskManager {
public:
    TaskManager(vector<vector<int>>& tasks) {
        
    }
    
    void add(int userId, int taskId, int priority) {
        
    }
    
    void edit(int taskId, int newPriority) {
        
    }
    
    void rmv(int taskId) {
        
    }
    
    int execTop() {
        
    }
};

/**
 * Your TaskManager object will be instantiated and called as such:
 * TaskManager* obj = new TaskManager(tasks);
 * obj->add(userId,taskId,priority);
 * obj->edit(taskId,newPriority);
 * obj->rmv(taskId);
 * int param_4 = obj->execTop();
 */
```

### Java

```java
class TaskManager {

    public TaskManager(List<List<Integer>> tasks) {
        
    }
    
    public void add(int userId, int taskId, int priority) {
        
    }
    
    public void edit(int taskId, int newPriority) {
        
    }
    
    public void rmv(int taskId) {
        
    }
    
    public int execTop() {
        
    }
}

/**
 * Your TaskManager object will be instantiated and called as such:
 * TaskManager obj = new TaskManager(tasks);
 * obj.add(userId,taskId,priority);
 * obj.edit(taskId,newPriority);
 * obj.rmv(taskId);
 * int param_4 = obj.execTop();
 */
```

### Python

```python
class TaskManager(object):

    def __init__(self, tasks):
        """
        :type tasks: List[List[int]]
        """
        

    def add(self, userId, taskId, priority):
        """
        :type userId: int
        :type taskId: int
        :type priority: int
        :rtype: None
        """
        

    def edit(self, taskId, newPriority):
        """
        :type taskId: int
        :type newPriority: int
        :rtype: None
        """
        

    def rmv(self, taskId):
        """
        :type taskId: int
        :rtype: None
        """
        

    def execTop(self):
        """
        :rtype: int
        """
        


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
```

### Python3

```python3
class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        

    def add(self, userId: int, taskId: int, priority: int) -> None:
        

    def edit(self, taskId: int, newPriority: int) -> None:
        

    def rmv(self, taskId: int) -> None:
        

    def execTop(self) -> int:
        


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
```

### C

```c



typedef struct {
    
} TaskManager;


TaskManager* taskManagerCreate(int** tasks, int tasksSize, int* tasksColSize) {
    
}

void taskManagerAdd(TaskManager* obj, int userId, int taskId, int priority) {
    
}

void taskManagerEdit(TaskManager* obj, int taskId, int newPriority) {
    
}

void taskManagerRmv(TaskManager* obj, int taskId) {
    
}

int taskManagerExecTop(TaskManager* obj) {
    
}

void taskManagerFree(TaskManager* obj) {
    
}

/**
 * Your TaskManager struct will be instantiated and called as such:
 * TaskManager* obj = taskManagerCreate(tasks, tasksSize, tasksColSize);
 * taskManagerAdd(obj, userId, taskId, priority);
 
 * taskManagerEdit(obj, taskId, newPriority);
 
 * taskManagerRmv(obj, taskId);
 
 * int param_4 = taskManagerExecTop(obj);
 
 * taskManagerFree(obj);
*/
```

### C#

```csharp
public class TaskManager {

    public TaskManager(IList<IList<int>> tasks) {
        
    }
    
    public void Add(int userId, int taskId, int priority) {
        
    }
    
    public void Edit(int taskId, int newPriority) {
        
    }
    
    public void Rmv(int taskId) {
        
    }
    
    public int ExecTop() {
        
    }
}

/**
 * Your TaskManager object will be instantiated and called as such:
 * TaskManager obj = new TaskManager(tasks);
 * obj.Add(userId,taskId,priority);
 * obj.Edit(taskId,newPriority);
 * obj.Rmv(taskId);
 * int param_4 = obj.ExecTop();
 */
```

### JavaScript

```javascript
/**
 * @param {number[][]} tasks
 */
var TaskManager = function(tasks) {
    
};

/** 
 * @param {number} userId 
 * @param {number} taskId 
 * @param {number} priority
 * @return {void}
 */
TaskManager.prototype.add = function(userId, taskId, priority) {
    
};

/** 
 * @param {number} taskId 
 * @param {number} newPriority
 * @return {void}
 */
TaskManager.prototype.edit = function(taskId, newPriority) {
    
};

/** 
 * @param {number} taskId
 * @return {void}
 */
TaskManager.prototype.rmv = function(taskId) {
    
};

/**
 * @return {number}
 */
TaskManager.prototype.execTop = function() {
    
};

/** 
 * Your TaskManager object will be instantiated and called as such:
 * var obj = new TaskManager(tasks)
 * obj.add(userId,taskId,priority)
 * obj.edit(taskId,newPriority)
 * obj.rmv(taskId)
 * var param_4 = obj.execTop()
 */
```

### TypeScript

```typescript
class TaskManager {
    constructor(tasks: number[][]) {
        
    }

    add(userId: number, taskId: number, priority: number): void {
        
    }

    edit(taskId: number, newPriority: number): void {
        
    }

    rmv(taskId: number): void {
        
    }

    execTop(): number {
        
    }
}

/**
 * Your TaskManager object will be instantiated and called as such:
 * var obj = new TaskManager(tasks)
 * obj.add(userId,taskId,priority)
 * obj.edit(taskId,newPriority)
 * obj.rmv(taskId)
 * var param_4 = obj.execTop()
 */
```

### PHP

```php
class TaskManager {
    /**
     * @param Integer[][] $tasks
     */
    function __construct($tasks) {
        
    }
  
    /**
     * @param Integer $userId
     * @param Integer $taskId
     * @param Integer $priority
     * @return NULL
     */
    function add($userId, $taskId, $priority) {
        
    }
  
    /**
     * @param Integer $taskId
     * @param Integer $newPriority
     * @return NULL
     */
    function edit($taskId, $newPriority) {
        
    }
  
    /**
     * @param Integer $taskId
     * @return NULL
     */
    function rmv($taskId) {
        
    }
  
    /**
     * @return Integer
     */
    function execTop() {
        
    }
}

/**
 * Your TaskManager object will be instantiated and called as such:
 * $obj = TaskManager($tasks);
 * $obj->add($userId, $taskId, $priority);
 * $obj->edit($taskId, $newPriority);
 * $obj->rmv($taskId);
 * $ret_4 = $obj->execTop();
 */
```

### Swift

```swift

class TaskManager {

    init(_ tasks: [[Int]]) {
        
    }
    
    func add(_ userId: Int, _ taskId: Int, _ priority: Int) {
        
    }
    
    func edit(_ taskId: Int, _ newPriority: Int) {
        
    }
    
    func rmv(_ taskId: Int) {
        
    }
    
    func execTop() -> Int {
        
    }
}

/**
 * Your TaskManager object will be instantiated and called as such:
 * let obj = TaskManager(tasks)
 * obj.add(userId, taskId, priority)
 * obj.edit(taskId, newPriority)
 * obj.rmv(taskId)
 * let ret_4: Int = obj.execTop()
 */
```

### Kotlin

```kotlin
class TaskManager(tasks: List<List<Int>>) {

    fun add(userId: Int, taskId: Int, priority: Int) {
        
    }

    fun edit(taskId: Int, newPriority: Int) {
        
    }

    fun rmv(taskId: Int) {
        
    }

    fun execTop(): Int {
        
    }

}

/**
 * Your TaskManager object will be instantiated and called as such:
 * var obj = TaskManager(tasks)
 * obj.add(userId,taskId,priority)
 * obj.edit(taskId,newPriority)
 * obj.rmv(taskId)
 * var param_4 = obj.execTop()
 */
```

### Dart

```dart
class TaskManager {

  TaskManager(List<List<int>> tasks) {
    
  }
  
  void add(int userId, int taskId, int priority) {
    
  }
  
  void edit(int taskId, int newPriority) {
    
  }
  
  void rmv(int taskId) {
    
  }
  
  int execTop() {
    
  }
}

/**
 * Your TaskManager object will be instantiated and called as such:
 * TaskManager obj = TaskManager(tasks);
 * obj.add(userId,taskId,priority);
 * obj.edit(taskId,newPriority);
 * obj.rmv(taskId);
 * int param4 = obj.execTop();
 */
```

### Go

```golang
type TaskManager struct {
    
}


func Constructor(tasks [][]int) TaskManager {
    
}


func (this *TaskManager) Add(userId int, taskId int, priority int)  {
    
}


func (this *TaskManager) Edit(taskId int, newPriority int)  {
    
}


func (this *TaskManager) Rmv(taskId int)  {
    
}


func (this *TaskManager) ExecTop() int {
    
}


/**
 * Your TaskManager object will be instantiated and called as such:
 * obj := Constructor(tasks);
 * obj.Add(userId,taskId,priority);
 * obj.Edit(taskId,newPriority);
 * obj.Rmv(taskId);
 * param_4 := obj.ExecTop();
 */
```

### Ruby

```ruby
class TaskManager

=begin
    :type tasks: Integer[][]
=end
    def initialize(tasks)
        
    end


=begin
    :type user_id: Integer
    :type task_id: Integer
    :type priority: Integer
    :rtype: Void
=end
    def add(user_id, task_id, priority)
        
    end


=begin
    :type task_id: Integer
    :type new_priority: Integer
    :rtype: Void
=end
    def edit(task_id, new_priority)
        
    end


=begin
    :type task_id: Integer
    :rtype: Void
=end
    def rmv(task_id)
        
    end


=begin
    :rtype: Integer
=end
    def exec_top()
        
    end


end

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager.new(tasks)
# obj.add(user_id, task_id, priority)
# obj.edit(task_id, new_priority)
# obj.rmv(task_id)
# param_4 = obj.exec_top()
```

### Scala

```scala
class TaskManager(_tasks: List[List[Int]]) {

    def add(userId: Int, taskId: Int, priority: Int): Unit = {
        
    }

    def edit(taskId: Int, newPriority: Int): Unit = {
        
    }

    def rmv(taskId: Int): Unit = {
        
    }

    def execTop(): Int = {
        
    }

}

/**
 * Your TaskManager object will be instantiated and called as such:
 * val obj = new TaskManager(tasks)
 * obj.add(userId,taskId,priority)
 * obj.edit(taskId,newPriority)
 * obj.rmv(taskId)
 * val param_4 = obj.execTop()
 */
```

### Rust

```rust
struct TaskManager {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl TaskManager {

    fn new(tasks: Vec<Vec<i32>>) -> Self {
        
    }
    
    fn add(&self, user_id: i32, task_id: i32, priority: i32) {
        
    }
    
    fn edit(&self, task_id: i32, new_priority: i32) {
        
    }
    
    fn rmv(&self, task_id: i32) {
        
    }
    
    fn exec_top(&self) -> i32 {
        
    }
}

/**
 * Your TaskManager object will be instantiated and called as such:
 * let obj = TaskManager::new(tasks);
 * obj.add(userId, taskId, priority);
 * obj.edit(taskId, newPriority);
 * obj.rmv(taskId);
 * let ret_4: i32 = obj.exec_top();
 */
```

### Racket

```racket
(define task-manager%
  (class object%
    (super-new)
    
    ; tasks : (listof (listof exact-integer?))
    (init-field
      tasks)
    
    ; add : exact-integer? exact-integer? exact-integer? -> void?
    (define/public (add user-id task-id priority)
      )
    ; edit : exact-integer? exact-integer? -> void?
    (define/public (edit task-id new-priority)
      )
    ; rmv : exact-integer? -> void?
    (define/public (rmv task-id)
      )
    ; exec-top : -> exact-integer?
    (define/public (exec-top)
      )))

;; Your task-manager% object will be instantiated and called as such:
;; (define obj (new task-manager% [tasks tasks]))
;; (send obj add user-id task-id priority)
;; (send obj edit task-id new-priority)
;; (send obj rmv task-id)
;; (define param_4 (send obj exec-top))
```

### Erlang

```erlang
-spec task_manager_init_(Tasks :: [[integer()]]) -> any().
task_manager_init_(Tasks) ->
  .

-spec task_manager_add(UserId :: integer(), TaskId :: integer(), Priority :: integer()) -> any().
task_manager_add(UserId, TaskId, Priority) ->
  .

-spec task_manager_edit(TaskId :: integer(), NewPriority :: integer()) -> any().
task_manager_edit(TaskId, NewPriority) ->
  .

-spec task_manager_rmv(TaskId :: integer()) -> any().
task_manager_rmv(TaskId) ->
  .

-spec task_manager_exec_top() -> integer().
task_manager_exec_top() ->
  .


%% Your functions will be called as such:
%% task_manager_init_(Tasks),
%% task_manager_add(UserId, TaskId, Priority),
%% task_manager_edit(TaskId, NewPriority),
%% task_manager_rmv(TaskId),
%% Param_4 = task_manager_exec_top(),

%% task_manager_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule TaskManager do
  @spec init_(tasks :: [[integer]]) :: any
  def init_(tasks) do
    
  end

  @spec add(user_id :: integer, task_id :: integer, priority :: integer) :: any
  def add(user_id, task_id, priority) do
    
  end

  @spec edit(task_id :: integer, new_priority :: integer) :: any
  def edit(task_id, new_priority) do
    
  end

  @spec rmv(task_id :: integer) :: any
  def rmv(task_id) do
    
  end

  @spec exec_top() :: integer
  def exec_top() do
    
  end
end

# Your functions will be called as such:
# TaskManager.init_(tasks)
# TaskManager.add(user_id, task_id, priority)
# TaskManager.edit(task_id, new_priority)
# TaskManager.rmv(task_id)
# param_4 = TaskManager.exec_top()

# TaskManager.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class TaskManager {
    init(tasks: ArrayList<ArrayList<Int64>>) {

    }
    
    func add(userId: Int64, taskId: Int64, priority: Int64): Unit {

    }
    
    func edit(taskId: Int64, newPriority: Int64): Unit {

    }
    
    func rmv(taskId: Int64): Unit {

    }
    
    func execTop(): Int64 {

    }
}

/**
 * Your TaskManager object will be instantiated and called as such:
 * let obj: TaskManager = TaskManager(tasks)
 * obj.add(userId,taskId,priority)
 * obj.edit(taskId,newPriority)
 * obj.rmv(taskId)
 * let param_4 = obj.execTop()
 */
```

