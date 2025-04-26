# 1850. 邻位交换的最小次数

## 题目描述

<p>给你一个表示大整数的字符串 <code>num</code> ，和一个整数 <code>k</code> 。</p>

<p>如果某个整数是 <code>num</code> 中各位数字的一个 <strong>排列</strong> 且它的 <strong>值大于</strong> <code>num</code> ，则称这个整数为 <strong>妙数</strong> 。可能存在很多妙数，但是只需要关注 <strong>值最小</strong> 的那些。</p>

<ul>
	<li>例如，<code>num = "5489355142"</code> ：

	<ul>
		<li>第 1 个最小妙数是 <code>"5489355214"</code></li>
		<li>第 2 个最小妙数是 <code>"5489355241"</code></li>
		<li>第 3 个最小妙数是 <code>"5489355412"</code></li>
		<li>第 4 个最小妙数是 <code>"5489355421"</code></li>
	</ul>
	</li>
</ul>

<p>返回要得到第 <code>k</code> 个 <strong>最小妙数</strong> 需要对 <code>num</code> 执行的 <strong>相邻位数字交换的最小次数</strong> 。</p>

<p>测试用例是按存在第 <code>k</code> 个最小妙数而生成的。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>num = "5489355142", k = 4
<strong>输出：</strong>2
<strong>解释：</strong>第 4 个最小妙数是 "5489355421" ，要想得到这个数字：
- 交换下标 7 和下标 8 对应的位："5489355<strong>14</strong>2" -&gt; "5489355<strong>41</strong>2"
- 交换下标 8 和下标 9 对应的位："54893554<strong>12</strong>" -&gt; "54893554<strong>21</strong>"
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>num = "11112", k = 4
<strong>输出：</strong>4
<strong>解释：</strong>第 4 个最小妙数是 "21111" ，要想得到这个数字：
- 交换下标 3 和下标 4 对应的位："111<strong>12</strong>" -&gt; "111<strong>21</strong>"
- 交换下标 2 和下标 3 对应的位："11<strong>12</strong>1" -&gt; "11<strong>21</strong>1"
- 交换下标 1 和下标 2 对应的位："1<strong>12</strong>11" -&gt; "1<strong>21</strong>11"
- 交换下标 0 和下标 1 对应的位："<strong>12</strong>111" -&gt; "<strong>21</strong>111"
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>num = "00123", k = 1
<strong>输出：</strong>1
<strong>解释：</strong>第 1 个最小妙数是 "00132" ，要想得到这个数字：
- 交换下标 3 和下标 4 对应的位："001<strong>23</strong>" -&gt; "001<strong>32</strong>"
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= num.length &lt;= 1000</code></li>
	<li><code>1 &lt;= k &lt;= 1000</code></li>
	<li><code>num</code> 仅由数字组成</li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 双指针
- 字符串

## 提示

1. Find the next permutation of the given string k times.
2. Try to move each element to its correct position and calculate the number of steps.

## 示例

```
"5489355142"
4
"11112"
4
"00123"
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int getMinSwaps(string num, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int getMinSwaps(String num, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def getMinSwaps(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        
```

### C

```c
int getMinSwaps(char* num, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int GetMinSwaps(string num, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} num
 * @param {number} k
 * @return {number}
 */
var getMinSwaps = function(num, k) {
    
};
```

### TypeScript

```typescript
function getMinSwaps(num: string, k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $num
     * @param Integer $k
     * @return Integer
     */
    function getMinSwaps($num, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func getMinSwaps(_ num: String, _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun getMinSwaps(num: String, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int getMinSwaps(String num, int k) {
    
  }
}
```

### Go

```golang
func getMinSwaps(num string, k int) int {
    
}
```

### Ruby

```ruby
# @param {String} num
# @param {Integer} k
# @return {Integer}
def get_min_swaps(num, k)
    
end
```

### Scala

```scala
object Solution {
    def getMinSwaps(num: String, k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn get_min_swaps(num: String, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (get-min-swaps num k)
  (-> string? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec get_min_swaps(Num :: unicode:unicode_binary(), K :: integer()) -> integer().
get_min_swaps(Num, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec get_min_swaps(num :: String.t, k :: integer) :: integer
  def get_min_swaps(num, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func getMinSwaps(num: String, k: Int64): Int64 {

    }
}
```

