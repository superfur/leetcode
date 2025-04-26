# 1441. 用栈操作构建数组

## 题目描述

<p>给你一个数组 <code>target</code> 和一个整数 <code>n</code>。每次迭代，需要从&nbsp; <code>list = { 1 , 2 , 3 ..., n }</code> 中依次读取一个数字。</p>

<p>请使用下述操作来构建目标数组 <code>target</code> ：</p>

<ul>
	<li><code>"Push"</code>：从 <code>list</code> 中读取一个新元素， 并将其推入数组中。</li>
	<li><code>"Pop"</code>：删除数组中的最后一个元素。</li>
	<li>如果目标数组构建完成，就停止读取更多元素。</li>
</ul>

<p>题目数据保证目标数组严格递增，并且只包含 <code>1</code> 到 <code>n</code> 之间的数字。</p>

<p>请返回构建目标数组所用的操作序列。如果存在多个可行方案，返回任一即可。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>target = [1,3], n = 3
<strong>输出：</strong>["Push","Push","Pop","Push"]
<strong>解释： 
</strong>读取 1 并自动推入数组 -&gt; [1]
读取 2 并自动推入数组，然后删除它 -&gt; [1]
读取 3 并自动推入数组 -&gt; [1,3]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>target = [1,2,3], n = 3
<strong>输出：</strong>["Push","Push","Push"]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>target = [1,2], n = 4
<strong>输出：</strong>["Push","Push"]
<strong>解释：</strong>只需要读取前 2 个数字就可以停止。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= target.length &lt;= 100</code></li>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>1 &lt;= target[i] &lt;= n</code></li>
	<li><code>target</code> 严格递增</li>
</ul>


## 难度

Medium

## 标签

- 栈
- 数组
- 模拟

## 提示

1. Use “Push” for numbers to be kept in target array and [“Push”, “Pop”] for numbers to be discarded.

## 示例

```
[1,3]
3
[1,2,3]
3
[1,2]
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<string> buildArray(vector<int>& target, int n) {
        
    }
};
```

### Java

```java
class Solution {
    public List<String> buildArray(int[] target, int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        
```

### Python3

```python3
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** buildArray(int* target, int targetSize, int n, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<string> BuildArray(int[] target, int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} target
 * @param {number} n
 * @return {string[]}
 */
var buildArray = function(target, n) {
    
};
```

### TypeScript

```typescript
function buildArray(target: number[], n: number): string[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $target
     * @param Integer $n
     * @return String[]
     */
    function buildArray($target, $n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func buildArray(_ target: [Int], _ n: Int) -> [String] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun buildArray(target: IntArray, n: Int): List<String> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<String> buildArray(List<int> target, int n) {
    
  }
}
```

### Go

```golang
func buildArray(target []int, n int) []string {
    
}
```

### Ruby

```ruby
# @param {Integer[]} target
# @param {Integer} n
# @return {String[]}
def build_array(target, n)
    
end
```

### Scala

```scala
object Solution {
    def buildArray(target: Array[Int], n: Int): List[String] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn build_array(target: Vec<i32>, n: i32) -> Vec<String> {
        
    }
}
```

### Racket

```racket
(define/contract (build-array target n)
  (-> (listof exact-integer?) exact-integer? (listof string?))
  )
```

### Erlang

```erlang
-spec build_array(Target :: [integer()], N :: integer()) -> [unicode:unicode_binary()].
build_array(Target, N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec build_array(target :: [integer], n :: integer) :: [String.t]
  def build_array(target, n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func buildArray(target: Array<Int64>, n: Int64): ArrayList<String> {

    }
}
```

