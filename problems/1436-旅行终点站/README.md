# 1436. 旅行终点站

## 题目描述

<p>给你一份旅游线路图，该线路图中的旅行线路用数组 <code>paths</code> 表示，其中 <code>paths[i] = [cityA<sub>i</sub>, cityB<sub>i</sub>]</code> 表示该线路将会从 <code>cityA<sub>i</sub></code> 直接前往 <code>cityB<sub>i</sub></code> 。请你找出这次旅行的终点站，即没有任何可以通往其他城市的线路的城市<em>。</em></p>

<p>题目数据保证线路图会形成一条不存在循环的线路，因此恰有一个旅行终点站。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
<strong>输出：</strong>"Sao Paulo" 
<strong>解释：</strong>从 "London" 出发，最后抵达终点站 "Sao Paulo" 。本次旅行的路线是 "London" -&gt; "New York" -&gt; "Lima" -&gt; "Sao Paulo" 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>paths = [["B","C"],["D","B"],["C","A"]]
<strong>输出：</strong>"A"
<strong>解释：</strong>所有可能的线路是：
"D" -&gt; "B" -&gt; "C" -&gt; "A".&nbsp;
"B" -&gt; "C" -&gt; "A".&nbsp;
"C" -&gt; "A".&nbsp;
"A".&nbsp;
显然，旅行终点站是 "A" 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>paths = [["A","Z"]]
<strong>输出：</strong>"Z"
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= paths.length &lt;= 100</code></li>
	<li><code>paths[i].length == 2</code></li>
	<li><code>1 &lt;=&nbsp;cityA<sub>i</sub>.length,&nbsp;cityB<sub>i</sub>.length &lt;= 10</code></li>
	<li><code>cityA<sub>i&nbsp;</sub>!=&nbsp;cityB<sub>i</sub></code></li>
	<li>所有字符串均由大小写英文字母和空格字符组成。</li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表
- 字符串

## 提示

1. Start in any city and use the path to move to the next city.
2. Eventually, you will reach a city with no path outgoing, this is the destination city.

## 示例

```
[["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
[["B","C"],["D","B"],["C","A"]]
[["A","Z"]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string destCity(vector<vector<string>>& paths) {
        
    }
};
```

### Java

```java
class Solution {
    public String destCity(List<List<String>> paths) {
        
    }
}
```

### Python

```python
class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
```

### C

```c
char* destCity(char*** paths, int pathsSize, int* pathsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public string DestCity(IList<IList<string>> paths) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[][]} paths
 * @return {string}
 */
var destCity = function(paths) {
    
};
```

### TypeScript

```typescript
function destCity(paths: string[][]): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[][] $paths
     * @return String
     */
    function destCity($paths) {
        
    }
}
```

### Swift

```swift
class Solution {
    func destCity(_ paths: [[String]]) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun destCity(paths: List<List<String>>): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String destCity(List<List<String>> paths) {
    
  }
}
```

### Go

```golang
func destCity(paths [][]string) string {
    
}
```

### Ruby

```ruby
# @param {String[][]} paths
# @return {String}
def dest_city(paths)
    
end
```

### Scala

```scala
object Solution {
    def destCity(paths: List[List[String]]): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn dest_city(paths: Vec<Vec<String>>) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (dest-city paths)
  (-> (listof (listof string?)) string?)
  )
```

### Erlang

```erlang
-spec dest_city(Paths :: [[unicode:unicode_binary()]]) -> unicode:unicode_binary().
dest_city(Paths) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec dest_city(paths :: [[String.t]]) :: String.t
  def dest_city(paths) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func destCity(paths: ArrayList<ArrayList<String>>): String {

    }
}
```

