# Coin Change
## Medium 
<div class="problem-statement">
                <p></p><p><span style="font-size:18px">Given a value N, find the number of ways to make change for N cents, if we have infinite supply of each of S = { S<sub>1</sub>, S<sub>2</sub>, .. , S<sub>M&nbsp;</sub>} valued coins. </span></p>

<p><br>
<span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
n = 4 , m = 3
S[] = {1,2,3}
<strong>Output:</strong> 4
<strong>Explanation</strong>: Four Possible ways are:
{1,1,1,1},{1,1,2},{2,2},{1,3}.</span>
</pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input</strong>:
n = 10 , m = 4
S[] ={2,5,3,6}
<strong>Output:</strong> 5
<strong>Explanation</strong>: Five Possible ways are:
{2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} 
and {5,5}.
</span></pre>

<p><br>
<span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function&nbsp;<strong>count()&nbsp;</strong>which accepts an array <strong>S[] </strong>its size <strong>m </strong>and <strong>n</strong>&nbsp;as input parameter and returns the number of ways to make change for N cents.</span></p>

<p><br>
<span style="font-size:18px"><strong>Expected Time Complexity:&nbsp;</strong>O(m*n).<br>
<strong>Expected Auxiliary Space:&nbsp;</strong>O(n). </span></p>

<p><br>
<span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;= n,m &lt;= 10<sup>3</sup></span></p>
 <p></p>
            </div>