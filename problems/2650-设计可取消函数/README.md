# 2650. 设计可取消函数

## 题目描述

<p>有时候你会有一个长时间运行的任务，并且你可能希望在它完成之前取消它。为了实现这个目标，请你编写一个名为 <code>cancellable</code> 的函数，它接收一个生成器对象，并返回一个包含两个值的数组：一个 <strong>取消函数</strong> 和一个 <strong>promise</strong> 对象。</p>

<p>你可以假设生成器函数只会生成 promise 对象。你的函数负责将 promise 对象解析的值传回生成器。如果 promise 被拒绝，你的函数应将该错误抛回给生成器。</p>

<p>如果在生成器完成之前调用了取消回调函数，则你的函数应该将错误抛回给生成器。该错误应该是字符串 <code>"Cancelled"</code>（而不是一个 <code>Error</code> 对象）。如果错误被捕获，则返回的 promise 应该解析为下一个生成或返回的值。否则，promise 应该被拒绝并抛出该错误。不应执行任何其他代码。</p>

<p>当生成器完成时，您的函数返回的 promise 应该解析为生成器返回的值。但是，如果生成器抛出错误，则返回的 promise 应该拒绝并抛出该错误。</p>

<p>下面的示例展示了你的代码会如何被使用：</p>

<pre>
function* tasks() {
  const val = yield new Promise(resolve =&gt; resolve(2 + 2));
  yield new Promise(resolve =&gt; setTimeout(resolve, 100));
  return val + 1; // calculation shouldn't be done.
}
const [cancel, promise] = cancellable(tasks());
setTimeout(cancel, 50);
promise.catch(console.log); // logs "Cancelled" at t=50ms
</pre>

<p>相反，如果 <code>cancel()</code> 没有被调用或者在 <code>t=100ms</code> 之后才被调用，那么 promise 应被解析为 <code>5</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>
generatorFunction = function*() { 
&nbsp; return 42; 
}
cancelledAt = 100
<strong>输出：</strong>{"resolved": 42}
<strong>解释：</strong>
const generator = generatorFunction();
const [cancel, promise] = cancellable(generator);
setTimeout(cancel, 100);
promise.then(console.log); // 在 t=0ms 解析为 42

该生成器立即生成 42 并完成。因此，返回的 promise 立即解析为 42。请注意，取消已经完成的生成器没有任何作用。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>
generatorFunction = function*() { 
&nbsp; const msg = yield new Promise(res =&gt; res("Hello")); 
&nbsp; throw `Error: ${msg}`; 
}
cancelledAt = null
<strong>输出：</strong>{"rejected": "Error: Hello"}
<strong>解释：</strong>
一个 Promise 被生成。该函数通过等待 promise 解析并将解析后的值传回生成器来处理它。然后抛出一个错误，这会导致 promise 被同样抛出的错误拒绝。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>
generatorFunction = function*() { 
&nbsp; yield new Promise(res =&gt; setTimeout(res, 200)); 
&nbsp; return "Success"; 
}
cancelledAt = 100
<strong>输出：</strong>{"rejected": "Cancelled"}
<strong>解释：</strong>
当函数等待被生成的 promise 解析时，cancel() 被调用。这会导致一个错误消息被发送回生成器。由于这个错误没有被捕获，返回的 promise 会因为这个错误而被拒绝。
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>
generatorFunction = function*() { 
&nbsp; let result = 0; 
&nbsp; yield new Promise(res =&gt; setTimeout(res, 100));
&nbsp; result += yield new Promise(res =&gt; res(1)); 
&nbsp; yield new Promise(res =&gt; setTimeout(res, 100)); 
&nbsp; result += yield new Promise(res =&gt; res(1)); 
&nbsp; return result;
}
cancelledAt = null
<strong>输出：</strong>{"resolved": 2}
<strong>解释：</strong>
生成器生成了 4 个 promise 。其中两个 promise 的值被添加到结果中。200ms 后，生成器以值 2 完成，该值被返回的 promise 解析。
</pre>

<p><strong>示例 5：</strong></p>

<pre>
<strong>输入：</strong>
generatorFunction = function*() { 
&nbsp; let result = 0; 
&nbsp; try { 
&nbsp;   yield new Promise(res =&gt; setTimeout(res, 100)); 
&nbsp;   result += yield new Promise(res =&gt; res(1)); 
&nbsp;   yield new Promise(res =&gt; setTimeout(res, 100)); 
&nbsp;   result += yield new Promise(res =&gt; res(1)); 
&nbsp; } catch(e) { 
&nbsp;   return result; 
&nbsp; } 
&nbsp; return result; 
}
cancelledAt = 150
<strong>输出：</strong>{"resolved": 1}
<strong>解释：</strong>
前两个生成的 promise 解析并导致结果递增。然而，在 t=150ms 时，生成器被取消了。发送给生成器的错误被捕获，结果被返回并最终由返回的 promise 解析。
</pre>

<p><strong>示例 6：</strong></p>

<pre>
<strong>输入：</strong>
generatorFunction = function*() { 
&nbsp; try { 
&nbsp;   yield new Promise((resolve, reject) =&gt; reject("Promise Rejected")); 
&nbsp; } catch(e) { 
&nbsp;   let a = yield new Promise(resolve =&gt; resolve(2));
    let b = yield new Promise(resolve =&gt; resolve(2)); 
&nbsp;   return a + b; 
&nbsp; }; 
}
cancelledAt = null
<strong>输出：</strong>{"resolved": 4}
<strong>解释：</strong>
第一个生成的 promise 立即被拒绝。该错误被捕获。因为生成器没有被取消，执行继续像往常一样。最终解析为 2 + 2 = 4。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>cancelledAt == null or 0 &lt;= cancelledAt &lt;= 1000</code></li>
	<li><code>generatorFunction</code> 返回一个生成器对象</li>
</ul>


## 难度

Hard

## 提示

1. This question tests understanding of two-way communication between generator functions and the code that evaluates the generator. It is a powerful technique which is used in libraries such as redux-saga.
2. You can pass a value value to a generator function X by calling generator.next(X). Then in the generator function, you can access this value by calling let X = yield "val to pass into generator.next()";
3. You can throw an error back to a generator function by calling generator.throw(err). If this error isn't caught in the generator function, that will throw an error.

## 示例

```
function*() { return 42; }
{"cancelledAt":100}
function*() { const msg = yield new Promise(res => res("Hello")); throw `Error: ${msg}`; }
{"cancelledAt":null}
function*() { yield new Promise(res => setTimeout(res, 200)); return "Success"; }
{"cancelledAt":100}
function*() { let result = 0; yield new Promise(res => setTimeout(res, 100)); result += yield new Promise(res => res(1)); yield new Promise(res => setTimeout(res, 100)); result += yield new Promise(res => res(1)); return result; }
{"cancelledAt":null}
function*() { let result = 0; try { yield new Promise(res => setTimeout(res, 100)); result += yield new Promise(res => res(1)); yield new Promise(res => setTimeout(res, 100)); result += yield new Promise(res => res(1)); } catch(e) { return result; } return result; }
{"cancelledAt":150}
function*() { try { yield new Promise((resolve, reject) => reject("Promise Rejected")); } catch(e) { let a = yield new Promise(resolve => resolve(2)); let b = yield new Promise(resolve => resolve(2)); return a + b; }; }
{"cancelledAt":null}
```

## 示例代码

### JavaScript

```javascript
/**
 * @param {Generator} generator
 * @return {[Function, Promise]}
 */
var cancellable = function(generator) {
    
};

/**
 * function* tasks() {
 *   const val = yield new Promise(resolve => resolve(2 + 2));
 *   yield new Promise(resolve => setTimeout(resolve, 100));
 *   return val + 1;
 * }
 * const [cancel, promise] = cancellable(tasks());
 * setTimeout(cancel, 50);
 * promise.catch(console.log); // logs "Cancelled" at t=50ms
 */
```

### TypeScript

```typescript
function cancellable<T>(generator: Generator<Promise<any>, T, unknown>): [() => void, Promise<T>] {
    
};

/**
 * function* tasks() {
 *   const val = yield new Promise(resolve => resolve(2 + 2));
 *   yield new Promise(resolve => setTimeout(resolve, 100));
 *   return val + 1;
 * }
 * const [cancel, promise] = cancellable(tasks());
 * setTimeout(cancel, 50);
 * promise.catch(console.log); // logs "Cancelled" at t=50ms
 */
```

