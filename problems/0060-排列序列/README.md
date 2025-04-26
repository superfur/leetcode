# 60. 排列序列

## 题目描述

<p>给出集合 <code>[1,2,3,...,n]</code>，其所有元素共有 <code>n!</code> 种排列。</p>

<p>按大小顺序列出所有排列情况，并一一标记，当 <code>n = 3</code> 时, 所有排列如下：</p>

<ol>
	<li><code>"123"</code></li>
	<li><code>"132"</code></li>
	<li><code>"213"</code></li>
	<li><code>"231"</code></li>
	<li><code>"312"</code></li>
	<li><code>"321"</code></li>
</ol>

<p>给定 <code>n</code> 和 <code>k</code>，返回第 <code>k</code> 个排列。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 3, k = 3
<strong>输出：</strong>"213"
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 4, k = 9
<strong>输出：</strong>"2314"
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 3, k = 1
<strong>输出：</strong>"123"
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= n <= 9</code></li>
	<li><code>1 <= k <= n!</code></li>
</ul>


## 难度

Hard

## 标签

- 递归
- 数学

## 示例

```
3
3
4
9
3
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string getPermutation(int n, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public String getPermutation(int n, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
```

### C

```c
char* getPermutation(int n, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public string GetPermutation(int n, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} k
 * @return {string}
 */
var getPermutation = function(n, k) {
    
};
```

### TypeScript

```typescript
function getPermutation(n: number, k: number): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $k
     * @return String
     */
    function getPermutation($n, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func getPermutation(_ n: Int, _ k: Int) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun getPermutation(n: Int, k: Int): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String getPermutation(int n, int k) {
    
  }
}
```

### Go

```golang
func getPermutation(n int, k int) string {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} k
# @return {String}
def get_permutation(n, k)
    
end
```

### Scala

```scala
object Solution {
    def getPermutation(n: Int, k: Int): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn get_permutation(n: i32, k: i32) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (get-permutation n k)
  (-> exact-integer? exact-integer? string?)
  )
```

### Erlang

```erlang
-spec get_permutation(N :: integer(), K :: integer()) -> unicode:unicode_binary().
get_permutation(N, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec get_permutation(n :: integer, k :: integer) :: String.t
  def get_permutation(n, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func getPermutation(n: Int64, k: Int64): String {

    }
}
```

