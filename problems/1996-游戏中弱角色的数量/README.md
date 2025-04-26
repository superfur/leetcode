# 1996. 游戏中弱角色的数量

## 题目描述

<p>你正在参加一个多角色游戏，每个角色都有两个主要属性：<strong>攻击</strong> 和 <strong>防御</strong> 。给你一个二维整数数组 <code>properties</code> ，其中 <code>properties[i] = [attack<sub>i</sub>, defense<sub>i</sub>]</code> 表示游戏中第 <code>i</code> 个角色的属性。</p>

<p>如果存在一个其他角色的攻击和防御等级 <strong>都严格高于</strong> 该角色的攻击和防御等级，则认为该角色为 <strong>弱角色</strong> 。更正式地，如果认为角色 <code>i</code> <strong>弱于</strong> 存在的另一个角色 <code>j</code> ，那么 <code>attack<sub>j</sub> &gt; attack<sub>i</sub></code> 且 <code>defense<sub>j</sub> &gt; defense<sub>i</sub></code> 。</p>

<p>返回 <strong>弱角色</strong> 的数量。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>properties = [[5,5],[6,3],[3,6]]
<strong>输出：</strong>0
<strong>解释：</strong>不存在攻击和防御都严格高于其他角色的角色。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>properties = [[2,2],[3,3]]
<strong>输出：</strong>1
<strong>解释：</strong>第一个角色是弱角色，因为第二个角色的攻击和防御严格大于该角色。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>properties = [[1,5],[10,4],[4,3]]
<strong>输出：</strong>1
<strong>解释：</strong>第三个角色是弱角色，因为第二个角色的攻击和防御严格大于该角色。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= properties.length &lt;= 10<sup>5</sup></code></li>
	<li><code>properties[i].length == 2</code></li>
	<li><code>1 &lt;= attack<sub>i</sub>, defense<sub>i</sub> &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 栈
- 贪心
- 数组
- 排序
- 单调栈

## 提示

1. Sort the array on the basis of the attack values and group characters with the same attack together. How can you use these groups?
2. Characters in one group will always have a lesser attack value than the characters of the next group. Hence, we will only need to check if there is a higher defense value present in the next groups.

## 示例

```
[[5,5],[6,3],[3,6]]
[[2,2],[3,3]]
[[1,5],[10,4],[4,3]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numberOfWeakCharacters(vector<vector<int>>& properties) {
        
    }
};
```

### Java

```java
class Solution {
    public int numberOfWeakCharacters(int[][] properties) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numberOfWeakCharacters(self, properties):
        """
        :type properties: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        
```

### C

```c
int numberOfWeakCharacters(int** properties, int propertiesSize, int* propertiesColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumberOfWeakCharacters(int[][] properties) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} properties
 * @return {number}
 */
var numberOfWeakCharacters = function(properties) {
    
};
```

### TypeScript

```typescript
function numberOfWeakCharacters(properties: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $properties
     * @return Integer
     */
    function numberOfWeakCharacters($properties) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numberOfWeakCharacters(_ properties: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numberOfWeakCharacters(properties: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numberOfWeakCharacters(List<List<int>> properties) {
    
  }
}
```

### Go

```golang
func numberOfWeakCharacters(properties [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} properties
# @return {Integer}
def number_of_weak_characters(properties)
    
end
```

### Scala

```scala
object Solution {
    def numberOfWeakCharacters(properties: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn number_of_weak_characters(properties: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (number-of-weak-characters properties)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec number_of_weak_characters(Properties :: [[integer()]]) -> integer().
number_of_weak_characters(Properties) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec number_of_weak_characters(properties :: [[integer]]) :: integer
  def number_of_weak_characters(properties) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numberOfWeakCharacters(properties: Array<Array<Int64>>): Int64 {

    }
}
```

