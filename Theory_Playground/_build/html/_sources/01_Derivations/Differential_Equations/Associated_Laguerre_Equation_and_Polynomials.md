# Associated Laguerre Equation and Polynomials (連帶拉蓋爾方程式的截斷條件與正交性)

+++

## 證明目標:

中心力場的徑向問題，在做完無因次化與[漸近行為剝離](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Differential_Equations/Asymptotic_Peeling_of_the_Laguerre_Type_Radial_Equation.html)之後，恆化為下列本徵方程式：

$$x\frac{d^2v}{dx^2} + \left( p + 1 - x \right)\frac{dv}{dx} + q\,v = 0$$

本文從這條式子出發，逐式證明下列四件事：

* (a) 冪級數係數滿足

  $$a_{k+1} = \frac{k - q}{\left( k+1 \right)\left( k+p+1 \right)}a_k$$

* (b) 若級數**不**截斷，則 $v\left( x \right)$ 在 $x \to \infty$ 的行為與 $e^{x}$ 同階，物理解隨之發散。
* (c) 因此級數必須截斷，這**強迫**本徵值量子化：

  $$q = 0, 1, 2, \dots \qquad \text{且} \qquad \deg v = q$$

  截斷後的多項式解記為連帶拉蓋爾多項式 $L_q^p\left( x \right)$。
* (d) 方程式的自伴形式與帶權正交性：

  $$\frac{d}{dx}\left[ x^{p+1}e^{-x}\frac{dv}{dx} \right] + q\,x^{p}e^{-x}v = 0, \qquad \int_{0}^{\infty}x^{p}e^{-x}L_{q}^{p}\left( x \right)L_{q'}^{p}\left( x \right)dx = 0 \quad \left( q \ne q' \right)$$

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【定義 1】 連帶拉蓋爾方程式 (Associated Laguerre equation)：**

  $$x\frac{d^2v}{dx^2} + \left( p + 1 - x \right)\frac{dv}{dx} + q\,v = 0$$

  * $x$ : 無因次自變數 (Dimensionless independent variable) $[\text{無單位}]$，$0 \le x < \infty$
  * $v(x)$ : 待求解 (Solution) $[\text{無單位}]$
  * $p$ : 方程式的階參數 (Order parameter) $[\text{無單位}]$，$p > -1$
  * $q$ : 本徵值 (Eigenvalue) $[\text{無單位}]$，待定

* **【假設 1】 無窮遠處的可歸一化條件 (Normalizability at infinity)：** 【定義 1】的 $v$ **不是**物理上要求的那個解——它只是原方程式（拉蓋爾型徑向方程式）在剝離兩端漸近行為之後剩下的餘因子。真正要求可歸一化的是完整解 $u$，故 $u$ 在無窮遠處必須趨於零，否則機率積分發散。

  $$\lim_{x \to \infty}u\left( x \right) = 0$$

  * $u(x)$ : 尚未剝離漸近行為的完整徑向解 (Full radial solution) $[\text{無單位}]$
  * $x$ : 無因次自變數 (Dimensionless independent variable) $[\text{無單位}]$，$0 \le x < \infty$

* **【已知 1】 [漸近行為的剝離設定 (The asymptotic peeling ansatz)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Differential_Equations/Asymptotic_Peeling_of_the_Laguerre_Type_Radial_Equation.html#c-proof-the-peeling-ansatz)：** 適用前提為 $u$ 滿足拉蓋爾型徑向方程式 $u'' + \dfrac{b}{x}u' + \left[ -\dfrac{1}{4} + \dfrac{\lambda}{x} - \dfrac{c}{x^{2}} \right]u = 0$，且在無窮遠可歸一化、在原點有界。此時 $u$ 在兩端的漸近行為分別是 $e^{-x/2}$（由 $x \to \infty$ 的主導平衡解出）與 $x^{\alpha}$（由 $x \to 0$ 的指標方程式解出）；把這兩個因子提出來之後剩下的部分，即為【定義 1】所要解的 $v$。

  $$u\left( x \right) = e^{-x/2}x^{\alpha}v\left( x \right)$$

  * $u(x)$ : 尚未剝離漸近行為的完整徑向解 (Full radial solution) $[\text{無單位}]$
  * $v(x)$ : 剝離之後剩下的餘因子，即【定義 1】所要解的那個函數 (Residual factor) $[\text{無單位}]$
  * $\alpha$ : 原點處的冪次 (Exponent at the origin) $[\text{無單位}]$，為指標方程式 $\alpha^{2} + \left( b-1 \right)\alpha - c = 0$ 的較大根；三維庫倫問題為 $\alpha = \ell$
  * $b, c, \lambda$ : 徑向方程式的一階項係數、離心項係數與無因次能量參數 (Coefficients of the radial equation) $[\text{無單位}]$
  * 註：$e^{-x/2}$ 與 $x^{\alpha}$ 都**不是**人為湊出來的設定，而是分別把原方程式在 $x \to \infty$ 與 $x \to 0$ 取極限後解出來的結果，證明見上方連結。

* **【已知 2】 冪級數展開 (Power series expansion)：**

  $$v\left( x \right) = \sum_{k=0}^{\infty}a_k x^{k}$$

  * $a_k$ : 第 $k$ 階展開係數 (Expansion coefficient) $[\text{無單位}]$

* **【已知 3】 指數函數的冪級數 (Power series of the exponential)：** 用來辨認級數在無窮遠的漸近行為。

  $$e^{x} = \sum_{k=0}^{\infty}\frac{x^{k}}{k!}$$

* **【已知 4】 [Sturm–Liouville 本徵函數的正交性 (Orthogonality of Sturm–Liouville eigenfunctions)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Differential_Equations/Sturm_Liouville_Orthogonality.html)：** 適用前提為方程式可寫成自伴形式 $\dfrac{d}{dz}\left[ p_{\text{SL}}\dfrac{d\psi}{dz} \right] + \left( q_{\text{SL}} + \lambda w \right)\psi = 0$，且邊界項 $\left[ p_{\text{SL}}\left( \psi_i\psi_j' - \psi_j\psi_i' \right) \right]_a^b = 0$；此時對應到相異本徵值的本徵函數，在權函數 $w$ 之下彼此正交。

  $$\int_{a}^{b} w\left( z \right)\psi_{i}\left( z \right)\psi_{j}\left( z \right) dz = 0, \qquad \lambda_i \ne \lambda_j$$

  * $\psi_i$ : 第 $i$ 個本徵函數 (Eigenfunction) $[\text{無單位}]$
  * $w(z)$ : 權函數 (Weight function) $[\text{無單位}]$
  * $\lambda_i$ : 第 $i$ 個本徵值 (Eigenvalue) $[\text{無單位}]$
  * $p_{\text{SL}}, q_{\text{SL}}$ : 自伴形式的兩個係數函數 (Coefficients of the self-adjoint form) $[\text{無單位}]$
  * $a, b$ : 積分區間的兩個端點 (Endpoints of the interval)

* **【推導 1】 級數各項的指標平移 (Index shift of the series terms)：** 把【已知 2】代入【定義 1】的每一項，並統一整理成 $x^{k}$ 的係數，供 (a) 比對。

  * (a) 二階項（先代入級數、再微分兩次並乘上 $x$，得到的最低冪次為 $x^{-1}$，故令 $k \to k+1$ 平移）：

  $$\begin{gather*}
  x\frac{d^2v}{dx^2} &\overset{\text{已知 2}}{=}& x\frac{d^2}{dx^2}\left[ \sum_{k=0}^{\infty}a_k x^{k} \right] \\
  &=& \sum_{k=0}^{\infty}k\left( k-1 \right)a_k x^{k-1} \\
  &=& \sum_{k=0}^{\infty}\left( k+1 \right)k\,a_{k+1}x^{k}
  \end{gather*}$$

  * (b) 一階項中不含 $x$ 的部分（先代入級數、再微分一次，同樣需要平移）：

  $$\begin{gather*}
  \left( p+1 \right)\frac{dv}{dx} &\overset{\text{已知 2}}{=}& \left( p+1 \right)\frac{d}{dx}\left[ \sum_{k=0}^{\infty}a_k x^{k} \right] \\
  &=& \sum_{k=0}^{\infty}\left( p+1 \right)k\,a_k x^{k-1} \\
  &=& \sum_{k=0}^{\infty}\left( p+1 \right)\left( k+1 \right)a_{k+1}x^{k}
  \end{gather*}$$

  * (c) 一階項中含 $x$ 的部分（微分後再乘上 $x$，冪次已是 $x^{k}$，不需平移）：

  $$\begin{gather*}
  -x\frac{dv}{dx} &\overset{\text{已知 2}}{=}& -x\frac{d}{dx}\left[ \sum_{k=0}^{\infty}a_k x^{k} \right] \\
  &=& -\sum_{k=0}^{\infty}k\,a_k x^{k}
  \end{gather*}$$

  * (d) 零階項（不含微分，直接代入級數即可）：

  $$q\,v \overset{\text{已知 2}}{=} \sum_{k=0}^{\infty}q\,a_k x^{k}$$

+++

## 證明:

### (a) proof 級數遞迴關係 (Series recurrence relation)

把【推導 1】的四項相加，並要求每一個 $x^{k}$ 的係數為零：

$$\begin{gather*}
0 &\overset{\text{推導 1(a)(b)(c)(d)}}{=}& \left( k+1 \right)k\,a_{k+1} + \left( p+1 \right)\left( k+1 \right)a_{k+1} - k\,a_k + q\,a_k \\
0 &=& \left( k+1 \right)\left( k + p + 1 \right)a_{k+1} - \left( k - q \right)a_k \\
\left( k+1 \right)\left( k + p + 1 \right)a_{k+1} &=& \left( k - q \right)a_k \\
a_{k+1} &=& \frac{k - q}{\left( k+1 \right)\left( k+p+1 \right)}a_k
\end{gather*}$$

（由於【定義 1】要求 $p > -1$，且 $k \ge 0$，故分母 $\left( k+1 \right)\left( k+p+1 \right)$ 恆不為零。）

### (b) proof 不截斷則於無窮遠發散 (Divergence at infinity without truncation)

若級數不截斷，取 $k \to \infty$ 的漸近比值：

$$\begin{gather*}
\frac{a_{k+1}}{a_k} &\overset{\text{(a)}}{=}& \frac{k - q}{\left( k+1 \right)\left( k+p+1 \right)} \\
&=& \frac{1}{k}\cdot\frac{1 - q/k}{\left( 1 + 1/k \right)\left( 1 + \left( p+1 \right)/k \right)} \\
&=& \frac{1}{k} + O\left( k^{-2} \right)
\end{gather*}$$

拿【已知 3】當比較對象：

$$\begin{gather*}
\frac{c_{k+1}}{c_k} &\overset{\text{已知 3}}{=}& \frac{1/\left( k+1 \right)!}{1/k!} \\
&=& \frac{1}{k+1} \\
&=& \frac{1}{k} + O\left( k^{-2} \right)
\end{gather*}$$

兩者漸近比值相同，故 $v\left( x \right)$ 在 $x \to \infty$ 的行為與 $e^{x}$ 同階。代回【已知 1】的剝離設定：

$$\begin{gather*}
u\left( x \right) &\overset{\text{已知 1}}{=}& e^{-x/2}x^{\alpha}v\left( x \right) \\
&\sim& e^{-x/2}x^{\alpha}e^{x} \\
&\sim& x^{\alpha}e^{x/2}
\end{gather*}$$

$\alpha$ 有限而 $e^{x/2}$ 在 $x \to \infty$ 發散，故 $u\left( x \right) \to \infty$，與【假設 1】的 $u\left( x \right) \to 0$ 矛盾。

### (c) proof 截斷條件與本徵值量子化 (Truncation condition and eigenvalue quantization)

由 (b)，級數**必須**在某個 $k = k_{\max}$ 截斷。截斷即要求 (a) 的分子為零：

$$\begin{gather*}
a_{k_{\max}+1} &\overset{\text{def}}{=}& 0 \\
k_{\max} - q &\overset{\text{(a)}}{=}& 0 \\
q &=& k_{\max}
\end{gather*}$$

而 $k_{\max} \in \left\{ 0, 1, 2, \dots \right\}$，故本徵值必為非負整數：

$$q = 0, 1, 2, \dots$$

且截斷後的 $v$ 為次數恰為 $q$ 的多項式。把此多項式解記為連帶拉蓋爾多項式：

$$\begin{gather*}
v\left( x \right) &\overset{\text{def}}{=}& L_{q}^{p}\left( x \right) \\
\deg L_{q}^{p} &=& q
\end{gather*}$$

（與【連帶勒讓德方程式】的遞迴每次跨兩階不同，此處遞迴每次只跨一階，故截斷後多項式**同時含有奇偶兩種冪次**，不具定宇稱。）

### (d) proof 自伴形式與帶權正交性 (Self-adjoint form and weighted orthogonality)

把【定義 1】整體乘上積分因子 $x^{p}e^{-x}$：

$$\begin{gather*}
0 &\overset{\text{定義 1}}{=}& x^{p}e^{-x}\left\{ x\frac{d^2v}{dx^2} + \left( p + 1 - x \right)\frac{dv}{dx} + q\,v \right\} \\
0 &=& x^{p+1}e^{-x}\frac{d^2v}{dx^2} + x^{p}e^{-x}\left( p + 1 - x \right)\frac{dv}{dx} + q\,x^{p}e^{-x}v
\end{gather*}$$

前兩項恰好是一個乘積的導數，因為

$$\begin{gather*}
\frac{d}{dx}\left[ x^{p+1}e^{-x} \right] &=& \left( p+1 \right)x^{p}e^{-x} - x^{p+1}e^{-x} \\
&=& x^{p}e^{-x}\left( p + 1 - x \right)
\end{gather*}$$

故

$$\frac{d}{dx}\left[ x^{p+1}e^{-x}\frac{dv}{dx} \right] + q\,x^{p}e^{-x}v = 0$$

此即自伴形式，可與【已知 4】對照：$p_{\text{SL}}\left( x \right) = x^{p+1}e^{-x}$、$q_{\text{SL}} = 0$、權函數 $w\left( x \right) = x^{p}e^{-x}$、本徵值為 $q$、區間為 $\left[ 0, \infty \right)$。邊界項在兩端皆消失：

* (d-1) 原點端（由【定義 1】的 $p > -1$ 保證指數為正）：

$$\begin{gather*}
p_{\text{SL}}\left( 0 \right) &=& 0^{p+1}e^{0} \\
&=& 0
\end{gather*}$$

* (d-2) 無窮遠端（指數衰減壓過任何冪次）：

$$\begin{gather*}
\lim_{x \to \infty}p_{\text{SL}}\left( x \right) &=& \lim_{x \to \infty}x^{p+1}e^{-x} \\
&=& 0
\end{gather*}$$

套【已知 4】即得

$$\int_{0}^{\infty}x^{p}e^{-x}L_{q}^{p}\left( x \right)L_{q'}^{p}\left( x \right)dx = 0, \qquad q \ne q'$$

+++

## 結構解釋

### 兩種截斷，兩種量子數

把本文與 ⟨Associated Legendre Equation and Quantization⟩ 並排看，會發現同一套邏輯被用了兩次：**級數不截斷就在邊界爆掉，所以必須截斷，而截斷條件把本徵值鎖成整數**。差別只在「哪個邊界」與「怎麼爆」——勒讓德是在**有限端點** $x = \pm 1$ 爆成 $\left( 1-x^2 \right)^{-|m|/2}$ 或對數發散；拉蓋爾是在**無窮遠**爆成 $e^{x}$。前者給出角動量量子數 $l$，後者給出主量子數 $n$。

### 為什麼分母是 $\left( k+1 \right)\left( k+p+1 \right)$ 而不是 $k^2$

分母的兩個因子分別來自二階項與一階項的指標平移。真正決定漸近行為的是分母比分子高一次冪：$\dfrac{a_{k+1}}{a_k}\sim\dfrac{k}{k^2}=\dfrac{1}{k}$，而 $1/k$ 正是 $e^{x}$ 的係數比。**指數發散不是巧合，是「一階項係數為 $-x$」這個結構的必然後果**——若把 $-x\dfrac{dv}{dx}$ 換成別的東西，漸近行為就會跟著換。

### 權函數 $x^{p}e^{-x}$ 從哪裡冒出來

自伴化的積分因子不是湊出來的：要讓 $x\dfrac{d^2}{dx^2}+\left( p+1-x \right)\dfrac{d}{dx}$ 變成 $\dfrac{1}{w}\dfrac{d}{dx}\left[ p_{\text{SL}}\dfrac{d}{dx} \right]$，必須有 $\dfrac{p_{\text{SL}}'}{p_{\text{SL}}}=\dfrac{p+1-x}{x}$，兩邊積分立刻得到 $p_{\text{SL}}=x^{p+1}e^{-x}$，再除以領導係數 $x$ 就是 $w=x^{p}e^{-x}$。在氫原子裡，這個 $e^{-x}$ 正是波函數 $e^{-\rho/2}$ 的平方，而 $x^{p}=\rho^{2l+1}$ 則吸收了 $\rho^{2l}$ 與體積元素的 $\rho^{2}$ 中的一部分——**權函數其實就是「機率密度乘上體積元素」的化身**。

### 這族解在哪裡還會再出現

只要位能是庫倫型 $1/r$、或問題可化為三維等向諧振子的徑向部分，就會回到這條方程式：氫原子與類氫離子的徑向波函數、里德堡態的分析、以及量子光學中相干態在 Fock 基底下的展開係數。因此把截斷條件在這裡一次證清楚，之後只需引用。
