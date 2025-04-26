# 面试题 16.10. 生存人数

## 题目描述

<p>给定 N 个人的出生年份和死亡年份，第 <code>i</code> 个人的出生年份为 <code>birth[i]</code>，死亡年份为 <code>death[i]</code>，实现一个方法以计算生存人数最多的年份。</p>

<p>你可以假设所有人都出生于 1900 年至 2000 年（含 1900 和 2000 ）之间。如果一个人在某一年的任意时期处于生存状态，那么他应该被纳入那一年的统计中。例如，生于 1908 年、死于 1909 年的人应当被列入 1908 年和 1909 年的计数。</p>

<p>如果有多个年份生存人数相同且均为最大值，输出其中最小的年份。</p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong>
birth = [1900, 1901, 1950]
death = [1948, 1951, 2000]
<strong>输出：</strong> 1901
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt; birth.length == death.length &lt;= 10000</code></li>
	<li><code>birth[i] &lt;= death[i]</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 计数

## 提示

1. 方案 1：你能计算出每年有多少人活着吗？
2. 方案1：用散列表或数组试试，将出生年份映射到该年还有多少人活着。
3. 解法2：如果对年份排序会如何？你会根据什么排序？
4. 解法2：你真的有必要匹配出生年份和死亡年份吗？当一个特定的人死了，会有什么关系，或者你只是需要一份死亡年份的清单？
5. 解法2：观察到人是“可替代的”，不管谁出生，何时死亡。你需要的只是一份出生年份和死亡年份的列表。这可能会使你对人员列表的排序变得更加容易。
6. 解法2：尝试创建一份排序的出生列表和一份排序的死亡列表。通过遍历两个列表，你能追踪任意时间活着的人的数量吗？
7. 每个出生增加一个人，每个死亡移除一个人。尝试编写一份人员列表（出生年份和死亡年份）示例，然后将其重新格式化为每年的列表，出生时加1，死亡时减1。
8. 解法3：如果你创建了一个年份数组并保存每个年份的人口变化会如何？你能找到人口最多的那一年吗?
9. 解法3：注意这个问题中的细节。你的算法/代码是否考虑一个在出生的同一年去世的人？这个人应该被计算为人口总数中的一人。

## 示例

```
[1900,1901,1950]
[1948,1951,2000]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxAliveYear(vector<int>& birth, vector<int>& death) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxAliveYear(int[] birth, int[] death) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxAliveYear(self, birth, death):
        """
        :type birth: List[int]
        :type death: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxAliveYear(self, birth: List[int], death: List[int]) -> int:
        
```

### C

```c
int maxAliveYear(int* birth, int birthSize, int* death, int deathSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxAliveYear(int[] birth, int[] death) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} birth
 * @param {number[]} death
 * @return {number}
 */
var maxAliveYear = function(birth, death) {
    
};
```

### TypeScript

```typescript
function maxAliveYear(birth: number[], death: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $birth
     * @param Integer[] $death
     * @return Integer
     */
    function maxAliveYear($birth, $death) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxAliveYear(_ birth: [Int], _ death: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxAliveYear(birth: IntArray, death: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxAliveYear(List<int> birth, List<int> death) {
    
  }
}
```

### Go

```golang
func maxAliveYear(birth []int, death []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} birth
# @param {Integer[]} death
# @return {Integer}
def max_alive_year(birth, death)
    
end
```

### Scala

```scala
object Solution {
    def maxAliveYear(birth: Array[Int], death: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_alive_year(birth: Vec<i32>, death: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-alive-year birth death)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_alive_year(Birth :: [integer()], Death :: [integer()]) -> integer().
max_alive_year(Birth, Death) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_alive_year(birth :: [integer], death :: [integer]) :: integer
  def max_alive_year(birth, death) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxAliveYear(birth: Array<Int64>, death: Array<Int64>): Int64 {

    }
}
```

