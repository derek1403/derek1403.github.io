# Hermite Orthonormality and Oscillator Eigenvalue (Hermite 函數的正交歸一性與諧振子本徵值)

+++

## 證明目標:

* (a) 歸一化 Hermite 函數是算子 $\dfrac{d^{2}}{d\hat{y}^{2}} - \hat{y}^{2}$ 的本徵函數，本徵值為 $-(2n+1)$：

$$\left(\frac{d^{2}}{d\hat{y}^{2}} - \hat{y}^{2}\right)\mathcal{H}_n(\hat{y}) = -(2n + 1)\,\mathcal{H}_n(\hat{y})$$

* (b) 相異階數的歸一化 Hermite 函數互相正交：

$$\int_{-\infty}^{\infty}\mathcal{H}_n(\hat{y})\,\mathcal{H}_{n'}(\hat{y})\,d\hat{y} = 0 \qquad \left(n' \neq n\right)$$

* (c) 每一階的範數恰為 $1$：

$$\int_{-\infty}^{\infty}\mathcal{H}_n^{2}(\hat{y})\,d\hat{y} = 1$$

* (d) 合起來即**正交歸一性 (Orthonormality)**：

$$\int_{-\infty}^{\infty}\mathcal{H}_n(\hat{y})\,\mathcal{H}_{n'}(\hat{y})\,d\hat{y} =
\begin{cases}
1, & n' = n \\
0, & n' \neq n
\end{cases}$$

* 註：本檔**完全不回到 $H_n$ 的二階常微分方程式**，(a)–(d) 全部只用 [Hermite Functions and Recurrence](Hermite_Functions_and_Recurrence.md) 已證的遞迴關係與微分關係推出來。這是刻意的：那兩條關係才是後續赤道波推導唯一會用到的工具。
* 註：本檔是純數學結果，$\hat{y}$ 為無因次自變數，故符號清單的單位欄一律為 $[\text{無單位}]$。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [歸一化 Hermite 函數的遞迴關係 (Recurrence relation of the normalized Hermite functions)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Differential_Equations/Hermite_Functions_and_Recurrence.html#a-proof-recurrence-relation)：** 此式已於本庫 [Hermite Functions and Recurrence](Hermite_Functions_and_Recurrence.md) 完整證明，此處直接引用不再重證

  $$\hat{y}\,\mathcal{H}_n(\hat{y}) = \left(\frac{n+1}{2}\right)^{1/2}\mathcal{H}_{n+1}(\hat{y}) + \left(\frac{n}{2}\right)^{1/2}\mathcal{H}_{n-1}(\hat{y})$$

  * $\hat{y}$ : 無因次自變數 (Dimensionless independent variable) $[\text{無單位}]$
  * $\mathcal{H}_n(\hat{y})$ : 第 $n$ 階歸一化 Hermite 函數 (The $n$-th normalized Hermite function) $[\text{無單位}]$
  * $n$ : 階數 (Order index) $[\text{無單位}]$

* **【已知 2】 [歸一化 Hermite 函數的微分關係 (Derivative relation of the normalized Hermite functions)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Differential_Equations/Hermite_Functions_and_Recurrence.html#b-proof-derivative-relation)：** 同上，此處直接引用不再重證

  $$\frac{d\mathcal{H}_n(\hat{y})}{d\hat{y}} = -\left(\frac{n+1}{2}\right)^{1/2}\mathcal{H}_{n+1}(\hat{y}) + \left(\frac{n}{2}\right)^{1/2}\mathcal{H}_{n-1}(\hat{y})$$

  * $\mathcal{H}_n(\hat{y})$ : 第 $n$ 階歸一化 Hermite 函數 (The $n$-th normalized Hermite function) $[\text{無單位}]$
  * $n$ : 階數 (Order index) $[\text{無單位}]$
  * $\hat{y}$ : 無因次自變數 (Dimensionless independent variable) $[\text{無單位}]$

* **【已知 3】 [最低階歸一化 Hermite 函數的顯式形式 (Lowest-order explicit form)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Differential_Equations/Hermite_Functions_and_Recurrence.html#c-proof-lowest-order-explicit-form)：** 同上，此處直接引用不再重證

  $$\mathcal{H}_0(\hat{y}) = \pi^{-1/4}\,e^{-\hat{y}^{2}/2}$$

  * $\mathcal{H}_n(\hat{y})$ : 第 $n$ 階歸一化 Hermite 函數 (The $n$-th normalized Hermite function) $[\text{無單位}]$
  * $\hat{y}$ : 無因次自變數 (Dimensionless independent variable) $[\text{無單位}]$

* **【已知 4】 [高斯積分 (Gaussian integral)](https://dlmf.nist.gov/7.4#E1)：** 標準結果，本檔直接引用不再重證

  $$\int_{-\infty}^{\infty} e^{-\hat{y}^{2}}\,d\hat{y} = \pi^{1/2}$$

  * $\hat{y}$ : 無因次自變數 (Dimensionless independent variable) $[\text{無單位}]$

* **【已知 5】 [Lagrange 恆等式 (Lagrange's identity)](Sturm_Liouville_Orthogonality.md)：** 此恆等式已於本庫 Sturm–Liouville 正交性一篇對一般主係數 $p(z)$ 完整證明，此處取 $p \equiv 1$ 的特例直接引用不再重證

  $$f\,\frac{d^{2}g}{d\hat{y}^{2}} - g\,\frac{d^{2}f}{d\hat{y}^{2}} = \frac{d}{d\hat{y}}\left[f\,\frac{dg}{d\hat{y}} - g\,\frac{df}{d\hat{y}}\right]$$

  * $f(\hat{y}),\ g(\hat{y})$ : 任意二階可微函數 (Arbitrary twice-differentiable functions) $[\text{無單位}]$
  * $\hat{y}$ : 無因次自變數 (Dimensionless independent variable) $[\text{無單位}]$
  * 註：Sturm–Liouville 那篇的【假設 1】限定**有限閉區間** $\left[z_b, z_t\right]$，而本檔的積分域是 $(-\infty, \infty)$，**故不能整篇套用**；邊界項的消失改由本檔的【假設 1】獨立提供。

* **【已知 6】 [分部積分 (Integration by parts)](https://dlmf.nist.gov/1.4#E33)：** 標準結果，本檔直接引用不再重證

  $$\int_{-\infty}^{\infty} u\,\frac{dv}{d\hat{y}}\,d\hat{y} = \left[u\,v\right]_{-\infty}^{\infty} - \int_{-\infty}^{\infty} v\,\frac{du}{d\hat{y}}\,d\hat{y}$$

  * $u(\hat{y}),\ v(\hat{y})$ : 任意可微函數 (Arbitrary differentiable functions) $[\text{無單位}]$
  * $\hat{y}$ : 無因次自變數 (Dimensionless independent variable) $[\text{無單位}]$

* **【假設 1】 無窮積分域與高斯衰減 (Infinite domain and Gaussian decay)：** 本檔所有積分都取在整條實軸上，而 $\mathcal{H}_n$ 的高斯包絡讓所有邊界項歸零

  * (a) 積分域為整條實軸：

    $$\int_{-\infty}^{\infty}(\cdot)\,d\hat{y}$$

  * (b) 任何多項式乘上高斯包絡，在無窮遠處都歸零：

    $$\lim_{|\hat{y}|\to\infty} P(\hat{y})\,e^{-\hat{y}^{2}/2} = 0 \qquad \left(\forall\,\text{多項式}\ P\right)$$

  * (c) $\mathcal{H}_n$ 與其導數都是「多項式 $\times$ 高斯包絡」的形式（由【已知 1】【已知 2】遞推可見，多項式部分的階數有限）：

    $$\mathcal{H}_n(\hat{y}) = P_n(\hat{y})\,e^{-\hat{y}^{2}/2}, \qquad \frac{d\mathcal{H}_n(\hat{y})}{d\hat{y}} = \tilde{P}_n(\hat{y})\,e^{-\hat{y}^{2}/2}$$

  * (d-1) 故 $\hat{y}\,\mathcal{H}_n^{2}$ 的邊界項為零：

    $$\begin{gather*}
    \left[\hat{y}\,\mathcal{H}_n^{2}\right]_{-\infty}^{\infty} &\overset{\text{假設 1(c)}}{=}& \left[\hat{y}\,P_n^{2}(\hat{y})\,e^{-\hat{y}^{2}}\right]_{-\infty}^{\infty} \\
    &\overset{\text{假設 1(b)}}{=}& 0
    \end{gather*}$$

  * (d-2) 同理，$\mathcal{H}_n$ 與其一階導數的乘積的邊界項為零：

    $$\begin{gather*}
    \left[\mathcal{H}_n\frac{d\mathcal{H}_n}{d\hat{y}}\right]_{-\infty}^{\infty} &\overset{\text{假設 1(c)}}{=}& \left[P_n(\hat{y})\,\tilde{P}_n(\hat{y})\,e^{-\hat{y}^{2}}\right]_{-\infty}^{\infty} \\
    &\overset{\text{假設 1(b)}}{=}& 0
    \end{gather*}$$

  * (d-3) 同理，兩個相異階組成的 Wronskian 型邊界項為零：

    $$\begin{gather*}
    \left[\mathcal{H}_{n'}\frac{d\mathcal{H}_n}{d\hat{y}} - \mathcal{H}_n\frac{d\mathcal{H}_{n'}}{d\hat{y}}\right]_{-\infty}^{\infty} &\overset{\text{假設 1(c)}}{=}& \left[\left(P_{n'}\tilde{P}_n - P_n\tilde{P}_{n'}\right)e^{-\hat{y}^{2}}\right]_{-\infty}^{\infty} \\
    &\overset{\text{假設 1(b)}}{=}& 0
    \end{gather*}$$

  * $P_n(\hat{y}),\ \tilde{P}_n(\hat{y})$ : 第 $n$ 階函數與其導數中的多項式部分 (Polynomial parts) $[\text{無單位}]$
  * $\hat{y}$ : 無因次自變數 (Dimensionless independent variable) $[\text{無單位}]$
  * $\mathcal{H}_n(\hat{y})$ : 第 $n$ 階歸一化 Hermite 函數 (The $n$-th normalized Hermite function) $[\text{無單位}]$
  * 註：這一張卡片是本檔與 [Sturm–Liouville 正交性](Sturm_Liouville_Orthogonality.md)**唯一實質不同**的地方 —— 那篇靠「有限區間 + 齊次邊界條件」殺掉邊界項，本檔靠「無窮區間 + 高斯衰減」。

* **【假設 2】 階數相異 (Distinct orders)：** 【證明 (b)】只比較兩個不同階的函數

  $$n' \neq n$$

  * $n$ : 階數 (Order index) $[\text{無單位}]$

* **【定義 1】 升降係數 (Ladder coefficients)：** 把【已知 1】【已知 2】反覆出現的兩個根號係數縮寫掉，避免後續代數被根號淹沒

  * (a) 上行係數：

    $$a_n \overset{\text{def}}{=} \left(\frac{n+1}{2}\right)^{1/2}$$

  * (b) 下行係數：

    $$b_n \overset{\text{def}}{=} \left(\frac{n}{2}\right)^{1/2}$$

  * $a_n$ : 第 $n$ 階的上行係數 (Raising coefficient) $[\text{無單位}]$
  * $b_n$ : 第 $n$ 階的下行係數 (Lowering coefficient) $[\text{無單位}]$
  * 註：由【定義 1】(a)(b) 直接得到本檔會反覆用到的兩條恆等式 $b_{n+1} = a_n$ 與 $a_{n-1} = b_n$。

* **【推導 1】 兩條基本關係的縮寫形式 (Shorthand form of the two basic relations)：** 把【定義 1】代進【已知 1】【已知 2】

  * (a) 遞迴關係：

    $$\begin{gather*}
    \hat{y}\,\mathcal{H}_n &\overset{\text{已知 1}}{=}& \left(\frac{n+1}{2}\right)^{1/2}\mathcal{H}_{n+1} + \left(\frac{n}{2}\right)^{1/2}\mathcal{H}_{n-1} \\
    &\overset{\text{定義 1(a)(b)}}{=}& a_n\,\mathcal{H}_{n+1} + b_n\,\mathcal{H}_{n-1}
    \end{gather*}$$

  * (b) 微分關係：

    $$\begin{gather*}
    \frac{d\mathcal{H}_n}{d\hat{y}} &\overset{\text{已知 2}}{=}& -\left(\frac{n+1}{2}\right)^{1/2}\mathcal{H}_{n+1} + \left(\frac{n}{2}\right)^{1/2}\mathcal{H}_{n-1} \\
    &\overset{\text{定義 1(a)(b)}}{=}& -a_n\,\mathcal{H}_{n+1} + b_n\,\mathcal{H}_{n-1}
    \end{gather*}$$

  * $\hat{y}$ : 無因次自變數 (Dimensionless independent variable) $[\text{無單位}]$
  * $\mathcal{H}_n(\hat{y})$ : 第 $n$ 階歸一化 Hermite 函數 (The $n$-th normalized Hermite function) $[\text{無單位}]$
  * $n$ : 階數 (Order index) $[\text{無單位}]$
  * $a_n$ : 第 $n$ 階的上行係數 (Raising coefficient) $[\text{無單位}]$
  * $b_n$ : 第 $n$ 階的下行係數 (Lowering coefficient) $[\text{無單位}]$

* **【推導 2】 兩個三項展開 (The two three-term expansions)：** 把【推導 1】各用**兩次**，$\mathcal{H}_n$ 就被推到 $\mathcal{H}_{n\pm2}$ 與 $\mathcal{H}_n$ 三項上

  * (a) 二階導數：

    $$\begin{gather*}
    \frac{d^{2}\mathcal{H}_n}{d\hat{y}^{2}} &\overset{\text{推導 1(b)}}{=}& \frac{d}{d\hat{y}}\left[-a_n\,\mathcal{H}_{n+1} + b_n\,\mathcal{H}_{n-1}\right] \\
    &=& -a_n\frac{d\mathcal{H}_{n+1}}{d\hat{y}} + b_n\frac{d\mathcal{H}_{n-1}}{d\hat{y}} \\
    &\overset{\text{推導 1(b)}}{=}& -a_n\left[-a_{n+1}\mathcal{H}_{n+2} + b_{n+1}\mathcal{H}_{n}\right] + b_n\left[-a_{n-1}\mathcal{H}_{n} + b_{n-1}\mathcal{H}_{n-2}\right] \\
    &=& a_na_{n+1}\,\mathcal{H}_{n+2} - \left(a_nb_{n+1} + b_na_{n-1}\right)\mathcal{H}_{n} + b_nb_{n-1}\,\mathcal{H}_{n-2}
    \end{gather*}$$

  * (b) 乘上 $\hat{y}^{2}$：

    $$\begin{gather*}
    \hat{y}^{2}\,\mathcal{H}_n &\overset{\text{推導 1(a)}}{=}& \hat{y}\left[a_n\,\mathcal{H}_{n+1} + b_n\,\mathcal{H}_{n-1}\right] \\
    &=& a_n\left[\hat{y}\,\mathcal{H}_{n+1}\right] + b_n\left[\hat{y}\,\mathcal{H}_{n-1}\right] \\
    &\overset{\text{推導 1(a)}}{=}& a_n\left[a_{n+1}\mathcal{H}_{n+2} + b_{n+1}\mathcal{H}_{n}\right] + b_n\left[a_{n-1}\mathcal{H}_{n} + b_{n-1}\mathcal{H}_{n-2}\right] \\
    &=& a_na_{n+1}\,\mathcal{H}_{n+2} + \left(a_nb_{n+1} + b_na_{n-1}\right)\mathcal{H}_{n} + b_nb_{n-1}\,\mathcal{H}_{n-2}
    \end{gather*}$$

  * $\mathcal{H}_n(\hat{y})$ : 第 $n$ 階歸一化 Hermite 函數 (The $n$-th normalized Hermite function) $[\text{無單位}]$
  * $n$ : 階數 (Order index) $[\text{無單位}]$
  * $\hat{y}$ : 無因次自變數 (Dimensionless independent variable) $[\text{無單位}]$
  * $a_n$ : 第 $n$ 階的上行係數 (Raising coefficient) $[\text{無單位}]$
  * $b_n$ : 第 $n$ 階的下行係數 (Lowering coefficient) $[\text{無單位}]$
  * 註：(a)(b) 的三項**完全相同**，唯一的差別是中央項的正負號。這個「只差一個符號」正是【已知 1】【已知 2】右端只差一個符號的直接後果。

* **【推導 3】 中央係數的化簡 (Simplification of the central coefficient)：** 用【定義 1】註記的兩條恆等式把根號整個消掉

  $$\begin{gather*}
  a_nb_{n+1} + b_na_{n-1} &\overset{\text{定義 1}}{=}& a_n\,a_n + b_n\,b_n \\
  &\overset{\text{定義 1(a)(b)}}{=}& \frac{n+1}{2} + \frac{n}{2} \\
  &=& \frac{2n + 1}{2}
  \end{gather*}$$

  * $a_n$ : 第 $n$ 階的上行係數 (Raising coefficient) $[\text{無單位}]$
  * $n$ : 階數 (Order index) $[\text{無單位}]$
  * $b_n$ : 第 $n$ 階的下行係數 (Lowering coefficient) $[\text{無單位}]$

* **【推導 4】 二階導數的封閉式 (Closed form of the second derivative)：** 把【推導 2】兩式相減，$\mathcal{H}_{n\pm2}$ 對消，只剩 $\mathcal{H}_n$

  $$\begin{gather*}
  \frac{d^{2}\mathcal{H}_n}{d\hat{y}^{2}} - \hat{y}^{2}\,\mathcal{H}_n &\overset{\text{推導 2(a)(b)}}{=}& -\left(a_nb_{n+1} + b_na_{n-1}\right)\mathcal{H}_{n} - \left(a_nb_{n+1} + b_na_{n-1}\right)\mathcal{H}_{n} \\
  \frac{d^{2}\mathcal{H}_n}{d\hat{y}^{2}} - \hat{y}^{2}\,\mathcal{H}_n &=& -2\left(a_nb_{n+1} + b_na_{n-1}\right)\mathcal{H}_{n} \\
  \frac{d^{2}\mathcal{H}_n}{d\hat{y}^{2}} - \hat{y}^{2}\,\mathcal{H}_n &\overset{\text{推導 3}}{=}& -2\cdot\frac{2n + 1}{2}\,\mathcal{H}_{n} \\
  \frac{d^{2}\mathcal{H}_n}{d\hat{y}^{2}} - \hat{y}^{2}\,\mathcal{H}_n &=& -(2n + 1)\,\mathcal{H}_{n} \\
  \frac{d^{2}\mathcal{H}_n}{d\hat{y}^{2}} &=& \hat{y}^{2}\,\mathcal{H}_n - (2n + 1)\,\mathcal{H}_{n}
  \end{gather*}$$

  * $\mathcal{H}_n(\hat{y})$ : 第 $n$ 階歸一化 Hermite 函數 (The $n$-th normalized Hermite function) $[\text{無單位}]$
  * $n$ : 階數 (Order index) $[\text{無單位}]$
  * $\hat{y}$ : 無因次自變數 (Dimensionless independent variable) $[\text{無單位}]$
  * $a_n$ : 第 $n$ 階的上行係數 (Raising coefficient) $[\text{無單位}]$
  * $b_n$ : 第 $n$ 階的下行係數 (Lowering coefficient) $[\text{無單位}]$

* **【推導 5】 反對稱組合的積分為零 (Vanishing of the antisymmetric combination)：** 兩階函數的「交叉相乘再相減」整成全微分，再被【假設 1】殺掉

  $$\begin{gather*}
  \int_{-\infty}^{\infty}\left[\mathcal{H}_{n'}\frac{d^{2}\mathcal{H}_n}{d\hat{y}^{2}} - \mathcal{H}_{n}\frac{d^{2}\mathcal{H}_{n'}}{d\hat{y}^{2}}\right]d\hat{y} &\overset{\text{已知 5}}{=}& \int_{-\infty}^{\infty}\frac{d}{d\hat{y}}\left[\mathcal{H}_{n'}\frac{d\mathcal{H}_n}{d\hat{y}} - \mathcal{H}_{n}\frac{d\mathcal{H}_{n'}}{d\hat{y}}\right]d\hat{y} \\
  &=& \left[\mathcal{H}_{n'}\frac{d\mathcal{H}_n}{d\hat{y}} - \mathcal{H}_{n}\frac{d\mathcal{H}_{n'}}{d\hat{y}}\right]_{-\infty}^{\infty} \\
  &\overset{\text{假設 1(d-3)}}{=}& 0
  \end{gather*}$$

  * $\mathcal{H}_n(\hat{y})$ : 第 $n$ 階歸一化 Hermite 函數 (The $n$-th normalized Hermite function) $[\text{無單位}]$
  * $n$ : 階數 (Order index) $[\text{無單位}]$
  * $\hat{y}$ : 無因次自變數 (Dimensionless independent variable) $[\text{無單位}]$

* **【推導 6】 兩個分部積分 (Two integrations by parts)：** 把【證明 (c)】會用到的兩個積分先換成不含導數平方的形式

  * (a) 導數平方的積分：

    $$\begin{gather*}
    \int_{-\infty}^{\infty}\left(\frac{d\mathcal{H}_n}{d\hat{y}}\right)^{2}d\hat{y} &\overset{\text{已知 6}}{=}& \left[\mathcal{H}_n\frac{d\mathcal{H}_n}{d\hat{y}}\right]_{-\infty}^{\infty} - \int_{-\infty}^{\infty}\mathcal{H}_n\frac{d^{2}\mathcal{H}_n}{d\hat{y}^{2}}\,d\hat{y} \\
    &\overset{\text{假設 1(d-2)}}{=}& -\int_{-\infty}^{\infty}\mathcal{H}_n\frac{d^{2}\mathcal{H}_n}{d\hat{y}^{2}}\,d\hat{y}
    \end{gather*}$$

  * (b) 交叉項的積分：

    $$\begin{gather*}
    \int_{-\infty}^{\infty}2\hat{y}\,\mathcal{H}_n\frac{d\mathcal{H}_n}{d\hat{y}}\,d\hat{y} &=& \int_{-\infty}^{\infty}\hat{y}\,\frac{d}{d\hat{y}}\left[\mathcal{H}_n^{2}\right]d\hat{y} \\
    &\overset{\text{已知 6}}{=}& \left[\hat{y}\,\mathcal{H}_n^{2}\right]_{-\infty}^{\infty} - \int_{-\infty}^{\infty}\mathcal{H}_n^{2}\,d\hat{y} \\
    &\overset{\text{假設 1(d-1)}}{=}& -\int_{-\infty}^{\infty}\mathcal{H}_n^{2}\,d\hat{y}
    \end{gather*}$$

  * $\mathcal{H}_n(\hat{y})$ : 第 $n$ 階歸一化 Hermite 函數 (The $n$-th normalized Hermite function) $[\text{無單位}]$
  * $n$ : 階數 (Order index) $[\text{無單位}]$
  * $\hat{y}$ : 無因次自變數 (Dimensionless independent variable) $[\text{無單位}]$

* **【推導 7】 升算子形式 (Raising-operator form)：** 把【推導 1】(a) 減去 (b)，$\mathcal{H}_{n-1}$ 對消，$\mathcal{H}_{n+1}$ 被單獨解出來

  $$\begin{gather*}
  \hat{y}\,\mathcal{H}_n - \frac{d\mathcal{H}_n}{d\hat{y}} &\overset{\text{推導 1(a)(b)}}{=}& \left[a_n\mathcal{H}_{n+1} + b_n\mathcal{H}_{n-1}\right] - \left[-a_n\mathcal{H}_{n+1} + b_n\mathcal{H}_{n-1}\right] \\
  \hat{y}\,\mathcal{H}_n - \frac{d\mathcal{H}_n}{d\hat{y}} &=& 2a_n\,\mathcal{H}_{n+1} \\
  \mathcal{H}_{n+1} &=& \frac{1}{2a_n}\left[\hat{y}\,\mathcal{H}_n - \frac{d\mathcal{H}_n}{d\hat{y}}\right]
  \end{gather*}$$

  * $\hat{y}$ : 無因次自變數 (Dimensionless independent variable) $[\text{無單位}]$
  * $\mathcal{H}_n(\hat{y})$ : 第 $n$ 階歸一化 Hermite 函數 (The $n$-th normalized Hermite function) $[\text{無單位}]$
  * $n$ : 階數 (Order index) $[\text{無單位}]$
  * $a_n$ : 第 $n$ 階的上行係數 (Raising coefficient) $[\text{無單位}]$
  * $b_n$ : 第 $n$ 階的下行係數 (Lowering coefficient) $[\text{無單位}]$
  * 註：由【定義 1】(a)，$n \ge 0$ 時 $a_n = \left(\frac{n+1}{2}\right)^{1/2} > 0$，故除法合法。

* **【推導 8】 範數的階不變性 (Order-invariance of the norm)：** 用【推導 7】把 $\mathcal{H}_{n+1}$ 的範數換算回 $\mathcal{H}_n$ 的範數，結果係數恰好為 $1$

  $$\begin{gather*}
  \int_{-\infty}^{\infty}\mathcal{H}_{n+1}^{2}\,d\hat{y} &\overset{\text{推導 7}}{=}& \frac{1}{4a_n^{2}}\int_{-\infty}^{\infty}\left[\hat{y}\,\mathcal{H}_n - \frac{d\mathcal{H}_n}{d\hat{y}}\right]^{2}d\hat{y} \\
  &=& \frac{1}{4a_n^{2}}\int_{-\infty}^{\infty}\left[\hat{y}^{2}\mathcal{H}_n^{2} - 2\hat{y}\,\mathcal{H}_n\frac{d\mathcal{H}_n}{d\hat{y}} + \left(\frac{d\mathcal{H}_n}{d\hat{y}}\right)^{2}\right]d\hat{y} \\
  &\overset{\text{推導 6(a)(b)}}{=}& \frac{1}{4a_n^{2}}\left[\int_{-\infty}^{\infty}\hat{y}^{2}\mathcal{H}_n^{2}\,d\hat{y} + \int_{-\infty}^{\infty}\mathcal{H}_n^{2}\,d\hat{y} - \int_{-\infty}^{\infty}\mathcal{H}_n\frac{d^{2}\mathcal{H}_n}{d\hat{y}^{2}}\,d\hat{y}\right] \\
  &\overset{\text{推導 4}}{=}& \frac{1}{4a_n^{2}}\left[\int_{-\infty}^{\infty}\hat{y}^{2}\mathcal{H}_n^{2}\,d\hat{y} + \int_{-\infty}^{\infty}\mathcal{H}_n^{2}\,d\hat{y} - \int_{-\infty}^{\infty}\mathcal{H}_n\left(\hat{y}^{2}\mathcal{H}_n - (2n+1)\mathcal{H}_n\right)d\hat{y}\right] \\
  &=& \frac{1}{4a_n^{2}}\left[\int_{-\infty}^{\infty}\mathcal{H}_n^{2}\,d\hat{y} + (2n+1)\int_{-\infty}^{\infty}\mathcal{H}_n^{2}\,d\hat{y}\right] \\
  &=& \frac{2n + 2}{4a_n^{2}}\int_{-\infty}^{\infty}\mathcal{H}_n^{2}\,d\hat{y} \\
  &\overset{\text{定義 1(a)}}{=}& \frac{2n + 2}{4\cdot\dfrac{n+1}{2}}\int_{-\infty}^{\infty}\mathcal{H}_n^{2}\,d\hat{y} \\
  &=& \int_{-\infty}^{\infty}\mathcal{H}_n^{2}\,d\hat{y}
  \end{gather*}$$

  * $\mathcal{H}_n(\hat{y})$ : 第 $n$ 階歸一化 Hermite 函數 (The $n$-th normalized Hermite function) $[\text{無單位}]$
  * $\hat{y}$ : 無因次自變數 (Dimensionless independent variable) $[\text{無單位}]$
  * $a_n$ : 第 $n$ 階的上行係數 (Raising coefficient) $[\text{無單位}]$
  * $n$ : 階數 (Order index) $[\text{無單位}]$
  * 註：第四列到第五列，兩個 $\int\hat{y}^{2}\mathcal{H}_n^{2}\,d\hat{y}$ 剛好對消 —— 這就是為什麼**完全不需要**去算 $\int\hat{y}^{2}\mathcal{H}_n^{2}\,d\hat{y}$ 這個看起來很麻煩的積分。

* **【推導 9】 起始範數 (Starting norm)：** 最低階的範數直接算得出來

  $$\begin{gather*}
  \int_{-\infty}^{\infty}\mathcal{H}_0^{2}\,d\hat{y} &\overset{\text{已知 3}}{=}& \int_{-\infty}^{\infty}\left(\pi^{-1/4}\,e^{-\hat{y}^{2}/2}\right)^{2}d\hat{y} \\
  &=& \pi^{-1/2}\int_{-\infty}^{\infty} e^{-\hat{y}^{2}}\,d\hat{y} \\
  &\overset{\text{已知 4}}{=}& \pi^{-1/2}\cdot\pi^{1/2} \\
  &=& 1
  \end{gather*}$$

  * $\mathcal{H}_n(\hat{y})$ : 第 $n$ 階歸一化 Hermite 函數 (The $n$-th normalized Hermite function) $[\text{無單位}]$
  * $\hat{y}$ : 無因次自變數 (Dimensionless independent variable) $[\text{無單位}]$

+++

## 證明:

### (a) proof 諧振子本徵值 (Harmonic oscillator eigenvalue)

把算子拆成兩項，直接引用【推導 4】的封閉式。

$$\begin{gather*}
\left(\frac{d^{2}}{d\hat{y}^{2}} - \hat{y}^{2}\right)\mathcal{H}_n &=& \frac{d^{2}\mathcal{H}_n}{d\hat{y}^{2}} - \hat{y}^{2}\,\mathcal{H}_n \\
&\overset{\text{推導 4}}{=}& -(2n + 1)\,\mathcal{H}_n
\end{gather*}$$

### (b) proof 相異階的正交性 (Orthogonality of distinct orders)

從【推導 5】的零起手，把兩個二階導數換成【證明 (a)】的本徵值形式，正交性就掉出來了。

$$\begin{gather*}
0 &\overset{\text{推導 5}}{=}& \int_{-\infty}^{\infty}\left[\mathcal{H}_{n'}\frac{d^{2}\mathcal{H}_n}{d\hat{y}^{2}} - \mathcal{H}_{n}\frac{d^{2}\mathcal{H}_{n'}}{d\hat{y}^{2}}\right]d\hat{y} \\
0 &=& \int_{-\infty}^{\infty}\left[\mathcal{H}_{n'}\left(\frac{d^{2}}{d\hat{y}^{2}} - \hat{y}^{2}\right)\mathcal{H}_n - \mathcal{H}_{n}\left(\frac{d^{2}}{d\hat{y}^{2}} - \hat{y}^{2}\right)\mathcal{H}_{n'}\right]d\hat{y} \\
0 &\overset{\text{證明 (a)}}{=}& \int_{-\infty}^{\infty}\left[-(2n+1)\,\mathcal{H}_{n'}\mathcal{H}_n + (2n'+1)\,\mathcal{H}_{n}\mathcal{H}_{n'}\right]d\hat{y} \\
0 &=& 2\left(n' - n\right)\int_{-\infty}^{\infty}\mathcal{H}_n\,\mathcal{H}_{n'}\,d\hat{y} \\
0 &\overset{\text{假設 2}}{=}& \int_{-\infty}^{\infty}\mathcal{H}_n(\hat{y})\,\mathcal{H}_{n'}(\hat{y})\,d\hat{y}
\end{gather*}$$

### (c) proof 單位範數 (Unit norm)

【推導 8】說範數不隨階數改變，於是沿著階梯一路降到【推導 9】的起始值。

$$\begin{gather*}
\int_{-\infty}^{\infty}\mathcal{H}_n^{2}\,d\hat{y} &\overset{\text{推導 8}}{=}& \int_{-\infty}^{\infty}\mathcal{H}_{n-1}^{2}\,d\hat{y} \\
&\overset{\text{推導 8}}{=}& \int_{-\infty}^{\infty}\mathcal{H}_{n-2}^{2}\,d\hat{y} \\
&\overset{\text{推導 8}}{=}& \cdots \\
&\overset{\text{推導 8}}{=}& \int_{-\infty}^{\infty}\mathcal{H}_{0}^{2}\,d\hat{y} \\
&\overset{\text{推導 9}}{=}& 1
\end{gather*}$$

### (d) proof 正交歸一性 (Orthonormality)

把【證明 (b)】與【證明 (c)】兩種情形併成一條。

$$\int_{-\infty}^{\infty}\mathcal{H}_n(\hat{y})\,\mathcal{H}_{n'}(\hat{y})\,d\hat{y} \overset{\text{證明 (b)(c)}}{=}
\begin{cases}
1, & n' = n \\
0, & n' \neq n
\end{cases}$$

+++

## 結構解釋

### 兩條關係，一個本徵值

【推導 2】把「二階微分」與「乘 $\hat{y}^{2}$」各展成三項，兩式的 $\mathcal{H}_{n+2}$ 與 $\mathcal{H}_{n-2}$ 項**係數完全相同**，中央項**恰好反號**。相減之後，兩端的鄰居全數消失，只剩中間那一項的兩倍。

這件事的來源非常單純：【已知 1】與【已知 2】的右端只差一個負號（見 [Hermite Functions and Recurrence 的數值與結構解釋](Hermite_Functions_and_Recurrence.md)）。**本徵值 $-(2n+1)$ 完全是這個符號差的產物**，不需要任何額外的微分方程知識。

### 為什麼「有本徵值」就有「正交」

【證明 (b)】的骨架是所有自伴算子共通的：

1. 造一個**反對稱**的組合 $\mathcal{H}_{n'}\left(\frac{d^{2}}{d\hat{y}^{2}} - \hat{y}^{2}\right)\mathcal{H}_n - \mathcal{H}_n\left(\frac{d^{2}}{d\hat{y}^{2}} - \hat{y}^{2}\right)\mathcal{H}_{n'}$；
2. 用 Lagrange 恆等式把它整成一個**全微分**，積分後只剩邊界項；
3. 邊界項為零 $\Rightarrow$ 整個積分為零；
4. 另一邊用本徵值算同一個積分，得到 $2(n'-n)\int\mathcal{H}_n\mathcal{H}_{n'}\,d\hat{y}$；
5. 兩邊相等，而 $n' \neq n$，只好是積分為零。

跟 [Sturm–Liouville 正交性](Sturm_Liouville_Orthogonality.md) 是**完全同一套機制**。唯一的差別在第 3 步：那篇靠「有限區間 + 齊次邊界條件」，本篇靠「無窮區間 + 高斯衰減」（【假設 1】）。$\hat{y}^{2}$ 這個位能項在無窮遠處把波函數壓死，扮演的正是邊界條件的角色。

### 歸一化為什麼「免費」

$\left\{\mathcal{H}_n\right\}$ 的範數之所以**全部**是 $1$，並不是每一階各自湊出來的，而是【推導 8】那個 $\dfrac{2n+2}{4a_n^{2}} = 1$ 的巧合 —— 而這個「巧合」正是 [Hermite Functions and Recurrence 的【定義 1】](Hermite_Functions_and_Recurrence.md) 裡 $\left(\pi^{1/2}2^{n}n!\right)^{-1/2}$ 這個係數被**刻意挑成如此**的結果。

換句話說：$c_n$ 那個看起來莫名其妙的 $2^{n}n!$，唯一的任務就是讓升算子 $\hat{y} - \dfrac{d}{d\hat{y}}$ 在除以 $2a_n$ 之後**保範**。有了它，只需要驗證 $\mathcal{H}_0$ 一階（【推導 9】），其餘無窮多階全部自動成立。

### 這兩件事在赤道波理論裡各自負責什麼

* **【證明 (d)】正交歸一** —— 讓「把場展開成 $\sum_n(\cdot)\mathcal{H}_n$」這件事可逆：投影係數只要做一次內積就取得到，不必解聯立。赤道波的正規模態轉換整個押在這上面。
* **【證明 (a)】本徵值 $-(2n+1)$** —— 讓含 $\dfrac{d^{2}}{d\hat{y}^{2}} - \hat{y}^{2}$ 的橢圓型算子在譜空間退化成**一個純量除法**。赤道 PV 可逆性原理之所以能寫成「除以 $m^{2} + \epsilon^{1/2}(2n+1)$」這麼簡單的一行，就是這條本徵性質的直接後果。
