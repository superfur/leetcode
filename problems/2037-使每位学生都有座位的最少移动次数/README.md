# 2037. 使每位学生都有座位的最少移动次数

## 题目描述

<p>一个房间里有 <code>n</code>&nbsp;个 <strong>空闲</strong> 座位和 <code>n</code>&nbsp;名 <strong>站着的</strong>&nbsp;学生，房间用一个数轴表示。给你一个长度为 <code>n</code>&nbsp;的数组&nbsp;<code>seats</code>&nbsp;，其中&nbsp;<code>seats[i]</code> 是第 <code>i</code>&nbsp;个座位的位置。同时给你一个长度为 <code>n</code>&nbsp;的数组&nbsp;<code>students</code>&nbsp;，其中&nbsp;<code>students[j]</code>&nbsp;是第 <code>j</code>&nbsp;位学生的位置。</p>

<p>你可以执行以下操作任意次：</p>

<ul>
	<li>增加或者减少第&nbsp;<code>i</code>&nbsp;位学生的位置，每次变化量为 <code>1</code>&nbsp;（也就是将第 <code>i</code>&nbsp;位学生从位置 <code>x</code>&nbsp;移动到 <code>x + 1</code>&nbsp;或者 <code>x - 1</code>）</li>
</ul>

<p>请你返回使所有学生都有座位坐的 <strong>最少移动次数</strong>&nbsp;，并确保没有两位学生的座位相同。</p>

<p>请注意，初始时有可能有多个座位或者多位学生在 <strong>同一</strong>&nbsp;位置。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>seats = [3,1,5], students = [2,7,4]
<b>输出：</b>4
<b>解释：</b>学生移动方式如下：
- 第一位学生从位置 2 移动到位置 1 ，移动 1 次。
- 第二位学生从位置 7 移动到位置 5 ，移动 2 次。
- 第三位学生从位置 4 移动到位置 3 ，移动 1 次。
总共 1 + 2 + 1 = 4 次移动。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>seats = [4,1,5,9], students = [1,3,2,6]
<b>输出：</b>7
<strong>解释：</strong>学生移动方式如下：
- 第一位学生不移动。
- 第二位学生从位置 3 移动到位置 4 ，移动 1 次。
- 第三位学生从位置 2 移动到位置 5 ，移动 3 次。
- 第四位学生从位置 6 移动到位置 9 ，移动 3 次。
总共 0 + 1 + 3 + 3 = 7 次移动。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<b>输入：</b>seats = [2,2,6,6], students = [1,3,2,6]
<b>输出：</b>4
<b>解释：</b>学生移动方式如下：
- 第一位学生从位置 1 移动到位置 2 ，移动 1 次。
- 第二位学生从位置 3 移动到位置 6 ，移动 3 次。
- 第三位学生不移动。
- 第四位学生不移动。
总共 1 + 3 + 0 + 0 = 4 次移动。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == seats.length == students.length</code></li>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>1 &lt;= seats[i], students[j] &lt;= 100</code></li>
</ul>


## 难度

Easy

## 标签

- 贪心
- 数组
- 计数排序
- 排序

## 提示

1. Can we sort the arrays to help solve the problem?
2. Can we greedily match each student to a seat?
3. The smallest positioned student will go to the smallest positioned chair, and then the next smallest positioned student will go to the next smallest positioned chair, and so on.

## 示例

```
[3,1,5]
[2,7,4]
[4,1,5,9]
[1,3,2,6]
[2,2,6,6]
[1,3,2,6]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minMovesToSeat(vector<int>& seats, vector<int>& students) {
        
    }
};
```

### Java

```java
class Solution {
    public int minMovesToSeat(int[] seats, int[] students) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        
```

### C

```c
int minMovesToSeat(int* seats, int seatsSize, int* students, int studentsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinMovesToSeat(int[] seats, int[] students) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} seats
 * @param {number[]} students
 * @return {number}
 */
var minMovesToSeat = function(seats, students) {
    
};
```

### TypeScript

```typescript
function minMovesToSeat(seats: number[], students: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $seats
     * @param Integer[] $students
     * @return Integer
     */
    function minMovesToSeat($seats, $students) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minMovesToSeat(_ seats: [Int], _ students: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minMovesToSeat(seats: IntArray, students: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minMovesToSeat(List<int> seats, List<int> students) {
    
  }
}
```

### Go

```golang
func minMovesToSeat(seats []int, students []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} seats
# @param {Integer[]} students
# @return {Integer}
def min_moves_to_seat(seats, students)
    
end
```

### Scala

```scala
object Solution {
    def minMovesToSeat(seats: Array[Int], students: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_moves_to_seat(seats: Vec<i32>, students: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-moves-to-seat seats students)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_moves_to_seat(Seats :: [integer()], Students :: [integer()]) -> integer().
min_moves_to_seat(Seats, Students) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_moves_to_seat(seats :: [integer], students :: [integer]) :: integer
  def min_moves_to_seat(seats, students) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minMovesToSeat(seats: Array<Int64>, students: Array<Int64>): Int64 {

    }
}
```

