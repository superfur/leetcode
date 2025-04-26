# 2399. 检查相同字母间的距离

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的字符串 <code>s</code> ，该字符串仅由小写英文字母组成，<code>s</code> 中的每个字母都 <strong>恰好</strong> 出现 <strong>两次</strong> 。另给你一个下标从 <strong>0</strong> 开始、长度为 <code>26</code> 的的整数数组 <code>distance</code> 。</p>

<p>字母表中的每个字母按从 <code>0</code> 到 <code>25</code> 依次编号（即，<code>'a' -&gt; 0</code>, <code>'b' -&gt; 1</code>, <code>'c' -&gt; 2</code>, ... , <code>'z' -&gt; 25</code>）。</p>

<p>在一个 <strong>匀整</strong> 字符串中，第 <code>i</code> 个字母的两次出现之间的字母数量是 <code>distance[i]</code> 。如果第 <code>i</code> 个字母没有在 <code>s</code> 中出现，那么 <code>distance[i]</code> 可以 <strong>忽略</strong> 。</p>

<p>如果 <code>s</code> 是一个 <strong>匀整</strong> 字符串，返回 <code>true</code> ；否则，返回 <code>false</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>s = "abaccb", distance = [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
<strong>输出：</strong>true
<strong>解释：</strong>
- 'a' 在下标 0 和下标 2 处出现，所以满足 distance[0] = 1 。
- 'b' 在下标 1 和下标 5 处出现，所以满足 distance[1] = 3 。
- 'c' 在下标 3 和下标 4 处出现，所以满足 distance[2] = 0 。
注意 distance[3] = 5 ，但是由于 'd' 没有在 s 中出现，可以忽略。
因为 s 是一个匀整字符串，返回 true 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>s = "aa", distance = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
<strong>输出：</strong>false
<strong>解释：</strong>
- 'a' 在下标 0 和 1 处出现，所以两次出现之间的字母数量为 0 。
但是 distance[0] = 1 ，s 不是一个匀整字符串。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= s.length &lt;= 52</code></li>
	<li><code>s</code> 仅由小写英文字母组成</li>
	<li><code>s</code> 中的每个字母恰好出现两次</li>
	<li><code>distance.length == 26</code></li>
	<li><code>0 &lt;= distance[i] &lt;= 50</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表
- 字符串

## 提示

1. Create an integer array of size 26 to keep track of the first occurrence of each letter.
2. The number of letters between indices i and j is j - i - 1.

## 示例

```
"abaccb"
[1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
"aa"
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool checkDistances(string s, vector<int>& distance) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean checkDistances(String s, int[] distance) {
        
    }
}
```

### Python

```python
class Solution(object):
    def checkDistances(self, s, distance):
        """
        :type s: str
        :type distance: List[int]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        
```

### C

```c
bool checkDistances(char* s, int* distance, int distanceSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CheckDistances(string s, int[] distance) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {number[]} distance
 * @return {boolean}
 */
var checkDistances = function(s, distance) {
    
};
```

### TypeScript

```typescript
function checkDistances(s: string, distance: number[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param Integer[] $distance
     * @return Boolean
     */
    function checkDistances($s, $distance) {
        
    }
}
```

### Swift

```swift
class Solution {
    func checkDistances(_ s: String, _ distance: [Int]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun checkDistances(s: String, distance: IntArray): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool checkDistances(String s, List<int> distance) {
    
  }
}
```

### Go

```golang
func checkDistances(s string, distance []int) bool {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer[]} distance
# @return {Boolean}
def check_distances(s, distance)
    
end
```

### Scala

```scala
object Solution {
    def checkDistances(s: String, distance: Array[Int]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn check_distances(s: String, distance: Vec<i32>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (check-distances s distance)
  (-> string? (listof exact-integer?) boolean?)
  )
```

### Erlang

```erlang
-spec check_distances(S :: unicode:unicode_binary(), Distance :: [integer()]) -> boolean().
check_distances(S, Distance) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec check_distances(s :: String.t, distance :: [integer]) :: boolean
  def check_distances(s, distance) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func checkDistances(s: String, distance: Array<Int64>): Bool {

    }
}
```

