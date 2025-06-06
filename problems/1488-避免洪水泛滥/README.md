# 1488. 避免洪水泛滥

## 题目描述

<p>你的国家有无数个湖泊，所有湖泊一开始都是空的。当第 <code>n</code>&nbsp;个湖泊下雨前是空的，那么它就会装满水。如果第 <code>n</code>&nbsp;个湖泊下雨前是 <strong>满的&nbsp;</strong>，这个湖泊会发生 <strong>洪水</strong> 。你的目标是避免任意一个湖泊发生洪水。</p>

<p>给你一个整数数组&nbsp;<code>rains</code>&nbsp;，其中：</p>

<ul>
	<li><code>rains[i] &gt; 0</code>&nbsp;表示第 <code>i</code>&nbsp;天时，第 <code>rains[i]</code>&nbsp;个湖泊会下雨。</li>
	<li><code>rains[i] == 0</code>&nbsp;表示第 <code>i</code>&nbsp;天没有湖泊会下雨，你可以选择 <strong>一个</strong>&nbsp;湖泊并 <strong>抽干</strong>&nbsp;这个湖泊的水。</li>
</ul>

<p>请返回一个数组<em>&nbsp;</em><code>ans</code>&nbsp;，满足：</p>

<ul>
	<li><code>ans.length == rains.length</code></li>
	<li>如果&nbsp;<code>rains[i] &gt; 0</code> ，那么<code>ans[i] == -1</code>&nbsp;。</li>
	<li>如果&nbsp;<code>rains[i] == 0</code>&nbsp;，<code>ans[i]</code>&nbsp;是你第&nbsp;<code>i</code>&nbsp;天选择抽干的湖泊。</li>
</ul>

<p>如果有多种可行解，请返回它们中的 <strong>任意一个</strong>&nbsp;。如果没办法阻止洪水，请返回一个 <strong>空的数组</strong>&nbsp;。</p>

<p>请注意，如果你选择抽干一个装满水的湖泊，它会变成一个空的湖泊。但如果你选择抽干一个空的湖泊，那么将无事发生。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>rains = [1,2,3,4]
<strong>输出：</strong>[-1,-1,-1,-1]
<strong>解释：</strong>第一天后，装满水的湖泊包括 [1]
第二天后，装满水的湖泊包括 [1,2]
第三天后，装满水的湖泊包括 [1,2,3]
第四天后，装满水的湖泊包括 [1,2,3,4]
没有哪一天你可以抽干任何湖泊的水，也没有湖泊会发生洪水。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>rains = [1,2,0,0,2,1]
<strong>输出：</strong>[-1,-1,2,1,-1,-1]
<strong>解释：</strong>第一天后，装满水的湖泊包括 [1]
第二天后，装满水的湖泊包括 [1,2]
第三天后，我们抽干湖泊 2 。所以剩下装满水的湖泊包括 [1]
第四天后，我们抽干湖泊 1 。所以暂时没有装满水的湖泊了。
第五天后，装满水的湖泊包括 [2]。
第六天后，装满水的湖泊包括 [1,2]。
可以看出，这个方案下不会有洪水发生。同时， [-1,-1,1,2,-1,-1] 也是另一个可行的没有洪水的方案。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>rains = [1,2,0,1,2]
<strong>输出：</strong>[]
<strong>解释：</strong>第二天后，装满水的湖泊包括 [1,2]。我们可以在第三天抽干一个湖泊的水。
但第三天后，湖泊 1 和 2 都会再次下雨，所以不管我们第三天抽干哪个湖泊的水，另一个湖泊都会发生洪水。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= rains.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= rains[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 哈希表
- 二分查找
- 堆（优先队列）

## 提示

1. Keep An array of the last day there was rains over each city.
2. Keep an array of the days you can dry a lake when you face one.
3. When it rains over a lake, check the first possible day you can dry this lake and assign this day to this lake.

## 示例

```
[1,2,3,4]
[1,2,0,0,2,1]
[1,2,0,1,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> avoidFlood(vector<int>& rains) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] avoidFlood(int[] rains) {
        
    }
}
```

### Python

```python
class Solution(object):
    def avoidFlood(self, rains):
        """
        :type rains: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* avoidFlood(int* rains, int rainsSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] AvoidFlood(int[] rains) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} rains
 * @return {number[]}
 */
var avoidFlood = function(rains) {
    
};
```

### TypeScript

```typescript
function avoidFlood(rains: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $rains
     * @return Integer[]
     */
    function avoidFlood($rains) {
        
    }
}
```

### Swift

```swift
class Solution {
    func avoidFlood(_ rains: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun avoidFlood(rains: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> avoidFlood(List<int> rains) {
    
  }
}
```

### Go

```golang
func avoidFlood(rains []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} rains
# @return {Integer[]}
def avoid_flood(rains)
    
end
```

### Scala

```scala
object Solution {
    def avoidFlood(rains: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn avoid_flood(rains: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (avoid-flood rains)
  (-> (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec avoid_flood(Rains :: [integer()]) -> [integer()].
avoid_flood(Rains) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec avoid_flood(rains :: [integer]) :: [integer]
  def avoid_flood(rains) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func avoidFlood(rains: Array<Int64>): Array<Int64> {

    }
}
```

