# 3006. 找出数组中的美丽下标 I

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的字符串 <code>s</code> 、字符串 <code>a</code> 、字符串 <code>b</code> 和一个整数 <code>k</code> 。</p>

<p>如果下标 <code>i</code> 满足以下条件，则认为它是一个 <strong>美丽下标</strong>：</p>

<ul>
	<li><code>0 &lt;= i &lt;= s.length - a.length</code></li>
	<li><code>s[i..(i + a.length - 1)] == a</code></li>
	<li>存在下标 <code>j</code> 使得：
	<ul>
		<li><code>0 &lt;= j &lt;= s.length - b.length</code></li>
		<li><code>s[j..(j + b.length - 1)] == b</code></li>
		<li><code>|j - i| &lt;= k</code></li>
	</ul>
	</li>
</ul>

<p>以数组形式按<strong> 从小到大排序 </strong>返回美丽下标。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "isawsquirrelnearmysquirrelhouseohmy", a = "my", b = "squirrel", k = 15
<strong>输出：</strong>[16,33]
<strong>解释：</strong>存在 2 个美丽下标：[16,33]。
- 下标 16 是美丽下标，因为 s[16..17] == "my" ，且存在下标 4 ，满足 s[4..11] == "squirrel" 且 |16 - 4| &lt;= 15 。
- 下标 33 是美丽下标，因为 s[33..34] == "my" ，且存在下标 18 ，满足 s[18..25] == "squirrel" 且 |33 - 18| &lt;= 15 。
因此返回 [16,33] 作为结果。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "abcd", a = "a", b = "a", k = 4
<strong>输出：</strong>[0]
<strong>解释：</strong>存在 1 个美丽下标：[0]。
- 下标 0 是美丽下标，因为 s[0..0] == "a" ，且存在下标 0 ，满足 s[0..0] == "a" 且 |0 - 0| &lt;= 4 。
因此返回 [0] 作为结果。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= a.length, b.length &lt;= 10</code></li>
	<li><code>s</code>、<code>a</code>、和 <code>b</code> 只包含小写英文字母。</li>
</ul>


## 难度

Medium

## 标签

- 双指针
- 字符串
- 二分查找
- 字符串匹配
- 哈希函数
- 滚动哈希

## 提示

1. For each <code>i</code>, you can iterate over all <code>j</code>s and determine if <code>i</code> is beautiful or not.

## 示例

```
"isawsquirrelnearmysquirrelhouseohmy"
"my"
"squirrel"
15
"abcd"
"a"
"a"
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> beautifulIndices(string s, string a, string b, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Integer> beautifulIndices(String s, String a, String b, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def beautifulIndices(self, s, a, b, k):
        """
        :type s: str
        :type a: str
        :type b: str
        :type k: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* beautifulIndices(char* s, char* a, char* b, int k, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<int> BeautifulIndices(string s, string a, string b, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {string} a
 * @param {string} b
 * @param {number} k
 * @return {number[]}
 */
var beautifulIndices = function(s, a, b, k) {
    
};
```

### TypeScript

```typescript
function beautifulIndices(s: string, a: string, b: string, k: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param String $a
     * @param String $b
     * @param Integer $k
     * @return Integer[]
     */
    function beautifulIndices($s, $a, $b, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func beautifulIndices(_ s: String, _ a: String, _ b: String, _ k: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun beautifulIndices(s: String, a: String, b: String, k: Int): List<Int> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> beautifulIndices(String s, String a, String b, int k) {
    
  }
}
```

### Go

```golang
func beautifulIndices(s string, a string, b string, k int) []int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {String} a
# @param {String} b
# @param {Integer} k
# @return {Integer[]}
def beautiful_indices(s, a, b, k)
    
end
```

### Scala

```scala
object Solution {
    def beautifulIndices(s: String, a: String, b: String, k: Int): List[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn beautiful_indices(s: String, a: String, b: String, k: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (beautiful-indices s a b k)
  (-> string? string? string? exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec beautiful_indices(S :: unicode:unicode_binary(), A :: unicode:unicode_binary(), B :: unicode:unicode_binary(), K :: integer()) -> [integer()].
beautiful_indices(S, A, B, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec beautiful_indices(s :: String.t, a :: String.t, b :: String.t, k :: integer) :: [integer]
  def beautiful_indices(s, a, b, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func beautifulIndices(s: String, a: String, b: String, k: Int64): ArrayList<Int64> {

    }
}
```

