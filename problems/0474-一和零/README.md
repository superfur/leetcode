# 474. 一和零

## 题目描述

<p>给你一个二进制字符串数组 <code>strs</code> 和两个整数 <code>m</code> 和 <code>n</code> 。</p>

<div class="MachineTrans-Lines">
<p class="MachineTrans-lang-zh-CN">请你找出并返回 <code>strs</code> 的最大子集的长度，该子集中 <strong>最多</strong> 有 <code>m</code> 个 <code>0</code> 和 <code>n</code> 个 <code>1</code> 。</p>

<p class="MachineTrans-lang-zh-CN">如果 <code>x</code> 的所有元素也是 <code>y</code> 的元素，集合 <code>x</code> 是集合 <code>y</code> 的 <strong>子集</strong> 。</p>
</div>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3
<strong>输出：</strong>4
<strong>解释：</strong>最多有 5 个 0 和 3 个 1 的最大子集是 {"10","0001","1","0"} ，因此答案是 4 。
其他满足题意但较小的子集包括 {"0001","1"} 和 {"10","1","0"} 。{"111001"} 不满足题意，因为它含 4 个 1 ，大于 n 的值 3 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>strs = ["10", "0", "1"], m = 1, n = 1
<strong>输出：</strong>2
<strong>解释：</strong>最大的子集是 {"0", "1"} ，所以答案是 2 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= strs.length &lt;= 600</code></li>
	<li><code>1 &lt;= strs[i].length &lt;= 100</code></li>
	<li><code>strs[i]</code>&nbsp;仅由&nbsp;<code>'0'</code> 和&nbsp;<code>'1'</code> 组成</li>
	<li><code>1 &lt;= m, n &lt;= 100</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 字符串
- 动态规划

## 示例

```
["10","0001","111001","1","0"]
5
3
["10","0","1"]
1
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int findMaxForm(String[] strs, int m, int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
```

### C

```c
int findMaxForm(char** strs, int strsSize, int m, int n) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindMaxForm(string[] strs, int m, int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} strs
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var findMaxForm = function(strs, m, n) {
    
};
```

### TypeScript

```typescript
function findMaxForm(strs: string[], m: number, n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $strs
     * @param Integer $m
     * @param Integer $n
     * @return Integer
     */
    function findMaxForm($strs, $m, $n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findMaxForm(_ strs: [String], _ m: Int, _ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findMaxForm(strs: Array<String>, m: Int, n: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findMaxForm(List<String> strs, int m, int n) {
    
  }
}
```

### Go

```golang
func findMaxForm(strs []string, m int, n int) int {
    
}
```

### Ruby

```ruby
# @param {String[]} strs
# @param {Integer} m
# @param {Integer} n
# @return {Integer}
def find_max_form(strs, m, n)
    
end
```

### Scala

```scala
object Solution {
    def findMaxForm(strs: Array[String], m: Int, n: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_max_form(strs: Vec<String>, m: i32, n: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-max-form strs m n)
  (-> (listof string?) exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec find_max_form(Strs :: [unicode:unicode_binary()], M :: integer(), N :: integer()) -> integer().
find_max_form(Strs, M, N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_max_form(strs :: [String.t], m :: integer, n :: integer) :: integer
  def find_max_form(strs, m, n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findMaxForm(strs: Array<String>, m: Int64, n: Int64): Int64 {

    }
}
```

