# 2798. 满足目标工作时长的员工数目

## 题目描述

<p>公司里共有 <code>n</code> 名员工，按从 <code>0</code> 到 <code>n - 1</code> 编号。每个员工 <code>i</code> 已经在公司工作了 <code>hours[i]</code> 小时。</p>

<p>公司要求每位员工工作&nbsp;<strong>至少</strong> <code>target</code> 小时。</p>

<p>给你一个下标从 <strong>0</strong> 开始、长度为 <code>n</code> 的非负整数数组 <code>hours</code> 和一个非负整数 <code>target</code> 。</p>

<p>请你用整数表示并返回工作至少 <code>target</code> 小时的员工数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>hours = [0,1,2,3,4], target = 2
<strong>输出：</strong>3
<strong>解释：</strong>公司要求每位员工工作至少 2 小时。
- 员工 0 工作 0 小时，不满足要求。
- 员工 1 工作 1 小时，不满足要求。
- 员工 2 工作 2 小时，满足要求。
- 员工 3 工作 3 小时，满足要求。
- 员工 4 工作 4 小时，满足要求。
共有 3 位满足要求的员工。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>hours = [5,1,4,2,2], target = 6
<strong>输出：</strong>0
<strong>解释：</strong>公司要求每位员工工作至少 6 小时。
共有 0 位满足要求的员工。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n == hours.length &lt;= 50</code></li>
	<li><code>0 &lt;=&nbsp;hours[i], target &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 数组

## 提示

1. Iterate over the elements of array hours and check if the value is greater than or equal to target.

## 示例

```
[0,1,2,3,4]
2
[5,1,4,2,2]
6
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numberOfEmployeesWhoMetTarget(vector<int>& hours, int target) {
        
    }
};
```

### Java

```java
class Solution {
    public int numberOfEmployeesWhoMetTarget(int[] hours, int target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        
```

### C

```c
int numberOfEmployeesWhoMetTarget(int* hours, int hoursSize, int target) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumberOfEmployeesWhoMetTarget(int[] hours, int target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} hours
 * @param {number} target
 * @return {number}
 */
var numberOfEmployeesWhoMetTarget = function(hours, target) {
    
};
```

### TypeScript

```typescript
function numberOfEmployeesWhoMetTarget(hours: number[], target: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $hours
     * @param Integer $target
     * @return Integer
     */
    function numberOfEmployeesWhoMetTarget($hours, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numberOfEmployeesWhoMetTarget(_ hours: [Int], _ target: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numberOfEmployeesWhoMetTarget(hours: IntArray, target: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numberOfEmployeesWhoMetTarget(List<int> hours, int target) {
    
  }
}
```

### Go

```golang
func numberOfEmployeesWhoMetTarget(hours []int, target int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} hours
# @param {Integer} target
# @return {Integer}
def number_of_employees_who_met_target(hours, target)
    
end
```

### Scala

```scala
object Solution {
    def numberOfEmployeesWhoMetTarget(hours: Array[Int], target: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn number_of_employees_who_met_target(hours: Vec<i32>, target: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (number-of-employees-who-met-target hours target)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec number_of_employees_who_met_target(Hours :: [integer()], Target :: integer()) -> integer().
number_of_employees_who_met_target(Hours, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec number_of_employees_who_met_target(hours :: [integer], target :: integer) :: integer
  def number_of_employees_who_met_target(hours, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numberOfEmployeesWhoMetTarget(hours: Array<Int64>, target: Int64): Int64 {

    }
}
```

