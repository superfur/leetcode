# 2933. 高访问员工

## 题目描述

<p>给你一个长度为 <code>n</code> 、下标从 <strong>0</strong> 开始的二维字符串数组 <code>access_times</code> 。对于每个 <code>i</code>（<code>0 &lt;= i &lt;= n - 1</code> ），<code>access_times[i][0]</code> 表示某位员工的姓名，<code>access_times[i][1]</code> 表示该员工的访问时间。<code>access_times</code> 中的所有条目都发生在同一天内。</p>

<p>访问时间用 <strong>四位</strong> 数字表示， 符合 <strong>24 小时制</strong> ，例如 <code>"0800"</code> 或 <code>"2250"</code> 。</p>

<p>如果员工在 <strong>同一小时内</strong> 访问系统 <strong>三次或更多</strong> ，则称其为 <strong>高访问</strong> 员工。</p>

<p>时间间隔正好相差一小时的时间 <strong>不</strong> 被视为同一小时内。例如，<code>"0815"</code> 和 <code>"0915"</code> 不属于同一小时内。</p>

<p>一天开始和结束时的访问时间不被计算为同一小时内。例如，<code>"0005"</code> 和 <code>"2350"</code> 不属于同一小时内。</p>

<p>以列表形式，按任意顺序，返回所有 <strong>高访问</strong> 员工的姓名。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>access_times = [["a","0549"],["b","0457"],["a","0532"],["a","0621"],["b","0540"]]
<strong>输出：</strong>["a"]
<strong>解释：</strong>"a" 在时间段 [05:32, 06:31] 内有三条访问记录，时间分别为 05:32 、05:49 和 06:21 。
但是 "b" 的访问记录只有两条。
因此，答案是 ["a"] 。</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>access_times = [["d","0002"],["c","0808"],["c","0829"],["e","0215"],["d","1508"],["d","1444"],["d","1410"],["c","0809"]]
<strong>输出：</strong>["c","d"]
<strong>解释：</strong>"c" 在时间段 [08:08, 09:07] 内有三条访问记录，时间分别为 08:08 、08:09 和 08:29 。
"d" 在时间段 [14:10, 15:09] 内有三条访问记录，时间分别为 14:10 、14:44 和 15:08 。
然而，"e" 只有一条访问记录，因此不能包含在答案中，最终答案是 ["c","d"] 。</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>access_times = [["cd","1025"],["ab","1025"],["cd","1046"],["cd","1055"],["ab","1124"],["ab","1120"]]
<strong>输出：</strong>["ab","cd"]
<strong>解释：</strong>"ab"在时间段 [10:25, 11:24] 内有三条访问记录，时间分别为 10:25 、11:20 和 11:24 。
"cd" 在时间段 [10:25, 11:24] 内有三条访问记录，时间分别为 10:25 、10:46 和 10:55 。
因此，答案是 ["ab","cd"] 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= access_times.length &lt;= 100</code></li>
	<li><code>access_times[i].length == 2</code></li>
	<li><code>1 &lt;= access_times[i][0].length &lt;= 10</code></li>
	<li><code>access_times[i][0]</code> 仅由小写英文字母组成。</li>
	<li><code>access_times[i][1].length == 4</code></li>
	<li><code>access_times[i][1]</code> 采用24小时制表示时间。</li>
	<li><code>access_times[i][1]</code> 仅由数字 <code>'0'</code> 到 <code>'9'</code> 组成。</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 字符串
- 排序

## 提示

1. Sort the access times in each person’s list.
2. A person’s name should be in the answer list if there are <code>2</code> access times in his/her access time list (after sorting), where the index difference is at least <code>2</code> and the time difference is strictly less than <code>60</code> minutes.

## 示例

```
[["a","0549"],["b","0457"],["a","0532"],["a","0621"],["b","0540"]]
[["d","0002"],["c","0808"],["c","0829"],["e","0215"],["d","1508"],["d","1444"],["d","1410"],["c","0809"]]
[["cd","1025"],["ab","1025"],["cd","1046"],["cd","1055"],["ab","1124"],["ab","1120"]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<string> findHighAccessEmployees(vector<vector<string>>& access_times) {
        
    }
};
```

### Java

```java
class Solution {
    public List<String> findHighAccessEmployees(List<List<String>> access_times) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findHighAccessEmployees(self, access_times):
        """
        :type access_times: List[List[str]]
        :rtype: List[str]
        """
        
```

### Python3

```python3
class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** findHighAccessEmployees(char*** access_times, int access_timesSize, int* access_timesColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<string> FindHighAccessEmployees(IList<IList<string>> access_times) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[][]} access_times
 * @return {string[]}
 */
var findHighAccessEmployees = function(access_times) {
    
};
```

### TypeScript

```typescript
function findHighAccessEmployees(access_times: string[][]): string[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[][] $access_times
     * @return String[]
     */
    function findHighAccessEmployees($access_times) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findHighAccessEmployees(_ access_times: [[String]]) -> [String] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findHighAccessEmployees(access_times: List<List<String>>): List<String> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<String> findHighAccessEmployees(List<List<String>> access_times) {
    
  }
}
```

### Go

```golang
func findHighAccessEmployees(access_times [][]string) []string {
    
}
```

### Ruby

```ruby
# @param {String[][]} access_times
# @return {String[]}
def find_high_access_employees(access_times)
    
end
```

### Scala

```scala
object Solution {
    def findHighAccessEmployees(access_times: List[List[String]]): List[String] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_high_access_employees(access_times: Vec<Vec<String>>) -> Vec<String> {
        
    }
}
```

### Racket

```racket
(define/contract (find-high-access-employees access_times)
  (-> (listof (listof string?)) (listof string?))
  )
```

### Erlang

```erlang
-spec find_high_access_employees(Access_times :: [[unicode:unicode_binary()]]) -> [unicode:unicode_binary()].
find_high_access_employees(Access_times) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_high_access_employees(access_times :: [[String.t]]) :: [String.t]
  def find_high_access_employees(access_times) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findHighAccessEmployees(access_times: ArrayList<ArrayList<String>>): ArrayList<String> {

    }
}
```

