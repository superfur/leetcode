# 2358. 分组的最大数量

## 题目描述

<p>给你一个正整数数组 <code>grades</code> ，表示大学中一些学生的成绩。你打算将 <strong>所有</strong> 学生分为一些 <strong>有序</strong> 的非空分组，其中分组间的顺序满足以下全部条件：</p>

<ul>
	<li>第 <code>i</code> 个分组中的学生总成绩 <strong>小于</strong> 第 <code>(i + 1)</code> 个分组中的学生总成绩，对所有组均成立（除了最后一组）。</li>
	<li>第 <code>i</code> 个分组中的学生总数 <strong>小于</strong> 第 <code>(i + 1)</code> 个分组中的学生总数，对所有组均成立（除了最后一组）。</li>
</ul>

<p>返回可以形成的 <strong>最大</strong> 组数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>grades = [10,6,12,7,3,5]
<strong>输出：</strong>3
<strong>解释：</strong>下面是形成 3 个分组的一种可行方法：
- 第 1 个分组的学生成绩为 grades = [12] ，总成绩：12 ，学生数：1
- 第 2 个分组的学生成绩为 grades = [6,7] ，总成绩：6 + 7 = 13 ，学生数：2
- 第 3 个分组的学生成绩为 grades = [10,3,5] ，总成绩：10 + 3 + 5 = 18 ，学生数：3 
可以证明无法形成超过 3 个分组。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>grades = [8,8]
<strong>输出：</strong>1
<strong>解释：</strong>只能形成 1 个分组，因为如果要形成 2 个分组的话，会导致每个分组中的学生数目相等。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= grades.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= grades[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 数学
- 二分查找

## 提示

1. Would it be easier to place the students into valid groups after sorting them based on their grades in ascending order?
2. Notice that, after sorting, we can separate them into groups of sizes 1, 2, 3, and so on.
3. If the last group is invalid, we can merge it with the previous group.
4. This creates the maximum number of groups because we always greedily form the smallest possible group.

## 示例

```
[10,6,12,7,3,5]
[8,8]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximumGroups(vector<int>& grades) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximumGroups(int[] grades) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumGroups(self, grades):
        """
        :type grades: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        
```

### C

```c
int maximumGroups(int* grades, int gradesSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximumGroups(int[] grades) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} grades
 * @return {number}
 */
var maximumGroups = function(grades) {
    
};
```

### TypeScript

```typescript
function maximumGroups(grades: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $grades
     * @return Integer
     */
    function maximumGroups($grades) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumGroups(_ grades: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumGroups(grades: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumGroups(List<int> grades) {
    
  }
}
```

### Go

```golang
func maximumGroups(grades []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} grades
# @return {Integer}
def maximum_groups(grades)
    
end
```

### Scala

```scala
object Solution {
    def maximumGroups(grades: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_groups(grades: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-groups grades)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_groups(Grades :: [integer()]) -> integer().
maximum_groups(Grades) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_groups(grades :: [integer]) :: integer
  def maximum_groups(grades) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumGroups(grades: Array<Int64>): Int64 {

    }
}
```

