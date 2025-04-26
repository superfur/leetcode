# 2637. 有时间限制的 Promise 对象

## 题目描述

<p>请你编写一个函数，它接受一个异步函数 <code>fn</code>&nbsp;和一个以毫秒为单位的时间 <code>t</code>。它应根据限时函数返回一个有 <strong>限时</strong> 效果的函数。函数 <code>fn</code> 接受提供给 <strong>限时</strong> 函数的参数。</p>

<p><strong>限时</strong> 函数应遵循以下规则：</p>

<ul>
	<li>如果 <code>fn</code> 在 <code>t</code> 毫秒的时间限制内完成，<strong>限时</strong> 函数应返回结果。</li>
	<li>如果 <code>fn</code> 的执行超过时间限制，<strong>限时&nbsp;</strong>函数应拒绝并返回字符串 <code>"Time Limit Exceeded"</code> 。</li>
</ul>

<p>&nbsp;</p>

<p><b>示例 1：</b></p>

<pre>
<strong>输入：</strong>
fn = async (n) =&gt; { 
&nbsp; await new Promise(res =&gt; setTimeout(res, 100)); 
&nbsp; return n * n; 
}
inputs = [5]
t = 50
<strong>输出：</strong>{"rejected":"Time Limit Exceeded","time":50}
<strong>解释：</strong>
const limited = timeLimit(fn, t)
const start = performance.now()
let result;
try {
&nbsp; &nbsp;const res = await limited(...inputs)
&nbsp; &nbsp;result = {"resolved": res, "time": Math.floor(performance.now() - start)};
} catch (err) {
&nbsp;  result = {"rejected": err, "time": Math.floor(performance.now() - start)};
}
console.log(result) // 输出结果
<b>
</b>提供的函数设置在 100ms 后执行完成，但是设置的超时时间为 50ms，所以在 t=50ms 时拒绝因为达到了超时时间。
</pre>

<p><b>示例 2：</b></p>

<pre>
<strong>输入：</strong>
fn = async (n) =&gt; { 
&nbsp; await new Promise(res =&gt; setTimeout(res, 100)); 
&nbsp; return n * n; 
}
inputs = [5]
t = 150
<strong>输出：</strong>{"resolved":25,"time":100}
<strong>解释：</strong>
在 t=100ms 时执行 5*5=25 ，没有达到超时时间。
</pre>

<p><b>示例 3：</b></p>

<pre>
<strong>输入：</strong>
fn = async (a, b) =&gt; { 
&nbsp; await new Promise(res =&gt; setTimeout(res, 120)); 
&nbsp; return a + b; 
}
inputs = [5,10]
t = 150
<strong>输出：</strong>{"resolved":15,"time":120}
<strong>解释：</strong><b>
</b>在 t=120ms 时执行 5+10=15，没有达到超时时间。
</pre>

<p><b>示例 4：</b></p>

<pre>
<strong>输入：</strong>
fn = async () =&gt; { 
&nbsp; throw "Error";
}
inputs = []
t = 1000
<strong>输出：</strong>{"rejected":"Error","time":0}
<strong>解释：</strong>
此函数始终丢出 Error</pre>

<p>&nbsp;</p>

<p><b>提示：</b></p>

<ul>
	<li><code>0 &lt;= inputs.length &lt;= 10</code></li>
	<li><code>0 &lt;= t &lt;= 1000</code></li>
	<li><code>fn</code> 返回一个 Promise 对象</li>
</ul>


## 难度

Medium

## 提示

1. You can return a copy of a function with: 

function outerFunction(fn) { 
  return function innerFunction(...params) {
    return fn(...params);
  };
}
2. Inside the inner function, you will need to return a new Promise.
3. You can create a new promise like: new Promise((resolve, reject) => {}).
4. You can execute code with a delay with "setTimeout(fn, delay)"
5. To reject a promise after a delay, "setTimeout(() => reject('err'), delay)"
6. You can resolve and reject when the passed promise resolves or rejects with: "fn(...params).then(resolve).catch(reject)"

## 示例

```
async (n) => { await new Promise(res => setTimeout(res, 100)); return n * n; }
[5]
50
async (n) => { await new Promise(res => setTimeout(res, 100)); return n * n; }
[5]
150
async (a, b) => { await new Promise(res => setTimeout(res, 120)); return a + b; }
[5,10]
150
async () => { throw "Error"; }
[]
1000
```

## 示例代码

### JavaScript

```javascript
/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function(fn, t) {
    
    return async function(...args) {
        
    }
};

/**
 * const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
 * limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms
 */
```

### TypeScript

```typescript
type Fn = (...params: any[]) => Promise<any>;

function timeLimit(fn: Fn, t: number): Fn {
    
    return async function(...args) {
        
    }
};

/**
 * const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
 * limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms
 */
```

