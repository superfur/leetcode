# 2511. 最多可以摧毁的敌人城堡数目

## 题目描述

<p>给你一个长度为 <code>n</code>&nbsp;，下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>forts</code>&nbsp;，表示一些城堡。<code>forts[i]</code> 可以是&nbsp;<code>-1</code>&nbsp;，<code>0</code>&nbsp;或者&nbsp;<code>1</code>&nbsp;，其中：</p>

<ul>
	<li><code>-1</code>&nbsp;表示第&nbsp;<code>i</code>&nbsp;个位置 <strong>没有</strong>&nbsp;城堡。</li>
	<li><code>0</code>&nbsp;表示第&nbsp;<code>i</code>&nbsp;个位置有一个 <strong>敌人</strong>&nbsp;的城堡。</li>
	<li><code>1</code>&nbsp;表示第&nbsp;<code>i</code>&nbsp;个位置有一个你控制的城堡。</li>
</ul>

<p>现在，你需要决定，将你的军队从某个你控制的城堡位置&nbsp;<code>i</code>&nbsp;移动到一个空的位置&nbsp;<code>j</code>&nbsp;，满足：</p>

<ul>
	<li><code>0 &lt;= i, j &lt;= n - 1</code></li>
	<li>军队经过的位置 <strong>只有</strong>&nbsp;敌人的城堡。正式的，对于所有&nbsp;<code>min(i,j) &lt; k &lt; max(i,j)</code>&nbsp;的&nbsp;<code>k</code>&nbsp;，都满足&nbsp;<code>forts[k] == 0</code>&nbsp;。</li>
</ul>

<p>当军队移动时，所有途中经过的敌人城堡都会被 <strong>摧毁</strong> 。</p>

<p>请你返回 <strong>最多</strong>&nbsp;可以摧毁的敌人城堡数目。如果 <strong>无法</strong>&nbsp;移动你的军队，或者没有你控制的城堡，请返回 <code>0</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>forts = [1,0,0,-1,0,0,0,0,1]
<b>输出：</b>4
<strong>解释：</strong>
- 将军队从位置 0 移动到位置 3 ，摧毁 2 个敌人城堡，位置分别在 1 和 2 。
- 将军队从位置 8 移动到位置 3 ，摧毁 4 个敌人城堡。
4 是最多可以摧毁的敌人城堡数目，所以我们返回 4 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>forts = [0,0,1,-1]
<b>输出：</b>0
<b>解释：</b>由于无法摧毁敌人的城堡，所以返回 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= forts.length &lt;= 1000</code></li>
	<li><code>-1 &lt;= forts[i] &lt;= 1</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 双指针

## 提示

1. For each fort under your command, check if you can move the army from here.
2. If yes, find the closest empty positions satisfying all criteria.
3. How can two-pointers be used to solve this problem optimally?

## 示例

```
[1,0,0,-1,0,0,0,0,1]
[0,0,1,-1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int captureForts(vector<int>& forts) {
        
    }
};
```

### Java

```java
class Solution {
    public int captureForts(int[] forts) {
        
    }
}
```

### Python

```python
class Solution(object):
    def captureForts(self, forts):
        """
        :type forts: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def captureForts(self, forts: List[int]) -> int:
        
```

### C

```c
int captureForts(int* forts, int fortsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int CaptureForts(int[] forts) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} forts
 * @return {number}
 */
var captureForts = function(forts) {
    
};
```

### TypeScript

```typescript
function captureForts(forts: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $forts
     * @return Integer
     */
    function captureForts($forts) {
        
    }
}
```

### Swift

```swift
class Solution {
    func captureForts(_ forts: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun captureForts(forts: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int captureForts(List<int> forts) {
    
  }
}
```

### Go

```golang
func captureForts(forts []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} forts
# @return {Integer}
def capture_forts(forts)
    
end
```

### Scala

```scala
object Solution {
    def captureForts(forts: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn capture_forts(forts: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (capture-forts forts)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec capture_forts(Forts :: [integer()]) -> integer().
capture_forts(Forts) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec capture_forts(forts :: [integer]) :: integer
  def capture_forts(forts) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func captureForts(forts: Array<Int64>): Int64 {

    }
}
```

