# 穩定度矩陣與雅可比行列式之關係證明 (Axisymmetric Stability Matrix and Jacobian Matrix )

+++



## 證明目標

證明在圓柱座標系下，穩定度矩陣的行列式（$AC - B^2$）與絕對角動量及浮力的雅可比行列式（Jacobian）存在以下關係：

$$AC - B^2 = \frac{1}{\rho^2 r} \left(f+\frac{2v}{r}\right) J(M, b)$$


+++


## 假設與已知 (Assumptions & Preliminaries)

為了確保推導邏輯嚴密且無循環引用，我們依序定義所需的物理量與數學工具：

* **【定義 1】 絕對角動量 (Absolute Angular Momentum, $M$) 與其偏導數：**
    單位質量的空氣塊具有相對於地球的旋轉角動量與隨地球自轉的角動量。
    $$M(r,z) \overset{\text{def}}{=} r v(r,z) + \frac{1}{2}fr^2$$
    * 徑向偏微分：$\frac{\partial M}{\partial r} = v + r\frac{\partial v}{\partial r} + fr = r\left(f + \frac{v}{r} + \frac{\partial v}{\partial r}\right) = r(f+\zeta)$
    * 垂直偏微分：$\frac{\partial M}{\partial z} = r\frac{\partial v}{\partial z}$

* **【已知 1】 嚴格定義之次環流結構參數 (Eliassen Coefficients)：**
    包含大氣密度 $\rho$ 的穩定度參數定義：
    * 垂直穩定度 (Static Stability)： $\rho A \overset{\text{def}}{=} \frac{\partial b}{\partial z}$
    * 斜壓性 / 熱力風 (Baroclinicity)： $\rho B \overset{\text{def}}{=} -\frac{\partial b}{\partial r} = -\left(f+\frac{2v}{r}\right)\frac{\partial v}{\partial z}$
    * 慣性穩定度 (Inertial Stability)： $\rho C \overset{\text{def}}{=} \left(f+\frac{2v}{r}\right)(f+\zeta)$

* **【已知 2】 結構參數之移項替換：**
    由【已知 1】直接移項可得以下四條替換式，以供後續替換偏微分項：
    * $\frac{\partial b}{\partial z} = \rho A$
    * $\frac{\partial b}{\partial r} = -\rho B$
    * $\frac{\partial v}{\partial z} = -\frac{\rho B}{f+\frac{2v}{r}}$
    * $f+\zeta = \frac{\rho C}{f+\frac{2v}{r}}$

* **【定義 2】 圓柱座標的雅可比行列式 (Jacobian Determinant)：**
    在圓柱座標 $(r, z)$ 平面上，表示絕對角動量 $M$ 與浮力 $b$ 在空間中梯度交角的數學運算子：
    $$J(M, b) \overset{\text{def}}{=} \frac{\partial (M,b)}{\partial (r,z)} = \frac{\partial M}{\partial r}\frac{\partial b}{\partial z} - \frac{\partial M}{\partial z}\frac{\partial b}{\partial r}$$


+++



## 證明

這段證明的核心思路非常純粹：**從雅可比行列式 $J(M, b)$ 的定義出發，利用連鎖律與我們準備好的已知條件，將偏微分項全部替換為大氣動力參數 $A, B, C$，最後移項即可得證。**

$$\begin{gather*}
J(M, b) &\overset{\text{定義 2}}{=}& \frac{\partial M}{\partial r}\frac{\partial b}{\partial z} - \frac{\partial M}{\partial z}\frac{\partial b}{\partial r} \\
J(M, b) &\overset{\text{定義 1}}{=}& \left[ r(f+\zeta) \right] \frac{\partial b}{\partial z} - \left[ r\frac{\partial v}{\partial z} \right] \frac{\partial b}{\partial r} \\
J(M, b) &\overset{\text{已知 2}}{=}& \left[ r(f+\zeta) \right] (\rho A) - \left[ r\frac{\partial v}{\partial z} \right] (-\rho B) \\
J(M, b) &=& \rho r \left[ (f+\zeta)A + \frac{\partial v}{\partial z}B \right] \\
J(M, b) &\overset{\text{已知 2}}{=}& \rho r \left[ \left( \frac{\rho C}{f+\frac{2v}{r}} \right) A + \left( \frac{-\rho B}{f+\frac{2v}{r}} \right) B \right] \\
J(M, b) &=& \frac{\rho^2 r}{f+\frac{2v}{r}} \left( AC - B^2 \right) \\
\frac{f+\frac{2v}{r}}{\rho^2 r} J(M, b) &=& AC - B^2 \\
AC - B^2 &=& \frac{1}{\rho^2 r} \left(f+\frac{2v}{r}\right) J(M, b)
\end{gather*}$$

---

## 💡 直觀比喻：動力與熱力的交織網路



這條簡潔的方程式蘊含了非常深刻的物理意義。我們可以把它想像成是一張大自然編織的「網子」：

* **$J(M, b)$ 是網子的形狀**：它代表著「等角動量線 ($M$)」與「等浮力線 ($b$)」在空間中交錯切割出來的平行四邊形面積。如果這兩組線完全平行（正壓大氣，$J=0$），這張網子就塌陷了；如果它們互相交錯（斜壓大氣），大氣就具備了將熱能轉換為動能的潛力。
* **$AC - B^2$ 是網子的彈性**：這就是我們熟悉的系統穩定度。

這個方程式完美地告訴我們：一個大氣系統到底穩不穩定（$AC-B^2$ 的正負號），其實就直接寫在了動力場 ($M$) 與熱力場 ($b$) 互相交錯的幾何結構 ($J$) 之中！而前面的係數 $\frac{1}{\rho^2 r}\left(f+\frac{2v}{r}\right)$，只是座標系與旋轉慣性給予的一個正值權重罷了。

+++
