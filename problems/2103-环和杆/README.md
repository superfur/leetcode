# 2103. 环和杆

## 题目描述

<p>总计有 <code>n</code> 个环，环的颜色可以是红、绿、蓝中的一种。这些环分别穿在 10 根编号为 <code>0</code> 到 <code>9</code> 的杆上。</p>

<p>给你一个长度为 <code>2n</code> 的字符串 <code>rings</code> ，表示这 <code>n</code> 个环在杆上的分布。<code>rings</code> 中每两个字符形成一个 <strong>颜色位置对</strong> ，用于描述每个环：</p>

<ul>
	<li>第 <code>i</code> 对中的 <strong>第一个</strong> 字符表示第 <code>i</code> 个环的 <strong>颜色</strong>（<code>'R'</code>、<code>'G'</code>、<code>'B'</code>）。</li>
	<li>第 <code>i</code> 对中的 <strong>第二个</strong> 字符表示第 <code>i</code> 个环的 <strong>位置</strong>，也就是位于哪根杆上（<code>'0'</code> 到 <code>'9'</code>）。</li>
</ul>

<p>例如，<code>"R3G2B1"</code> 表示：共有 <code>n == 3</code> 个环，红色的环在编号为 3 的杆上，绿色的环在编号为 2 的杆上，蓝色的环在编号为 1 的杆上。</p>

<p>找出所有集齐 <strong>全部三种颜色</strong> 环的杆，并返回这种杆的数量。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/11/23/ex1final.png" style="width: 258px; height: 130px;" />
<pre>
<strong>输入：</strong>rings = "B0B6G0R6R0R6G9"
<strong>输出：</strong>1
<strong>解释：</strong>
- 编号 0 的杆上有 3 个环，集齐全部颜色：红、绿、蓝。
- 编号 6 的杆上有 3 个环，但只有红、蓝两种颜色。
- 编号 9 的杆上只有 1 个绿色环。
因此，集齐全部三种颜色环的杆的数目为 1 。
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/11/23/ex2final.png" style="width: 266px; height: 130px;" />
<pre>
<strong>输入：</strong>rings = "B0R0G0R9R0B0G0"
<strong>输出：</strong>1
<strong>解释：</strong>
- 编号 0 的杆上有 6 个环，集齐全部颜色：红、绿、蓝。
- 编号 9 的杆上只有 1 个红色环。
因此，集齐全部三种颜色环的杆的数目为 1 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>rings = "G4"
<strong>输出：</strong>0
<strong>解释：</strong>
只给了一个环，因此，不存在集齐全部三种颜色环的杆。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>rings.length == 2 * n</code></li>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li>如 <code>i</code> 是 <strong>偶数</strong> ，则&nbsp;<code>rings[i]</code> 的值可以取 <code>'R'</code>、<code>'G'</code> 或 <code>'B'</code>（下标从 <strong>0</strong> 开始计数）</li>
	<li>如 <code>i</code> 是 <strong>奇数</strong> ，则&nbsp;<code>rings[i]</code> 的值可以取 <code>'0'</code> 到 <code>'9'</code> 中的一个数字（下标从 <strong>0</strong> 开始计数）</li>
</ul>


## 难度

Easy

## 标签

- 哈希表
- 字符串

## 提示

1. For every rod, look through ‘rings’ to see if the rod contains all colors.
2. Create 3 booleans, 1 for each color, to store if that color is present for the current rod. If all 3 are true after looking through the string, then the rod contains all the colors.

## 示例

```
"B0B6G0R6R0R6G9"
"B0R0G0R9R0B0G0"
"G4"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countPoints(string rings) {
        
    }
};
```

### Java

```java
class Solution {
    public int countPoints(String rings) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countPoints(self, rings):
        """
        :type rings: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countPoints(self, rings: str) -> int:
        
```

### C

```c
int countPoints(char* rings) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountPoints(string rings) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} rings
 * @return {number}
 */
var countPoints = function(rings) {
    
};
```

### TypeScript

```typescript
function countPoints(rings: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $rings
     * @return Integer
     */
    function countPoints($rings) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countPoints(_ rings: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countPoints(rings: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countPoints(String rings) {
    
  }
}
```

### Go

```golang
func countPoints(rings string) int {
    
}
```

### Ruby

```ruby
# @param {String} rings
# @return {Integer}
def count_points(rings)
    
end
```

### Scala

```scala
object Solution {
    def countPoints(rings: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_points(rings: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-points rings)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_points(Rings :: unicode:unicode_binary()) -> integer().
count_points(Rings) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_points(rings :: String.t) :: integer
  def count_points(rings) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countPoints(rings: String): Int64 {

    }
}
```

