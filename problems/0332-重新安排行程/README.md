# 332. 重新安排行程

## 题目描述

<p>给你一份航线列表 <code>tickets</code> ，其中 <code>tickets[i] = [from<sub>i</sub>, to<sub>i</sub>]</code> 表示飞机出发和降落的机场地点。请你对该行程进行重新规划排序。</p>

<p>所有这些机票都属于一个从 <code>JFK</code>（肯尼迪国际机场）出发的先生，所以该行程必须从 <code>JFK</code> 开始。如果存在多种有效的行程，请你按字典排序返回最小的行程组合。</p>

<ul>
	<li>例如，行程 <code>["JFK", "LGA"]</code> 与 <code>["JFK", "LGB"]</code> 相比就更小，排序更靠前。</li>
</ul>

<p>假定所有机票至少存在一种合理的行程。且所有的机票 必须都用一次 且 只能用一次。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/14/itinerary1-graph.jpg" style="width: 382px; height: 222px;" />
<pre>
<strong>输入：</strong>tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
<strong>输出：</strong>["JFK","MUC","LHR","SFO","SJC"]
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/14/itinerary2-graph.jpg" style="width: 222px; height: 230px;" />
<pre>
<strong>输入：</strong>tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
<strong>输出：</strong>["JFK","ATL","JFK","SFO","ATL","SFO"]
<strong>解释：</strong>另一种有效的行程是 ["JFK","SFO","ATL","JFK","ATL","SFO"] ，但是它字典排序更大更靠后。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= tickets.length <= 300</code></li>
	<li><code>tickets[i].length == 2</code></li>
	<li><code>from<sub>i</sub>.length == 3</code></li>
	<li><code>to<sub>i</sub>.length == 3</code></li>
	<li><code>from<sub>i</sub></code> 和 <code>to<sub>i</sub></code> 由大写英文字母组成</li>
	<li><code>from<sub>i</sub> != to<sub>i</sub></code></li>
</ul>


## 难度

Hard

## 标签

- 深度优先搜索
- 图
- 欧拉回路

## 示例

```
[["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        
    }
};
```

### Java

```java
class Solution {
    public List<String> findItinerary(List<List<String>> tickets) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        
```

### Python3

```python3
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** findItinerary(char*** tickets, int ticketsSize, int* ticketsColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<string> FindItinerary(IList<IList<string>> tickets) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[][]} tickets
 * @return {string[]}
 */
var findItinerary = function(tickets) {
    
};
```

### TypeScript

```typescript
function findItinerary(tickets: string[][]): string[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[][] $tickets
     * @return String[]
     */
    function findItinerary($tickets) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findItinerary(_ tickets: [[String]]) -> [String] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findItinerary(tickets: List<List<String>>): List<String> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<String> findItinerary(List<List<String>> tickets) {
    
  }
}
```

### Go

```golang
func findItinerary(tickets [][]string) []string {
    
}
```

### Ruby

```ruby
# @param {String[][]} tickets
# @return {String[]}
def find_itinerary(tickets)
    
end
```

### Scala

```scala
object Solution {
    def findItinerary(tickets: List[List[String]]): List[String] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_itinerary(tickets: Vec<Vec<String>>) -> Vec<String> {
        
    }
}
```

### Racket

```racket
(define/contract (find-itinerary tickets)
  (-> (listof (listof string?)) (listof string?))
  )
```

### Erlang

```erlang
-spec find_itinerary(Tickets :: [[unicode:unicode_binary()]]) -> [unicode:unicode_binary()].
find_itinerary(Tickets) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_itinerary(tickets :: [[String.t]]) :: [String.t]
  def find_itinerary(tickets) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findItinerary(tickets: ArrayList<ArrayList<String>>): ArrayList<String> {

    }
}
```

