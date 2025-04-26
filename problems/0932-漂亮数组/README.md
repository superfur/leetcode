# 932. 漂亮数组

## 题目描述

<p>如果长度为 <code>n</code> 的数组 <code>nums</code> 满足下述条件，则认为该数组是一个 <strong>漂亮数组</strong> ：</p>

<ul>
	<li><code>nums</code> 是由范围 <code>[1, n]</code> 的整数组成的一个排列。</li>
	<li>对于每个 <code>0 &lt;= i &lt; j &lt; n</code> ，均不存在下标 <code>k</code>（<code>i &lt; k &lt; j</code>）使得 <code>2 * nums[k] == nums[i] + nums[j]</code> 。</li>
</ul>

<p>给你整数 <code>n</code> ，返回长度为 <code>n</code> 的任一 <strong>漂亮数组</strong> 。本题保证对于给定的 <code>n</code> 至少存在一个有效答案。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1 ：</strong></p>

<pre>
<strong>输入：</strong>n = 4
<strong>输出：</strong>[2,1,4,3]
</pre>

<p><strong class="example">示例 2 ：</strong></p>

<pre>
<strong>输入：</strong>n = 5
<strong>输出：</strong>[3,1,2,5,4]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
</ul>

<p>&nbsp;</p>


## 难度

Medium

## 标签

- 数组
- 数学
- 分治

## 示例

```
4
5
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> beautifulArray(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] beautifulArray(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def beautifulArray(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* beautifulArray(int n, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] BeautifulArray(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number[]}
 */
var beautifulArray = function(n) {
    
};
```

### TypeScript

```typescript
function beautifulArray(n: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer[]
     */
    function beautifulArray($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func beautifulArray(_ n: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun beautifulArray(n: Int): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> beautifulArray(int n) {
    
  }
}
```

### Go

```golang
func beautifulArray(n int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer[]}
def beautiful_array(n)
    
end
```

### Scala

```scala
object Solution {
    def beautifulArray(n: Int): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn beautiful_array(n: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (beautiful-array n)
  (-> exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec beautiful_array(N :: integer()) -> [integer()].
beautiful_array(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec beautiful_array(n :: integer) :: [integer]
  def beautiful_array(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func beautifulArray(n: Int64): Array<Int64> {

    }
}
```

