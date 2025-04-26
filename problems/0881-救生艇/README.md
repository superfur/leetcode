# 881. 救生艇

## 题目描述

<p>给定数组<meta charset="UTF-8" />&nbsp;<code>people</code>&nbsp;。<code>people[i]</code>表示第 <code>i</code><sup>&nbsp;</sup>个人的体重&nbsp;，<strong>船的数量不限</strong>，每艘船可以承载的最大重量为&nbsp;<code>limit</code>。</p>

<p>每艘船最多可同时载两人，但条件是这些人的重量之和最多为&nbsp;<code>limit</code>。</p>

<p>返回 <em>承载所有人所需的最小船数</em>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>people = [1,2], limit = 3
<strong>输出：</strong>1
<strong>解释：</strong>1 艘船载 (1, 2)
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>people = [3,2,2,1], limit = 3
<strong>输出：</strong>3
<strong>解释：</strong>3 艘船分别载 (1, 2), (2) 和 (3)
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>people = [3,5,3,4], limit = 5
<strong>输出：</strong>4
<strong>解释：</strong>4 艘船分别载 (3), (3), (4), (5)</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= people.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= people[i] &lt;= limit &lt;= 3 * 10<sup>4</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 双指针
- 排序

## 示例

```
[1,2]
3
[3,2,2,1]
3
[3,5,3,4]
5
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        
    }
};
```

### Java

```java
class Solution {
    public int numRescueBoats(int[] people, int limit) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
```

### C

```c
int numRescueBoats(int* people, int peopleSize, int limit) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumRescueBoats(int[] people, int limit) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} people
 * @param {number} limit
 * @return {number}
 */
var numRescueBoats = function(people, limit) {
    
};
```

### TypeScript

```typescript
function numRescueBoats(people: number[], limit: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $people
     * @param Integer $limit
     * @return Integer
     */
    function numRescueBoats($people, $limit) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numRescueBoats(_ people: [Int], _ limit: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numRescueBoats(people: IntArray, limit: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numRescueBoats(List<int> people, int limit) {
    
  }
}
```

### Go

```golang
func numRescueBoats(people []int, limit int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} people
# @param {Integer} limit
# @return {Integer}
def num_rescue_boats(people, limit)
    
end
```

### Scala

```scala
object Solution {
    def numRescueBoats(people: Array[Int], limit: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn num_rescue_boats(people: Vec<i32>, limit: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (num-rescue-boats people limit)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec num_rescue_boats(People :: [integer()], Limit :: integer()) -> integer().
num_rescue_boats(People, Limit) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec num_rescue_boats(people :: [integer], limit :: integer) :: integer
  def num_rescue_boats(people, limit) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numRescueBoats(people: Array<Int64>, limit: Int64): Int64 {

    }
}
```

