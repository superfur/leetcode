# LCP 40. 心算挑战

## 题目描述

「力扣挑战赛」心算项目的挑战比赛中，要求选手从 `N` 张卡牌中选出 `cnt` 张卡牌，若这 `cnt` 张卡牌数字总和为偶数，则选手成绩「有效」且得分为 `cnt` 张卡牌数字总和。
给定数组 `cards` 和 `cnt`，其中 `cards[i]` 表示第 `i` 张卡牌上的数字。 请帮参赛选手计算最大的有效得分。若不存在获取有效得分的卡牌方案，则返回 0。

**示例 1：**
>输入：`cards = [1,2,8,9], cnt = 3`
>
>输出：`18`
>
>解释：选择数字为 1、8、9 的这三张卡牌，此时可获得最大的有效得分 1+8+9=18。

**示例 2：**
>输入：`cards = [3,3,1], cnt = 1`
>
>输出：`0`
>
>解释：不存在获取有效得分的卡牌方案。

**提示：**
- `1 <= cnt <= cards.length <= 10^5`
- `1 <= cards[i] <= 1000`




## 难度

Easy

## 标签

- 贪心
- 数组
- 排序

## 示例

```
[1,2,8,9]
3
[3,3,1]
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximumScore(vector<int>& cards, int cnt) {

    }
};
```

### Java

```java
class Solution {
    public int maximumScore(int[] cards, int cnt) {

    }
}
```

### Python

```python
class Solution(object):
    def maximumScore(self, cards, cnt):
        """
        :type cards: List[int]
        :type cnt: int
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def maximumScore(self, cards: List[int], cnt: int) -> int:
```

### C

```c
int maximumScore(int* cards, int cardsSize, int cnt) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximumScore(int[] cards, int cnt) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} cards
 * @param {number} cnt
 * @return {number}
 */
var maximumScore = function(cards, cnt) {

};
```

### TypeScript

```typescript
function maximumScore(cards: number[], cnt: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $cards
     * @param Integer $cnt
     * @return Integer
     */
    function maximumScore($cards, $cnt) {

    }
}
```

### Swift

```swift
class Solution {
    func maximumScore(_ cards: [Int], _ cnt: Int) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumScore(cards: IntArray, cnt: Int): Int {

    }
}
```

### Go

```golang
func maximumScore(cards []int, cnt int) int {

}
```

### Ruby

```ruby
# @param {Integer[]} cards
# @param {Integer} cnt
# @return {Integer}
def maximum_score(cards, cnt)

end
```

### Scala

```scala
object Solution {
    def maximumScore(cards: Array[Int], cnt: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_score(cards: Vec<i32>, cnt: i32) -> i32 {

    }
}
```

