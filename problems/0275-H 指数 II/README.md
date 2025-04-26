# 275. H 指数 II

## 题目描述

<p>给你一个整数数组 <code>citations</code> ，其中 <code>citations[i]</code> 表示研究者的第 <code>i</code> 篇论文被引用的次数，<code>citations</code> 已经按照&nbsp;<strong>非降序排列&nbsp;</strong>。计算并返回该研究者的 h<strong><em>&nbsp;</em></strong>指数。</p>

<p><a href="https://baike.baidu.com/item/h-index/3991452?fr=aladdin" target="_blank">h 指数的定义</a>：h 代表“高引用次数”（high citations），一名科研人员的 <code>h</code> 指数是指他（她）的 （<code>n</code> 篇论文中）<strong>至少&nbsp;</strong>有 <code>h</code> 篇论文分别被引用了<strong>至少</strong> <code>h</code> 次。</p>

<p>请你设计并实现对数时间复杂度的算法解决此问题。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong><code>citations = [0,1,3,5,6]</code>
<strong>输出：</strong><code>3</code>
<strong>解释：</strong>给定数组表示研究者总共有 <code>5</code> 篇论文，每篇论文相应的被引用了 <code>0, 1, 3, 5, 6</code> 次。
&nbsp;    由于研究者有<code>3</code>篇论文每篇<strong> 至少 </strong>被引用了 <code>3</code> 次，其余两篇论文每篇被引用<strong> 不多于</strong> <code>3</code> 次，所以她的<em> h </em>指数是 <code>3</code> 。</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong><code>citations = [1,2,100]</code>
<strong>输出：</strong><code>2</code>
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == citations.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= citations[i] &lt;= 1000</code></li>
	<li><code>citations</code> 按 <strong>升序排列</strong></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 二分查找

## 提示

1. Expected runtime complexity is in <i>O</i>(log <i>n</i>) and the input is sorted.

## 示例

```
[0,1,3,5,6]
[1,2,100]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int hIndex(vector<int>& citations) {
        
    }
};
```

### Java

```java
class Solution {
    public int hIndex(int[] citations) {
        
    }
}
```

### Python

```python
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
```

### C

```c
int hIndex(int* citations, int citationsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int HIndex(int[] citations) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} citations
 * @return {number}
 */
var hIndex = function(citations) {
    
};
```

### TypeScript

```typescript
function hIndex(citations: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $citations
     * @return Integer
     */
    function hIndex($citations) {
        
    }
}
```

### Swift

```swift
class Solution {
    func hIndex(_ citations: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun hIndex(citations: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int hIndex(List<int> citations) {
    
  }
}
```

### Go

```golang
func hIndex(citations []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} citations
# @return {Integer}
def h_index(citations)
    
end
```

### Scala

```scala
object Solution {
    def hIndex(citations: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn h_index(citations: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (h-index citations)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec h_index(Citations :: [integer()]) -> integer().
h_index(Citations) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec h_index(citations :: [integer]) :: integer
  def h_index(citations) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func hIndex(citations: Array<Int64>): Int64 {

    }
}
```

