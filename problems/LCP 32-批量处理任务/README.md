# LCP 32. 批量处理任务

## 题目描述

某实验室计算机待处理任务以 `[start,end,period]` 格式记于二维数组 `tasks`，表示完成该任务的时间范围为起始时间 `start` 至结束时间 `end` 之间，需要计算机投入 `period` 的时长，注意：
1. `period` 可为不连续时间
2. 首尾时间均包含在内

处于开机状态的计算机可同时处理任意多个任务，请返回电脑最少开机多久，可处理完所有任务。

**示例 1：**
>输入：`tasks = [[1,3,2],[2,5,3],[5,6,2]]`
>
>输出：`4`
>
>解释：
>tasks[0] 选择时间点 2、3；
>tasks[1] 选择时间点 2、3、5；
>tasks[2] 选择时间点 5、6；
>因此计算机仅需在时间点 2、3、5、6 四个时刻保持开机即可完成任务。

**示例 2：**
>输入：`tasks = [[2,3,1],[5,5,1],[5,6,2]]`
>
>输出：`3`
>
>解释：
>tasks[0] 选择时间点 2 或 3；
>tasks[1] 选择时间点 5；
>tasks[2] 选择时间点 5、6；
>因此计算机仅需在时间点 2、5、6 或 3、5、6 三个时刻保持开机即可完成任务。

**提示：**
- `2 <= tasks.length <= 10^5`
- `tasks[i].length == 3`
- `0 <= tasks[i][0] <= tasks[i][1] <= 10^9`
- `1 <= tasks[i][2] <= tasks[i][1]-tasks[i][0] + 1`

## 难度

Hard

## 标签

- 贪心
- 数组
- 堆（优先队列）

## 示例

```
[[1,3,2],[2,5,3],[5,6,2]]
[[2,3,1],[5,5,1],[5,6,2]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int processTasks(vector<vector<int>>& tasks) {

    }
};
```

### Java

```java
class Solution {
    public int processTasks(int[][] tasks) {

    }
}
```

### Python

```python
class Solution(object):
    def processTasks(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def processTasks(self, tasks: List[List[int]]) -> int:
```

### C

```c


int processTasks(int** tasks, int tasksSize, int* tasksColSize){

}
```

### C#

```csharp
public class Solution {
    public int ProcessTasks(int[][] tasks) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} tasks
 * @return {number}
 */
var processTasks = function(tasks) {

};
```

### TypeScript

```typescript
function processTasks(tasks: number[][]): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $tasks
     * @return Integer
     */
    function processTasks($tasks) {

    }
}
```

### Swift

```swift
class Solution {
    func processTasks(_ tasks: [[Int]]) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun processTasks(tasks: Array<IntArray>): Int {

    }
}
```

### Go

```golang
func processTasks(tasks [][]int) int {

}
```

### Ruby

```ruby
# @param {Integer[][]} tasks
# @return {Integer}
def process_tasks(tasks)

end
```

### Scala

```scala
object Solution {
    def processTasks(tasks: Array[Array[Int]]): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn process_tasks(tasks: Vec<Vec<i32>>) -> i32 {

    }
}
```

### Racket

```racket
(define/contract (process-tasks tasks)
  (-> (listof (listof exact-integer?)) exact-integer?)

  )
```

