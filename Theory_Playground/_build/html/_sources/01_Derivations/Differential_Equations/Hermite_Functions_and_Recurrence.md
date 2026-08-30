# Hermite Functions and Recurrence (歸一化 Hermite 函數的遞迴與微分關係)

+++

## 證明目標:

* (a) 歸一化 Hermite 函數（在赤道波理論中稱為「經向結構函數」）滿足**遞迴關係**：

$$\hat{y}\,\mathcal{H}_n(\hat{y}) = \left(\frac{n+1}{2}\right)^{1/2}\mathcal{H}_{n+1}(\hat{y}) + \left(\frac{n}{2}\right)^{1/2}\mathcal{H}_{n-1}(\hat{y})$$

* (b) 同一組函數滿足**微分關係**：

$$\frac{d\mathcal{H}_n(\hat{y})}{d\hat{y}} = -\left(\frac{n+1}{2}\right)^{1/2}\mathcal{H}_{n+1}(\hat{y}) + \left(\frac{n}{2}\right)^{1/2}\mathcal{H}_{n-1}(\hat{y})$$

* (c) 最低階的顯式形式：

$$\mathcal{H}_0(\hat{y}) = \pi^{-1/4}\,e^{-\hat{y}^{2}/2}$$

* (d) 次低階的顯式形式，可由 (a)(c) 直接生出：

$$\mathcal{H}_1(\hat{y}) = 2^{1/2}\pi^{-1/4}\,\hat{y}\,e^{-\hat{y}^{2}/2}$$

* 註：$\mathcal{H}_n$ 本身的**定義式**是【定義 2】，不列為證明目標。(a)(b) 這一對關係最關鍵的性質是**右端只出現 $\mathcal{H}_{n\pm1}$** —— 乘 $\hat{y}$ 與微分都不會跑出這組基底之外，這是後續赤道波推導能保持封閉的原因，見【數值與結構解釋】。
* 註：本檔是純數學結果，$\hat{y}$ 為無因次自變數，故符號清單的單位欄一律為 $[\text{無單位}]$。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [Hermite 多項式的生成函數 (Generating function of the Hermite polynomials)](https://dlmf.nist.gov/18.12#E15)：** 物理學慣例的 Hermite 多項式 $H_n$ 由下式定義，本檔直接引用不再重證

  $$e^{2\hat{y}t - t^{2}} = \sum_{n=0}^{\infty} H_n(\hat{y})\,\frac{t^{n}}{n!}$$

  * $\hat{y}$ : 無因次自變數 (Dimensionless independent variable) $[\text{無單位}]$
  * $t$ : 生成函數的形式參數 (Formal parameter of the generating function) $[\text{無單位}]$
  * $H_n(\hat{y})$ : 第 $n$ 階 Hermite 多項式 (The $n$-th Hermite polynomial) $[\text{無單位}]$
  * $n$ : 階數 (Order index) $[\text{無單位}]$

* **【已知 2】 冪級數的逐項運算 (Term-by-term operations on a power series)：** 冪級數在其收斂半徑內的兩條標準性質，本檔直接引用不再重證

  * (a) 逐項微分定理 —— 收斂半徑內可與求和交換微分（對 $t$、對出現在係數中的 $\hat{y}$ 皆然）：

    $$\frac{\partial}{\partial s}\left[\sum_{n=0}^{\infty} g_n(\hat{y})\,\frac{t^{n}}{n!}\right] = \sum_{n=0}^{\infty} \frac{\partial}{\partial s}\left[g_n(\hat{y})\,\frac{t^{n}}{n!}\right] \qquad \left(s = t \ \text{或}\ \hat{y}\right)$$

  * (b) 恆等定理（係數唯一性）—— 兩個冪級數在收斂區內恆等，則同次項係數相等：

    $$\begin{gather*}
    &\sum_{n=0}^{\infty} A_n\,\frac{t^{n}}{n!} &=& \sum_{n=0}^{\infty} B_n\,\frac{t^{n}}{n!}  \\
    \iff &A_n &=& B_n \quad \left(\forall\, n \ge 0\right)
    \end{gather*}$$

  * $g_n(\hat{y})$ : 冪級數的第 $n$ 階係數函數 (The $n$-th coefficient function) $[\text{無單位}]$
  * $s$ : 被微分的自變數 (Variable of differentiation) $[\text{無單位}]$
  * $A_n,\ B_n$ : 兩個冪級數的第 $n$ 階係數 (Coefficients of the two power series) $[\text{無單位}]$
  * $\hat{y}$ : 無因次自變數 (Dimensionless independent variable) $[\text{無單位}]$
  * $t$ : 生成函數的形式參數 (Formal parameter of the generating function) $[\text{無單位}]$

* **【假設 1】 生成函數為整函數 (The generating function is entire)：** $e^{2\hat{y}t-t^{2}}$ 對 $t$ 而言處處解析，其 Taylor 級數收斂半徑為無窮大

  $$R_{\text{conv}} \to \infty$$

  * $R_{\text{conv}}$ : 【已知 1】右端冪級數的收斂半徑 (Radius of convergence) $[\text{無單位}]$
  * 註：本條是【已知 2】(a)(b) 能套用在【已知 1】上的前提；少了它，逐項微分與比對係數都不合法。

* **【定義 1】 歸一化常數 (Normalization constant)：** 把 Hermite 多項式壓成單位範數所需的比例因子

  $$c_n \overset{\text{def}}{=} \left(\pi^{1/2}\,2^{n}\,n!\right)^{-1/2}$$

  * $c_n$ : 第 $n$ 階歸一化常數 (The $n$-th normalization constant) $[\text{無單位}]$

* **【定義 2】 歸一化 Hermite 函數（經向結構函數）(Normalized Hermite function / meridional structure function)：** Hermite 多項式乘上高斯包絡再歸一化

  * (a) 主定義：

    $$\mathcal{H}_n(\hat{y}) \overset{\text{def}}{=} c_n\,H_n(\hat{y})\,e^{-\hat{y}^{2}/2}$$

  * (b) 負階約定，使 (a) 的遞迴式在 $n = 0$ 時仍有意義：

    $$\mathcal{H}_{-1}(\hat{y}) \overset{\text{def}}{=} 0$$

  * $\mathcal{H}_n(\hat{y})$ : 第 $n$ 階歸一化 Hermite 函數 (The $n$-th normalized Hermite function) $[\text{無單位}]$
  * $\hat{y}$ : 無因次自變數 (Dimensionless independent variable) $[\text{無單位}]$
  * $c_n$ : 第 $n$ 階歸一化常數 (The $n$-th normalization constant) $[\text{無單位}]$
  * $H_n(\hat{y})$ : 第 $n$ 階 Hermite 多項式 (The $n$-th Hermite polynomial) $[\text{無單位}]$
  * 註：把【定義 1】代入【定義 2】(a) 即得展開形式 $\mathcal{H}_n = \left(\pi^{1/2}2^{n}n!\right)^{-1/2}H_n\,e^{-\hat{y}^{2}/2}$。

* **【推導 1】 Hermite 多項式的遞迴與微分關係 (Recurrence and derivative relations of the Hermite polynomials)：** 對【已知 1】兩側分別取 $\partial/\partial t$ 與 $\partial/\partial\hat{y}$，再比對 $t^{n}/n!$ 的係數

  * (a) 對 $t$ 微分並比對係數，得遞迴關係：

    $$\begin{gather*}
    \left(2\hat{y} - 2t\right)e^{2\hat{y}t-t^{2}} &\overset{\text{已知 1}}{=}& \frac{\partial}{\partial t}\left[\sum_{n=0}^{\infty} H_n\,\frac{t^{n}}{n!}\right] \\
    \left(2\hat{y} - 2t\right)\sum_{n=0}^{\infty} H_n\,\frac{t^{n}}{n!} &\overset{\text{已知 1,已知 2(a),假設 1}}{=}& \sum_{n=1}^{\infty} H_n\,\frac{t^{n-1}}{(n-1)!} \\
    \sum_{n=0}^{\infty} 2\hat{y}H_n\,\frac{t^{n}}{n!} - \sum_{n=0}^{\infty} 2H_n\,\frac{t^{n+1}}{n!} &=& \sum_{n=0}^{\infty} H_{n+1}\,\frac{t^{n}}{n!} \\
    \sum_{n=0}^{\infty} 2\hat{y}H_n\,\frac{t^{n}}{n!} - \sum_{n=1}^{\infty} 2nH_{n-1}\,\frac{t^{n}}{n!} &=& \sum_{n=0}^{\infty} H_{n+1}\,\frac{t^{n}}{n!} \\
    2\hat{y}H_n - 2nH_{n-1} &\overset{\text{已知 2(b),假設 1}}{=}& H_{n+1} \\
    \hat{y}H_n &=& \frac{1}{2}H_{n+1} + nH_{n-1}
    \end{gather*}$$

  * (b) 對 $\hat{y}$ 微分並比對係數，得微分關係：

    $$\begin{gather*}
    2t\,e^{2\hat{y}t-t^{2}} &\overset{\text{已知 1}}{=}& \frac{\partial}{\partial \hat{y}}\left[\sum_{n=0}^{\infty} H_n\,\frac{t^{n}}{n!}\right] \\
    2t\sum_{n=0}^{\infty} H_n\,\frac{t^{n}}{n!} &\overset{\text{已知 1,已知 2(a),假設 1}}{=}& \sum_{n=0}^{\infty} \frac{dH_n}{d\hat{y}}\,\frac{t^{n}}{n!} \\
    \sum_{n=0}^{\infty} 2H_n\,\frac{t^{n+1}}{n!} &=& \sum_{n=0}^{\infty} \frac{dH_n}{d\hat{y}}\,\frac{t^{n}}{n!} \\
    \sum_{n=1}^{\infty} 2nH_{n-1}\,\frac{t^{n}}{n!} &=& \sum_{n=0}^{\infty} \frac{dH_n}{d\hat{y}}\,\frac{t^{n}}{n!} \\
    \frac{dH_n}{d\hat{y}} &\overset{\text{已知 2(b),假設 1}}{=}& 2nH_{n-1}
    \end{gather*}$$

  * $\hat{y}$ : 無因次自變數 (Dimensionless independent variable) $[\text{無單位}]$
  * $t$ : 生成函數的形式參數 (Formal parameter of the generating function) $[\text{無單位}]$
  * $H_n(\hat{y})$ : 第 $n$ 階 Hermite 多項式 (The $n$-th Hermite polynomial) $[\text{無單位}]$
  * $n$ : 階數 (Order index) $[\text{無單位}]$
  * 註：第三列到第四列做的是同一件事 —— 把 $\sum_{n\ge0}(\cdots)\frac{t^{n+1}}{n!}$ 平移指標成 $\sum_{n\ge1}(\cdots)\frac{t^{n}}{n!}$，其中 $\frac{1}{(n-1)!} = \frac{n}{n!}$。
  * 註：(a)(b) 在 $n = 0$ 時右端含 $H_{-1}$ 的項係數為零（$n = 0$），故不需要對 $H_{-1}$ 另立約定。

* **【推導 2】 Hermite 多項式的起始值 (Starting value of the Hermite polynomials)：** 在【已知 1】中令 $t = 0$，右端只剩 $n = 0$ 一項

  $$\begin{gather*}
  1 &=& e^{2\hat{y}\cdot 0 - 0^{2}} \\
  1 &\overset{\text{已知 1}}{=}& \sum_{n=0}^{\infty} H_n(\hat{y})\,\frac{0^{n}}{n!} \\
  1 &=& H_0(\hat{y})
  \end{gather*}$$

  * $\hat{y}$ : 無因次自變數 (Dimensionless independent variable) $[\text{無單位}]$
  * $H_n(\hat{y})$ : 第 $n$ 階 Hermite 多項式 (The $n$-th Hermite polynomial) $[\text{無單位}]$
  * $n$ : 階數 (Order index) $[\text{無單位}]$
  * 註：第二列到第三列用到冪級數在原點取值的標準約定 $0^{0} = 1$、$0^{n} = 0\ (n \ge 1)$，故整個級數只剩 $n = 0$ 那一項。

* **【推導 3】 高斯包絡的導數 (Derivative of the Gaussian envelope)：** 連鎖律的直接結果，先算掉以免污染主證明

  $$\begin{gather*}
  \frac{d}{d\hat{y}}\left[e^{-\hat{y}^{2}/2}\right] &=& e^{-\hat{y}^{2}/2}\cdot\frac{d}{d\hat{y}}\left[-\frac{\hat{y}^{2}}{2}\right] \\
  &=& -\hat{y}\,e^{-\hat{y}^{2}/2}
  \end{gather*}$$

  * $\hat{y}$ : 無因次自變數 (Dimensionless independent variable) $[\text{無單位}]$

* **【推導 4】 歸一化常數的相鄰比 (Ratios of adjacent normalization constants)：** 把 $2^{n}n!$ 這種會溢位的組合**提前約掉**，主證明才不會被階乘淹沒

  * (a) 與上一階的比：

    $$\begin{gather*}
    \frac{c_n}{c_{n+1}} &\overset{\text{定義 1}}{=}& \frac{\left(\pi^{1/2}2^{n}n!\right)^{-1/2}}{\left(\pi^{1/2}2^{n+1}(n+1)!\right)^{-1/2}} \\
    &=& \left[\frac{\pi^{1/2}2^{n+1}(n+1)!}{\pi^{1/2}2^{n}n!}\right]^{1/2} \\
    &=& \left[2(n+1)\right]^{1/2}
    \end{gather*}$$

  * (b) 與下一階的比：

    $$\begin{gather*}
    \frac{c_n}{c_{n-1}} &\overset{\text{定義 1}}{=}& \frac{\left(\pi^{1/2}2^{n}n!\right)^{-1/2}}{\left(\pi^{1/2}2^{n-1}(n-1)!\right)^{-1/2}} \\
    &=& \left[\frac{\pi^{1/2}2^{n-1}(n-1)!}{\pi^{1/2}2^{n}n!}\right]^{1/2} \\
    &=& \left[\frac{1}{2n}\right]^{1/2}
    \end{gather*}$$

  * $c_n$ : 第 $n$ 階歸一化常數 (The $n$-th normalization constant) $[\text{無單位}]$
  * $n$ : 階數 (Order index) $[\text{無單位}]$

+++

## 證明:

### (a) proof 遞迴關係 (Recurrence relation)

從【定義 2】(a) 起手，用【推導 1】(a) 換掉 $\hat{y}H_n$，再用【推導 4】把歸一化常數的比值代進去。

$$\begin{gather*}
\hat{y}\,\mathcal{H}_n &\overset{\text{定義 2(a)}}{=}& \hat{y}\,c_nH_n\,e^{-\hat{y}^{2}/2} \\
&\overset{\text{推導 1(a)}}{=}& c_n\left[\frac{1}{2}H_{n+1} + nH_{n-1}\right]e^{-\hat{y}^{2}/2} \\
&=& \frac{1}{2}\,c_nH_{n+1}\,e^{-\hat{y}^{2}/2} + n\,c_nH_{n-1}\,e^{-\hat{y}^{2}/2} \\
&=& \frac{1}{2}\frac{c_n}{c_{n+1}}\left[c_{n+1}H_{n+1}\,e^{-\hat{y}^{2}/2}\right] + n\frac{c_n}{c_{n-1}}\left[c_{n-1}H_{n-1}\,e^{-\hat{y}^{2}/2}\right] \\
&\overset{\text{定義 2(a)}}{=}& \frac{1}{2}\frac{c_n}{c_{n+1}}\,\mathcal{H}_{n+1} + n\frac{c_n}{c_{n-1}}\,\mathcal{H}_{n-1} \\
&\overset{\text{推導 4(a)(b)}}{=}& \frac{1}{2}\left[2(n+1)\right]^{1/2}\mathcal{H}_{n+1} + n\left[\frac{1}{2n}\right]^{1/2}\mathcal{H}_{n-1} \\
&=& \left[\frac{2(n+1)}{4}\right]^{1/2}\mathcal{H}_{n+1} + \left[\frac{n^{2}}{2n}\right]^{1/2}\mathcal{H}_{n-1} \\
&=& \left(\frac{n+1}{2}\right)^{1/2}\mathcal{H}_{n+1} + \left(\frac{n}{2}\right)^{1/2}\mathcal{H}_{n-1}
\end{gather*}$$

### (b) proof 微分關係 (Derivative relation)

對【定義 2】(a) 微分會生出兩項：Hermite 多項式的導數由【推導 1】(b) 接手，高斯包絡的導數由【推導 3】接手；最後冒出的 $\hat{y}\mathcal{H}_n$ 再用【證明 (a)】消掉。

$$\begin{gather*}
\frac{d\mathcal{H}_n}{d\hat{y}} &\overset{\text{定義 2(a)}}{=}& \frac{d}{d\hat{y}}\left[c_nH_n\,e^{-\hat{y}^{2}/2}\right] \\
&=& c_n\frac{dH_n}{d\hat{y}}\,e^{-\hat{y}^{2}/2} + c_nH_n\frac{d}{d\hat{y}}\left[e^{-\hat{y}^{2}/2}\right] \\
&\overset{\text{推導 1(b),推導 3}}{=}& c_n\left[2nH_{n-1}\right]e^{-\hat{y}^{2}/2} - c_nH_n\,\hat{y}\,e^{-\hat{y}^{2}/2} \\
&=& 2n\frac{c_n}{c_{n-1}}\left[c_{n-1}H_{n-1}\,e^{-\hat{y}^{2}/2}\right] - \hat{y}\left[c_nH_n\,e^{-\hat{y}^{2}/2}\right] \\
&\overset{\text{定義 2(a)}}{=}& 2n\frac{c_n}{c_{n-1}}\,\mathcal{H}_{n-1} - \hat{y}\,\mathcal{H}_n \\
&\overset{\text{推導 4(b)}}{=}& 2n\left[\frac{1}{2n}\right]^{1/2}\mathcal{H}_{n-1} - \hat{y}\,\mathcal{H}_n \\
&=& \left[\frac{4n^{2}}{2n}\right]^{1/2}\mathcal{H}_{n-1} - \hat{y}\,\mathcal{H}_n \\
&=& \left(2n\right)^{1/2}\mathcal{H}_{n-1} - \hat{y}\,\mathcal{H}_n \\
&\overset{\text{證明 (a)}}{=}& \left(2n\right)^{1/2}\mathcal{H}_{n-1} - \left(\frac{n+1}{2}\right)^{1/2}\mathcal{H}_{n+1} - \left(\frac{n}{2}\right)^{1/2}\mathcal{H}_{n-1} \\
&=& -\left(\frac{n+1}{2}\right)^{1/2}\mathcal{H}_{n+1} + \left[\left(2n\right)^{1/2} - \left(\frac{n}{2}\right)^{1/2}\right]\mathcal{H}_{n-1} \\
&=& -\left(\frac{n+1}{2}\right)^{1/2}\mathcal{H}_{n+1} + \left[2\left(\frac{n}{2}\right)^{1/2} - \left(\frac{n}{2}\right)^{1/2}\right]\mathcal{H}_{n-1} \\
&=& -\left(\frac{n+1}{2}\right)^{1/2}\mathcal{H}_{n+1} + \left(\frac{n}{2}\right)^{1/2}\mathcal{H}_{n-1}
\end{gather*}$$

### (c) proof 最低階的顯式形式 (Lowest-order explicit form)

把【定義 2】(a) 取 $n = 0$，歸一化常數與 Hermite 多項式都退化成最簡單的情形。

$$\begin{gather*}
\mathcal{H}_0 &\overset{\text{定義 2(a)}}{=}& c_0\,H_0\,e^{-\hat{y}^{2}/2} \\
&\overset{\text{定義 1}}{=}& \left(\pi^{1/2}\,2^{0}\,0!\right)^{-1/2}H_0\,e^{-\hat{y}^{2}/2} \\
&=& \left(\pi^{1/2}\right)^{-1/2}H_0\,e^{-\hat{y}^{2}/2} \\
&\overset{\text{推導 2}}{=}& \pi^{-1/4}\cdot 1\cdot e^{-\hat{y}^{2}/2} \\
&=& \pi^{-1/4}\,e^{-\hat{y}^{2}/2}
\end{gather*}$$

### (d) proof 次低階的顯式形式 (Next-order explicit form)

把【證明 (a)】的遞迴關係取 $n = 0$，就能只用 $\mathcal{H}_0$ 生出 $\mathcal{H}_1$ —— 這正是論文建議的數值遞迴起點。

$$\begin{gather*}
\hat{y}\,\mathcal{H}_0 &\overset{\text{證明 (a)}}{=}& \left(\frac{0+1}{2}\right)^{1/2}\mathcal{H}_{1} + \left(\frac{0}{2}\right)^{1/2}\mathcal{H}_{-1} \\
\hat{y}\,\mathcal{H}_0 &\overset{\text{定義 2(b)}}{=}& \left(\frac{1}{2}\right)^{1/2}\mathcal{H}_{1} \\
\mathcal{H}_1 &=& 2^{1/2}\,\hat{y}\,\mathcal{H}_0 \\
\mathcal{H}_1 &\overset{\text{證明 (c)}}{=}& 2^{1/2}\pi^{-1/4}\,\hat{y}\,e^{-\hat{y}^{2}/2}
\end{gather*}$$

+++

## 數值與結構解釋

### 為什麼是 $\mathcal{H}_n$ 而不是 $H_n$

Hermite 多項式 $H_n$ 本身在 $|\hat{y}|$ 大時**發散**，$e^{-\hat{y}^{2}/2}$ 這層高斯包絡才把它壓成一個**平方可積**的函數。歸一化常數 $c_n$ 則進一步讓它的範數為 $1$。

代價是【證明 (a)(b)】右端的係數從 $H_n$ 那組乾淨的 $\frac{1}{2}$ 與 $n$，變成帶根號的 $\left(\frac{n+1}{2}\right)^{1/2}$ 與 $\left(\frac{n}{2}\right)^{1/2}$。這個「醜化」是**值得的**：兩條關係的係數在 $\mathcal{H}_n$ 之下變成**對稱**的（$\mathcal{H}_{n+1}$ 與 $\mathcal{H}_{n-1}$ 的權重同形），而在 $H_n$ 之下則完全不對稱（$\frac{1}{2}$ vs. $n$）。這個對稱性正是赤道波本徵函數能寫成緊湊 $\mathcal{H}_{n\pm1}$ 組合的原因。

### 遞迴的閉合性：乘 $\hat{y}$ 與微分都跑不出去

把【證明 (a)(b)】並排看：

$$\hat{y}\,\mathcal{H}_n = \left(\frac{n+1}{2}\right)^{1/2}\mathcal{H}_{n+1} + \left(\frac{n}{2}\right)^{1/2}\mathcal{H}_{n-1}$$

$$\frac{d\mathcal{H}_n}{d\hat{y}} = -\left(\frac{n+1}{2}\right)^{1/2}\mathcal{H}_{n+1} + \left(\frac{n}{2}\right)^{1/2}\mathcal{H}_{n-1}$$

兩式的右端**只差一個負號**。這代表在 $\left\{\mathcal{H}_n\right\}$ 這組基底上，「乘 $\hat{y}$」與「對 $\hat{y}$ 微分」這兩個算子都只是**往上一階、往下一階各走一步**（三對角矩陣）。

赤道 $\beta$ 平面的線性方程組裡，出現的正好就是 $\beta y\,(\cdot)$ 與 $d(\cdot)/dy$ 兩種操作。閉合性因此保證：只要解形如 $\mathcal{H}_n$，方程組就會塌縮成幾條 $\mathcal{H}_{n\pm1}$ 之間的代數關係，而不會生出無窮多個新函數。

把兩式**相加**與**相減**還可以直接讀出升降算子：

$$\left(\hat{y} + \frac{d}{d\hat{y}}\right)\mathcal{H}_n = \left(2n\right)^{1/2}\mathcal{H}_{n-1}$$

$$\left(\hat{y} - \frac{d}{d\hat{y}}\right)\mathcal{H}_n = \left(2(n+1)\right)^{1/2}\mathcal{H}_{n+1}$$

這就是量子諧振子的湮滅／產生算子。

### 為什麼實作時一定要走遞迴

【證明 (c)(d)】給了 $\mathcal{H}_0$ 與 $\mathcal{H}_1$，之後全部用【證明 (a)】往上遞推：

$$\mathcal{H}_{n+1} = \left(\frac{2}{n+1}\right)^{1/2}\left[\hat{y}\,\mathcal{H}_n - \left(\frac{n}{2}\right)^{1/2}\mathcal{H}_{n-1}\right]$$

**不要**先算 $H_n$ 再套【定義 2】(a)。原因在【推導 4】已經看得很清楚：$c_n$ 裡有 $2^{n}n!$，而赤道波的譜解要遞迴到 $n = 200$ —— 此時 $2^{200}\cdot 200! \sim 10^{435}$，雙精度浮點數（上限約 $10^{308}$）**直接溢位**。反觀上面的遞迴式，係數 $\left(\frac{2}{n+1}\right)^{1/2}$ 與 $\left(\frac{n}{2}\right)^{1/2}$ 都是 $O(n^{\pm1/2})$ 的溫和數字，而 $\mathcal{H}_n$ 本身始終是 $O(1)$ 量級。**大數從頭到尾沒有被顯式算出來過**，這就是【推導 4】那兩個比值真正的價值。
