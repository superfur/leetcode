# 2491. 划分技能点相等的团队

## 题目描述

<p>给你一个正整数数组 <code>skill</code> ，数组长度为 <strong>偶数</strong> <code>n</code> ，其中 <code>skill[i]</code> 表示第 <code>i</code> 个玩家的技能点。将所有玩家分成 <code>n / 2</code> 个 <code>2</code> 人团队，使每一个团队的技能点之和 <strong>相等</strong> 。</p>

<p>团队的 <strong>化学反应</strong> 等于团队中玩家的技能点 <strong>乘积</strong> 。</p>

<p>返回所有团队的 <strong>化学反应</strong> 之和，如果无法使每个团队的技能点之和相等，则返回 <code>-1</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>skill = [3,2,5,1,3,4]
<strong>输出：</strong>22
<strong>解释：</strong>
将玩家分成 3 个团队 (1, 5), (2, 4), (3, 3) ，每个团队的技能点之和都是 6 。
所有团队的化学反应之和是 1 * 5 + 2 * 4 + 3 * 3 = 5 + 8 + 9 = 22 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>skill = [3,4]
<strong>输出：</strong>12
<strong>解释：</strong>
两个玩家形成一个团队，技能点之和是 7 。
团队的化学反应是 3 * 4 = 12 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>skill = [1,1,2,3]
<strong>输出：</strong>-1
<strong>解释：</strong>
无法将玩家分成每个团队技能点都相等的若干个 2 人团队。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= skill.length &lt;= 10<sup>5</sup></code></li>
	<li><code>skill.length</code> 是偶数</li>
	<li><code>1 &lt;= skill[i] &lt;= 1000</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 双指针
- 排序

## 提示

1. Try sorting the skill array.
2. It is always optimal to pair the weakest available player with the strongest available player.

## 示例

```
[3,2,5,1,3,4]
[3,4]
[1,1,2,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long dividePlayers(vector<int>& skill) {
        
    }
};
```

### Java

```java
class Solution {
    public long dividePlayers(int[] skill) {
        
    }
}
```

### Python

```python
class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
```

### C

```c
long long dividePlayers(int* skill, int skillSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long DividePlayers(int[] skill) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} skill
 * @return {number}
 */
var dividePlayers = function(skill) {
    
};
```

### TypeScript

```typescript
function dividePlayers(skill: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $skill
     * @return Integer
     */
    function dividePlayers($skill) {
        
    }
}
```

### Swift

```swift
class Solution {
    func dividePlayers(_ skill: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun dividePlayers(skill: IntArray): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int dividePlayers(List<int> skill) {
    
  }
}
```

### Go

```golang
func dividePlayers(skill []int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} skill
# @return {Integer}
def divide_players(skill)
    
end
```

### Scala

```scala
object Solution {
    def dividePlayers(skill: Array[Int]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn divide_players(skill: Vec<i32>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (divide-players skill)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec divide_players(Skill :: [integer()]) -> integer().
divide_players(Skill) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec divide_players(skill :: [integer]) :: integer
  def divide_players(skill) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func dividePlayers(skill: Array<Int64>): Int64 {

    }
}
```

