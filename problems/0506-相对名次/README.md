# 506. 相对名次

## 题目描述

<p>给你一个长度为 <code>n</code> 的整数数组 <code>score</code> ，其中 <code>score[i]</code> 是第 <code>i</code> 位运动员在比赛中的得分。所有得分都 <strong>互不相同</strong> 。</p>

<p>运动员将根据得分 <strong>决定名次</strong> ，其中名次第 <code>1</code> 的运动员得分最高，名次第 <code>2</code> 的运动员得分第 <code>2</code> 高，依此类推。运动员的名次决定了他们的获奖情况：</p>

<ul>
	<li>名次第 <code>1</code> 的运动员获金牌 <code>"Gold Medal"</code> 。</li>
	<li>名次第 <code>2</code> 的运动员获银牌 <code>"Silver Medal"</code> 。</li>
	<li>名次第 <code>3</code> 的运动员获铜牌 <code>"Bronze Medal"</code> 。</li>
	<li>从名次第 <code>4</code> 到第 <code>n</code> 的运动员，只能获得他们的名次编号（即，名次第 <code>x</code> 的运动员获得编号 <code>"x"</code>）。</li>
</ul>

<p>使用长度为 <code>n</code> 的数组 <code>answer</code> 返回获奖，其中 <code>answer[i]</code> 是第 <code>i</code> 位运动员的获奖情况。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>score = [5,4,3,2,1]
<strong>输出：</strong>["Gold Medal","Silver Medal","Bronze Medal","4","5"]
<strong>解释：</strong>名次为 [1<sup>st</sup>, 2<sup>nd</sup>, 3<sup>rd</sup>, 4<sup>th</sup>, 5<sup>th</sup>] 。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>score = [10,3,8,9,4]
<strong>输出：</strong>["Gold Medal","5","Bronze Medal","Silver Medal","4"]
<strong>解释：</strong>名次为 [1<sup>st</sup>, 5<sup>th</sup>, 3<sup>rd</sup>, 2<sup>nd</sup>, 4<sup>th</sup>] 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == score.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= score[i] &lt;= 10<sup>6</sup></code></li>
	<li><code>score</code> 中的所有值 <strong>互不相同</strong></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 排序
- 堆（优先队列）

## 示例

```
[5,4,3,2,1]
[10,3,8,9,4]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<string> findRelativeRanks(vector<int>& score) {
        
    }
};
```

### Java

```java
class Solution {
    public String[] findRelativeRanks(int[] score) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        
```

### Python3

```python3
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** findRelativeRanks(int* score, int scoreSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public string[] FindRelativeRanks(int[] score) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} score
 * @return {string[]}
 */
var findRelativeRanks = function(score) {
    
};
```

### TypeScript

```typescript
function findRelativeRanks(score: number[]): string[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $score
     * @return String[]
     */
    function findRelativeRanks($score) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findRelativeRanks(_ score: [Int]) -> [String] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findRelativeRanks(score: IntArray): Array<String> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<String> findRelativeRanks(List<int> score) {
    
  }
}
```

### Go

```golang
func findRelativeRanks(score []int) []string {
    
}
```

### Ruby

```ruby
# @param {Integer[]} score
# @return {String[]}
def find_relative_ranks(score)
    
end
```

### Scala

```scala
object Solution {
    def findRelativeRanks(score: Array[Int]): Array[String] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_relative_ranks(score: Vec<i32>) -> Vec<String> {
        
    }
}
```

### Racket

```racket
(define/contract (find-relative-ranks score)
  (-> (listof exact-integer?) (listof string?))
  )
```

### Erlang

```erlang
-spec find_relative_ranks(Score :: [integer()]) -> [unicode:unicode_binary()].
find_relative_ranks(Score) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_relative_ranks(score :: [integer]) :: [String.t]
  def find_relative_ranks(score) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findRelativeRanks(score: Array<Int64>): Array<String> {

    }
}
```

